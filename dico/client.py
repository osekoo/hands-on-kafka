import json
import threading

from kafka import KafkaConsumer, KafkaProducer

from dico.kafka_data import KafkaRequest, KafkaResponse
from dico.config import BOOTSTRAP_SERVER, TOPIC_DICO_FR, TOPIC_DICO_EN


class KafkaClient:

    def __init__(self, dico_topic_name: str, response_topic_name: str):
        self.dico_topic_name = dico_topic_name
        self.response_topic_name = response_topic_name
        self.producer = None
        self.consumer = None

    def connect(self):
        self.producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER,
                                      value_serializer=self.data_serializer)

        self.consumer = KafkaConsumer(self.response_topic_name,
                                      bootstrap_servers=BOOTSTRAP_SERVER,
                                      value_deserializer=self.data_deserializer,
                                      auto_offset_reset='earliest',
                                      enable_auto_commit=True,
                                      group_id=self.response_topic_name + '-group')

    def produce(self):
        if not self.producer:
            self.connect()
        print('enter the word to search')
        word = None
        while word != '':
            word = input()
            if word != '':
                data = KafkaRequest(word, self.response_topic_name)
                self.producer.send(self.dico_topic_name, data)

    def read_definition(self):
        if not self.consumer:
            self.connect()
        for data in self.consumer:
            print(data.value)

    @staticmethod
    def data_deserializer(data) -> KafkaResponse:
        """
        Converts the given data into json format
        :param data: given data to convert into json
        :return: KafkaRequest data
        """
        jdata = json.loads(data.decode('utf-8'))
        return KafkaResponse(**jdata)

    @staticmethod
    def data_serializer(data: KafkaRequest):
        """
        Converts the given data into json format
        :param data: given data to convert into json
        :return: json data
        """
        return json.dumps(data.__dict__).encode('utf-8')


if __name__ == "__main__":
    dico_name = input('Which dictionary? ')
    dico_name = TOPIC_DICO_EN if dico_name == 'en' else TOPIC_DICO_FR

    your_name = input('Your nickname? ')

    def_producer = KafkaClient(dico_name, dico_name + '-' + your_name)

    reading_thread = threading.Thread(target=def_producer.read_definition)
    reading_thread.start()

    print(f'dico client {dico_name} started.')
    def_producer.produce()
