from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the Customer, Order, and Transaction classes
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Order(Customer):
    def __init__(self, name, customer_id, order_id, item_name):
        super().__init__(name, customer_id)
        self.order_id = order_id
        self.item_name = item_name

class Transaction(Order):
    def __init__(self, name, customer_id, order_id, item_name, transaction_id, date, time):
        super().__init__(name, customer_id, order_id, item_name)
        self.transaction_id = transaction_id
        self.date = date
        self.time = time

# In-memory storage for transactions
transactions = []

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

        # Create a new transaction object
        transaction = Transaction(name, customer_id, order_id, item_name, transaction_id, date, time)

        # Store the transaction in the list
        transactions.append(transaction)

        # Redirect to the same page after form submission
        return redirect(url_for('index'))

    # Render the page with the form and display all transactions
    return render_template('index.html', transactions=transactions)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
