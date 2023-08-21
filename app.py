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
app = Flask(__name__,  static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def hello_world():
    return "<p>This is a Hello World my python with Jenkinsfile</p>"

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('password')
        print(email, senha)
        return "OK POST"
    return "OK GET"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)