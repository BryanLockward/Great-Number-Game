from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
    session['num'] = random.randint(1,100)

@app.route('/')
def index():
    try:
        print session['num']
    except:
        setSession()
        print session['num']

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_numb():
    error = None
    success = None
    guess = request.form['guess']
    if request.method == 'POST':
        guess = int(guess)
        if guess == session['num']:
            flash('Correct', 'success')
            return redirect('/')
        elif guess > session['num']:
            flash('Too high, Try Again', 'error')
        else:
            flash('Too low, Try Again', 'error')


    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)
