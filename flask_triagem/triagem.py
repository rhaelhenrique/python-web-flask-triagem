from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__== "__main__":
    app.run(debug=True)
    
    
a = 2
b = 3

c = a + b