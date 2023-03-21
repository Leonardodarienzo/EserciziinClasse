from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("form.html")
  
@app.route('/login',methods = ['GET'])
def login():
  Username = request.args.get('Username')
  password = request.args.get('password')
  if Username == "admin" and password == "xxx123##":

    return render_template("login.html", Username=Username)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)