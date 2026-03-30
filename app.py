from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['user'] = username
        return redirect(url_for('chatbot'))
    return render_template('login.html')

# Chatbot Page
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    bmi = None
    suggestion = ""
    lifestyle_score = None

    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        sleep = int(request.form['sleep'])
        water = int(request.form['water'])

        bmi = weight / (height ** 2)

        # Lifestyle Score (simple logic)
        lifestyle_score = (sleep * 5) + (water * 2)

        if bmi < 18.5:
            suggestion = "You are underweight. Improve diet."
        elif bmi < 25:
            suggestion = "You are healthy. Maintain lifestyle."
        else:
            suggestion = "You are overweight. Exercise more."

    return render_template(
        'chatbot.html',
        bmi=bmi,
        suggestion=suggestion,
        lifestyle_score=lifestyle_score
    )

if __name__ == '__main__':
    app.run(debug=True)