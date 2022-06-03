from json import loads
from kafka import KafkaConsumer
import requests

consumer = KafkaConsumer(
    'message_data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    auto_commit_interval_ms=100
)

for message in consumer:
    user_id = message.value['user_id']
    mes = message.value['message']
    text_message = mes.split(" ")

    flag = True

    for word in text_message:
        if word.lower() == 'абракадабра':
            flag = False
            break

    requests.post("http://localhost:8000/api/v1/message_confirmation",
                  json={"message_id": user_id,
                        "text_message": mes,
                        "success": flag},
                  headers={"Authorization": "ccA1CDAFCbe6Ca984F88614B4eD00495Ccb3291e29fD0c0192d4C1CF8274e7B8"})
