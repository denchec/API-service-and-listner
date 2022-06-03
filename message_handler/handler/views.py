from django.http import HttpResponse
import json
import handler.in_kafka_addter as addter
import handler.add_post as add_post


def get_message(request):
    if request.method == "POST":
        print(request)
        message_data = json.loads(request.body.decode())
        user_id = message_data["user_id"]
        message = message_data["message"]

        query = add_post.Query(user_id, message)
        query.insert()

        addter.in_kafka_addter(user_id, message)

        return HttpResponse(f"{user_id} {message} на проверке")


def update_message_status(request):
    if request.method == "POST" and request.headers["Authorization"] == "ccA1CDAFCbe6Ca984F88614B4eD00495Ccb3291e29fD0c0192d4C1CF8274e7B8":
        message_data = json.loads(request.body.decode())
        user_id = message_data["message_id"]
        text_message = message_data["text_message"]
        status = message_data["success"]

        query = add_post.Query(user_id, text_message, status)
        query.update()

        return HttpResponse(f"{user_id} {status}")
