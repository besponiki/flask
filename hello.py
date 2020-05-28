from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

<<<<<<< HEAD
    return 'Hello'
=======
    return 'Hello'
>>>>>>> task53

if __name__ == '__main__':
    app.run()