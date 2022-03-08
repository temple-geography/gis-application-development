from flask import Flask, render_template, flash, request


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1><b>Welcome to Casey's Maps</b></h1> <br> Try looking adding /philly or /nyc to the current link</br>"

@app.route('/nyc')
def nyc():
    return render_template('nyc_map.html')

@app.route('/philly')
def philly():
    return render_template('philly_map.html')

if __name__=='__main__':
    app.run(debug=True)

