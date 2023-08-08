# Import flask module
# from flask import Flask
 
# app = Flask(__name__)
 
# @app.route('/')
# def index():
#     return 'Hello to Flask!'
 
# # main driver function
# if __name__ == "__main__":
#     app.run()
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>This is a Hello World my python</p>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)