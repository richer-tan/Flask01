from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/products')
def products():
    return '<h1>Product Page</h1>'

@app.route('/products/<string:id>')
def product_detail(id):
    return f'<h1>Product ID#{id} Details</h1>'

@app.route('/example')
def example():
    return render_template('index.html')



if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80)


