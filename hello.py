from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/products')
def products():
    return '<h1>Product Page</h1>'

@app.route('/products/<string:id>')
def product_detail(id):
    return f'<h1>Product #{id} Details</h1>'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80)


