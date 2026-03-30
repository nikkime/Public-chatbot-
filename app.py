from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -------- BMI --------
def calculate_bmi(weight, height):
    bmi = round(weight / (height * height), 2)

    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 25:
        return bmi, "Normal"
    elif bmi < 30:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"

# -------- CHATBOT --------
def chatbot(msg):
    msg = msg.lower()

    if "hello" in msg:
        return "Hi 👋 I'm your Health AI"
    elif "bmi" in msg:
        return "Use the form above to calculate BMI 📊"
    elif "diet" in msg:
        return "Eat healthy 🥗 and drink water 💧"
    else:
        return "Ask about BMI, diet, or health"

# -------- ROUTES --------
@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100
        bmi, category = calculate_bmi(weight, height)

    return render_template("index.html", bmi=bmi, category=category)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"response": chatbot(data["message"])})

app = app
