from json import dumps
from kafka import KafkaProducer

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def in_kafka_addter(user_id, message):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    message_data = {"user_id": user_id,
                    "message": message}

    producer.send(topic='message_data', value=message_data)
