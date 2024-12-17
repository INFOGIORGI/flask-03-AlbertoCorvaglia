from flask import Flask, render_template

app = Flask(__name__)

prodotti = (("Tavolo","1","5"),("Sedia","1","15"),("PC","2","50"))

@app.route("/")
def home():
    return render_template("index.html",titolo="HomePage")

@app.route("/details")
def details():
    return render_template("details.html",titolo="Details",prodotti=prodotti)

@app.route("/dettagliprodotto/<scaffale>")
def dettagliprodotto(scaffale):
    listaProdotti = []
    print(scaffale)
    for p in prodotti:
        if(p[1]==scaffale):
            listaProdotti.append(p)
    return render_template("dettagliprodotto.html",prodotti=listaProdotti)

app.run(debug=True)
