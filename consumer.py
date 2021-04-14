import time
import json

from kafka import KafkaConsumer


def data_deserializer(data):
    """
    Converts the given data into json format
    :param data: given data to convert into json
    :return: json data
    """
    return json.loads(data.decode('utf-8'))


def receive(consumer):
    for data in consumer:
        print(data.value)
        # time.sleep(1)


print('connecting the consumer to Kafka bootstrap server...')
consumer_handler = KafkaConsumer('my-topic',
                                 bootstrap_servers='localhost:9092',
                                 value_deserializer=data_deserializer,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True,
                                 group_id='my-consumer-group')

print('reading data from Kafka...')
receive(consumer_handler)
