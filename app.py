from flask import Flask, render_template, jsonify
from database import jobs_dict,load_job_from_db
app = Flask(__name__)


@app.route('/jobs')

def list_jobs():
  result_dicts = jobs_dict()
  return jsonify(result_dicts)


@app.route('/')
def hello_world():
  result_dicts = jobs_dict()
  return render_template('home.html', jobs=result_dicts)
  

@app.route('/job/<id>')
def show_job(id):

  loaded_job = load_job_from_db(id)
  return render_template("job.html",job = loaded_job)



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
