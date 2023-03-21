from flask import Flask,render_template,request
app = Flask(__name__)
def IMC():
    alt=int(request.form["al"])/100
    peso=float(request.form["kg"])
    return peso/(alt**2)


@app.route('/', methods=['GET'])
def tour():
  return render_template("info.html")

@app.route('/login', methods=['POST'])
def login():
    imc=IMC()
    come=""
    if imc>25:
        come="sovrappeso"
        immage="../../static/images/sovrappeso.jpg"
    elif imc<24.9 and imc>18.5 :
        come="normopeso"
        immage="../../static/images/normo.jpg"
    elif imc<18.5:
        come="sottopeso"
        immage="../../static/images/sotto.jpg" 
    return render_template("login.html",IMC=imc,testo=come,immagine=immage)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  
  