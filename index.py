from flask import Flask, current_app
import itertools

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return "<h1> Welcome to the first main page</h1><p>Have a good day</p>"
    return current_app.send_static_file('index.html')



app.run(host='0.0.0.0', port=int("8000"))
