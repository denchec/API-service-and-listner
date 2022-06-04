Installation environment:
py -3.10 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip

Loading libraries:
pip install -r requirements.txt

Start listener:
1) Enable Kafka service
2) cd listener\
3) python listener.py

Start API-service:
1) Enable Postges service
2) cd message_handler\
3) python manage.py runserver
