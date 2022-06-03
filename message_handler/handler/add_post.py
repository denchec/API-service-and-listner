from psycopg2 import Error
import psycopg2


class Query:
    def __init__(self, user_id, message, status="на проверке"):
        self.user_id = user_id
        self.message = message
        self.status = status

    def insert(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1234",
                                          host="localhost",
                                          port="5432",
                                          database="MessageDB")

            cursor = connection.cursor()

            insert_query = "INSERT INTO message_table (user_id, message, status) VALUES (%s, %s, %s)"
            arguments = (self.user_id, self.message, self.status)
            cursor.execute(insert_query, arguments)
            connection.commit()
            print("Вставили запись")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
            print("Соединение с PostgreSQL закрыто")

    def update(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1234",
                                          host="localhost",
                                          port="5432",
                                          database="MessageDB")

            cursor = connection.cursor()

            update_query = "UPDATE message_table set status = %s where user_id = %s"
            arguments = (self.status, self.user_id)
            cursor.execute(update_query, arguments)
            connection.commit()
            
            print("Запись успешно изменена")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
            print("Соединение с PostgreSQL закрыто")
