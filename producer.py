import time
import json

from kafka import KafkaProducer


def data_serializer(data):
    """
    Converts the given data into json format
    :param data: given data to convert into json
    :return: json data
    """
    return json.dumps(data).encode('utf-8')


def send(producer, size):
    for i in range(size):
        message = {'message': i}
        if i % 100 == 0:
            print('sending message %d ...', i)
        producer.send('my_topic', value=message)
        time.sleep(1)

    producer.flush()


def send_with_key(producer, size, key_mod):
    for i in range(size):
        message = {'message': i}
        key = i % key_mod
        if i % 100 == 0:
            print('sending message %d ...', i)
        producer.send('my-topic', key=str.encode(f'{key}'), value=message)
        time.sleep(1)

    producer.flush()


print('connecting the producer to Kafka bootstrap server...')
producer_handler = KafkaProducer(bootstrap_servers='localhost:9092',
                                 value_serializer=data_serializer)

# send(producer_handler, 1000)

send_with_key(producer_handler, 1000, 7)
