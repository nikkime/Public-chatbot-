from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    bmi = None
    category = ""
    score = 0
    suggestions = []

    if request.method == 'POST':
        height_cm = float(request.form['height'])
        weight = float(request.form['weight'])
        sleep = float(request.form['sleep'])
        water = float(request.form['water'])

        # ✅ FIX: cm → meters
        height_m = height_cm / 100

        # ✅ BMI
        bmi = round(weight / (height_m ** 2), 2)

        # ✅ Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # ✅ Lifestyle Score
        if sleep >= 7:
            score += 20
        elif sleep >= 5:
            score += 10

        if water >= 8:
            score += 20
        elif water >= 5:
            score += 10

        # ✅ Suggestions
        if category == "Underweight":
            suggestions.append("Increase calorie intake (milk, nuts, rice).")
            suggestions.append("Do strength training.")
        elif category == "Normal":
            suggestions.append("Maintain balanced diet.")
        elif category == "Overweight":
            suggestions.append("Reduce sugar & junk food.")
            suggestions.append("Do cardio exercises.")
        else:
            suggestions.append("Strict diet & regular workout.")
            suggestions.append("Consult doctor if needed.")

        if sleep < 7:
            suggestions.append("Sleep at least 7–8 hours.")

        if water < 8:
            suggestions.append("Drink at least 8 glasses of water.")

    return render_template('chatbot.html',
                           bmi=bmi,
                           category=category,
                           score=score,
                           suggestions=suggestions)


if __name__ == '__main__':
    app.run(debug=True)