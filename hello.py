from flask import Flask

app = Flask(__name__)  # default line necessary to run flask applications in a "nice way"

@app.route("/")  # home/main page or root path
def hello_world():
    return "<p>Hello, World!</p>"

# pip freeze > requirements.txt - list all installed packages and write into requirements.txt
# pip install .\requirements.txt - install all the packages required for application according to the requirements.txt file

# cannot run with just python, need to use flask command to run applications
# flask --app hello run - runs application on development server on http://127.0.0.1:5000 - local address/host used by developers
# flask run --host=0.0.0.0 - runs on externally visible server and listen to all public IPs
# flask run - can also run a debug mode

if __name__ == '__main__':  # lets you run with python or vs play button
    # app.run(debug=True)  - not using this with the app.run command below, otherwise external users can see debugging info
    app.run(host='0.0.0.0', port=80)  # sets host to any host (listens to all IPs) and change port to 80 (http/default port for web apps)
    # same as flask run --host=0.0.0.0 --port=80 in terminal
