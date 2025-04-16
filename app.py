from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL config
db = mysql.connector.connect(
    host="restaurantdb-1.cl068gesmg67.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Abhv2468",
    database="restaurant_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']

        query = "INSERT INTO reservations (name, email, date, time, guests) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, date, time, guests)
        cursor.execute(query, values)
        db.commit()

        return redirect('/')
    return render_template('reservation.html')

if __name__ == '__main__':
    app.run(debug=True)
