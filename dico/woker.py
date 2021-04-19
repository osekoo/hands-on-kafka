import json
from kafka import KafkaConsumer, KafkaProducer

from dico.crawler import Crawler, CrawlerEN, CrawlerFR
from dico.kafka_data import KafkaRequest, KafkaResponse
from dico.config import BOOTSTRAP_SERVER, TOPIC_DICO_FR, TOPIC_DICO_EN


class KafkaWorker:

    def __init__(self, topic_name: str, crawler: Crawler):
        self.topic_name = topic_name
        self.crawler = crawler
        self.consumer = None
        self.producer = None

    def connect(self):
        self.consumer = KafkaConsumer(self.topic_name,
                                      bootstrap_servers=BOOTSTRAP_SERVER,
                                      value_deserializer=self.data_deserializer,
                                      auto_offset_reset='earliest',
                                      enable_auto_commit=True,
                                      auto_commit_interval_ms=500,
                                      group_id=self.topic_name + '-group')

        self.producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER,
                                      value_serializer=self.data_serializer)

    def consume(self):
        if not self.consumer:
            self.connect()
        for data in self.consumer:
            self.__handle_word(data.value)

    def __handle_word(self, data: KafkaRequest):
        """
        Requests the definition of the word and send it back to the requester
        :return:
        """
        print(f'handling the word: {data.word} ...')
        word_def = self.crawler.get_definition(data.word)
        message = KafkaResponse(data.word, word_def)
        self.producer.send(data.response_topic, value=message)

    @staticmethod
    def data_deserializer(data) -> KafkaRequest:
        """
        Converts the given data into json format
        :param data: given data to convert into json
        :return: KafkaRequest data
        """
        jdata = json.loads(data.decode('utf-8'))
        return KafkaRequest(**jdata)

    @staticmethod
    def data_serializer(data: KafkaResponse):
        """
        Converts the given data into json format
        :param data: given data to convert into json
        :return: json data
        """
        return json.dumps(data.__dict__).encode('utf-8')


if __name__ == "__main__":
    worker = None
    dico_name = input('Which dictionary? ')
    if dico_name == 'en':
        worker = KafkaWorker(TOPIC_DICO_EN, CrawlerEN())
    else:
        worker = KafkaWorker(TOPIC_DICO_FR, CrawlerFR())

    print(f'dico worker {dico_name} worker started.')
    worker.consume()
