from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route('/quiz', methods=["GET"])
def quiz(): 
    course = request.args.get('cour')
    return render_template("quiz.html", course = course) 

if __name__=='__main__':
    app.run(debug=True)

