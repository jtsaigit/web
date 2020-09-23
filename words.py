from flask import request, jsonify, Flask
import itertools

app = Flask(__name__)
app.config["DEBUG"] = True

user = ""

@app.route('/')
def home():
    return "<h1> Welcome to Anagrams World</h1><p>Enter your </p>

@app.route('/data')
def data():
    # Get the value of userInput (i.e. ?userInput=some-value)
    userInput = request.args.get('userInput').strip()

    # Validate user input to check if it is a word (no numbers or special characters)
    if userInput.isalpha():
        list1 = ["".join(perm) for perm in itertools.permutations(userInput)]
        return ' '.join(list1)
    else:
        return "This is not a word, please try again!"

app.run(host='0.0.0.0', port=int("80"))
