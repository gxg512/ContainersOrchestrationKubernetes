from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def test_db_connection():
    try:
        # Replace the placeholders with your MySQL database credentials
        cnx = mysql.connector.connect(user='root', password='abc123',
                                      host='mysql-deploy',database='books')
        print("Connected")
        cnx.close()
    except mysql.connector.Error as err:
        print("Not connected, try again")
        print(err)

    return "Check the console for connection status!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9999)
