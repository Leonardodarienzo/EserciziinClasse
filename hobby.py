#3 scrivere una web app che permetta di slezionare da una lista di checkbox i propri hobby e cliccando su un bottone avere l'elenco degli obbi selezionati  e il numero di essi
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
  return render_template("hobby.html")

@app.route('/login', methods=['POST'])
def login():
  i=True
  hobby=[]
  indicatore=1
  while i==True:#non avviare senza controllare
    try:
      hobby.append(request.form["hobby"+str(indicatore)])
      indicatore +=1
    except:
      i=False
    
  return render_template("login2.html",numero=len(hobby),testo=hobby)

 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)