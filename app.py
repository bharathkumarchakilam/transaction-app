from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Bharath@2647'
app.config['MYSQL_DB'] = 'transaction_db'

# Initialize MySQL
mysql = MySQL(app)

# Route to display the form and handle input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect data from the form
        name = request.form['name']
        customer_id = request.form['customer_id']
        order_id = request.form['order_id']
        item_name = request.form['item_name']
        transaction_id = request.form['transaction_id']
        date = request.form['date']
        time = request.form['time']

        # Insert data into MySQL database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO transactions (name, customer_id, order_id, item_name, transaction_id, date, time)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                    (name, customer_id, order_id, item_name, transaction_id, date, time))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    # Retrieve all transactions from MySQL database
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM transactions')
    transactions = cur.fetchall()
    cur.close()

    return render_template('index.html', transactions=transactions)

# Route to handle transaction deletion
@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM transactions WHERE transaction_id = %s', (transaction_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
