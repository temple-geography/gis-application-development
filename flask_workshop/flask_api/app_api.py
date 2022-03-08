
#!/usr/bin/env python

from flask import Flask,json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/")
def hello():
    #it is a good idea to include information on how to use your API on the home route
    text = '''go to /all to see all events
              and /year/<year> to see events for a particular year'''
    return render_template('index.html', html_page_text=text)
  
@app.route("/all")
def all():
    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))

    #render_template is always looking in templates folder
    return render_template('index.html',html_page_text=data_json)

@app.route("/year/<year>",methods=['GET', 'POST'])
def add_year(year):
    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))
    data = data_json["events"]
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['events']
        year = request.view_args['year']
        output_data = [x for x in data if x['year']==year]
        
        
        
        #render template is always looking in tempate folder
        return render_template('events.html',html_page_text=output_data)

    
if __name__ == "__main__":
    app.run(debug=True)