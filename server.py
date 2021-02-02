from bottle import Bottle, run

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
            Liste2 <input name="parametre2" type="text"/>
            <br/><input value="Ajouter" type="submit" />
        </form>
    """


@app.post("/formulaire2")
def traiter_formulaire2():
    valeur = request.forms.get("parametre2")
    valeur = valeur.split(';')
    valeur2=[float(v) for v in valeur]
    print(valeur2)
    return str(valeur2)