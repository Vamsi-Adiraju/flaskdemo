from flask import Flask,render_template

app = Flask(__name__)
JOBS=[{
  'id':1,
  'title':'Data Analyst',
  'location':'Bangalore, India',
  'salary' :'Rs. 10,00,000'
}, 
{
  'id':2,
  'title':'Data Scientist',
  'location':'Hyderabad, India',
  'salary' :'Rs. 15,00,000'
},
{
  'id':1,
  'title':'Business Analyst',
  'location':'Pune, India',
  'salary' :'Rs. 8,00,000'
},
{
  'id':1,
  'title':'Full Stack Developer',
  'location':'San Fansisco, USA',
  'salary' :'$170,000'
}
 ]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)

if __name__== "__main__":
  app.run(host='0.0.0.0',debug=True)