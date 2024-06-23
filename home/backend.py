# myproject/myapp/backend.py
import mysql.connector # type: ignore

class MySQLAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            cnx = mysql.connector.connect(
                user='your_username',
                password='your_password',
                host='your_host',
                database='your_database'
            )
            cursor = cnx.cursor()
            query = "SELECT * FROM your_table WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            if user:
                return user
            else:
                return None
        except mysql.connector.Error as err:
            print(err)
            return None

    def get_user(self, user_id):
        try:
            cnx = mysql.connector.connect(
                user='your_username',
                password='your_password',
                host='your_host',
                database='your_database'
            )
            cursor = cnx.cursor()
            query = "SELECT * FROM your_table WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            if user:
                return user
            else:
                return None
        except mysql.connector.Error as err:
            print(err)
            return None