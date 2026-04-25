from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    
    # Usuario y clave de prueba
    if usuario == "admin" and clave == "1234":
        return f"<h1>Bienvenido, {usuario}</h1><p>Acceso correcto.</p>"
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

if __name__ == "__main__":
    app.run(debug=True)