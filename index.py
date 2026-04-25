import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request

app = Flask(__name__)

# --- CARGAR EL MODELO TFLITE ---
def predict_fahrenheit(celsius_value):
    interpreter = tf.lite.Interpreter(model_path="model_c2f.tflite")
    interpreter.allocate_tensors()
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # Preparar el dato de entrada
    input_data = np.array([[celsius_value]], dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    # Ejecutar la predicción
    interpreter.invoke()
    
    # Obtener el resultado
    prediction = interpreter.get_tensor(output_details[0]['index'])
    return float(prediction[0][0])

@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    if usuario == "admin" and clave == "1234":
        # Al loguearse, redirigimos a una nueva página de predicción
        return render_template("predict.html")
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

@app.route("/predict", methods=["POST"])
def predict():
    celsius = request.form.get("celsius")
    if celsius:
        resultado = predict_fahrenheit(float(celsius))
        return render_template("predict.html", resultado=f"{celsius}°C son aproximadamente {resultado:.2f}°F")
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)