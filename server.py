from bottle import Bottle, run
import numpy as np

app = Bottle()

@app.route('/')
def bonjour():
    return "Bonjour !"
    

from bottle import template, request

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

#Formulaire 1

@app.get("/formulaire")
def afficher_formulaire():
    return """
        <form action="/formulaire" method="post">
            Texte1 <input name="parametre1" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """


@app.post("/formulaire")
def traiter_formulaire():
    valeur = request.forms.get("parametre1")
    return valeur

#Formulaire 2 rr

@app.get("/formulaire2")
def afficher_formulaire2():
    return """
        <form action="/formulaire2" method="post">
            Liste1 <input name="parametre2" type="text"
            sep=";" />
        <br/>
            Fonction <input name="fname" type="text"/>
            <br/><input value="Ajouter" type="submit" />
        </form>
    """


@app.post("/formulaire2")
def traiter_formulaire2():
    valeur = request.forms.get("parametre2")
    valeur = valeur.split(';')
    valeur2=[float(v) for v in valeur]
    print(valeur2)
      
    fname=request.forms.get("fname")  #fname="somme"
    dic= {'somme': sum, "moyenne": np.mean}
    f=dic[fname]
    return [str(valeur2),"""<br/><br/>""",str(f(valeur2))]


#Tests

@app.get("/doubler")
def calcul():
    return """
     <form action="/doubler" method="post">
            valeur <input name="valeur" type="text" />
        <input value="Ajouter" type="submit" />
        </form>
    """


@app.post("/doubler")
def doubler_valeur():
    data = request.forms
    valeur = int(data.get("valeur"))
    double = valeur * 2
    res = {"valeur": valeur, "double": double}
    #import ipdb; ipdb.set_trace()
    return template("{{valeur}} * 2 = <br/> {{double}}", valeur=valeur, double=double)


# Tests json

@app.post('/doubler.json')
def doubler_valeur_json():
    data = request.json 
    valeur = int(data.get("valeur"))
    res = {'double': valeur*2}
    return res
  
