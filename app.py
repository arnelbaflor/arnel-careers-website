from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Survey Programmer',
    'location': 'Cebu, PH',
    'salary': 'Php 1,000,000'
  },
  {
    'id': 2,
    'title': 'Data Processor',
    'location': 'Davao, PH'
  },
  {
    'id': 3,
    'title': 'Project Manager',
    'location': 'Remote',
    'salary': 'Php 10,000,000'
  },
  {
    'id': 4,
    'title': 'QA Tester',
    'location': 'Manila, PH',
    'salary': 'Php 100,000'
  }
  
]

@app.route("/")
def hello_arnel():
    return render_template('home.html',
                          jobs=JOBS,
                          company_name="Arnel")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)