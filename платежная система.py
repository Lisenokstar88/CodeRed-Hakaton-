from flask import Flask, render_template, redirect

from cloudipsp import Api, Checkout


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')





@app.route('/buy/<int:id>')
def item_buy(id):

    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "Rub",
        "amount": str(10) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)



if __name__ == "__main__":
    app.run(debug=True)


