from flask import Flask
"""
-Here i have imported the Flask class
-Flask(__name__) is the constructor, which initialise the app.
"""
app = Flask(__name__)
"""
-Here i have added function for homepage operation.
"""
@app.route('/')
def index():
    return "<h1>Demo Flask App</h1>"

"""
-Here i am using route with redirection as a return.
"""
@app.route('/page1')
def google():
    return "<a href='/'>Click here for Homepage</a>'"
"""
-Here i am using route variables
"""
@app.route('/<string:name>')
def welcome(name):
    return f"<h1>Hello {name}, Welcome to Bridgelabz</h1>"

"""
-This main method will run this app with debug=True.
"""
if __name__ == "__main__":
    app.run(debug=True)
