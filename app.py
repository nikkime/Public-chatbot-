from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login ❌"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    bmi = None
    status = None
    score = None
    suggestion = ""

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100

        diet = int(request.form["diet"])
        exercise = int(request.form["exercise"])
        sleep = int(request.form["sleep"])
        water = int(request.form["water"])

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        score = diet + exercise + sleep + water

        if score < 50:
            suggestion = "Improve your lifestyle"
        elif score < 80:
            suggestion = "Good but can improve"
        else:
            suggestion = "Excellent lifestyle!"

    return render_template("dashboard.html",
                           bmi=bmi,
                           status=status,
                           score=score,
                           suggestion=suggestion)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)