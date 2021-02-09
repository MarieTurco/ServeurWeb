from webtest import TestApp as make_app
from server import app

app.catchall = False

testapp = make_app(app)

def test_1():
    index = testapp.get("/")
    assert "Bonjour" in index.ubody


def test_double():
    formulaire = testapp.get("/doubler")
    form = formulaire.form
    form["valeur"] = "32"
    res = form.submit()
    assert "64" in res.ubody  


#Tests json

def test_double_json():
    reponse = testapp.post_json("/doubler.json", {"valeur": 43} )

    assert reponse.json["double"] == 86