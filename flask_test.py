from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    var=f'Hello World'
    return render_template('index.html',var=var)

@app.route("/<string:name>")
def erro(name):
    var=f"Pagina ({name}) não encontrada"
    return render_template('error.html',var=var)

if __name__ == "__main__":
    app.run(debug=True)