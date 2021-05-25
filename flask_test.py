from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/olamundo")
def hello_world():
    var=f'Hello World'
    return render_template('index.html',var=var)

@app.route("/", methods=["GET","POST"])
def the_game():
    var = "Game: Adivinhe o número"
    if request.method=="GET":
        return render_template('game.html',var=var)
    else:
        num = randint(1,20)
        palpite = int(request.form.get("name"))
        return f"<h1>Você ganhou! {num}</h1>" if num==palpite else f"<h1>Você perdeu! {num}</h1>"

@app.route("/<string:name>")
def erro(name):
    var=f"Pagina ({name}) não encontrada"
    return render_template('error.html',var=var)

if __name__ == "__main__":
    app.run(debug=True)