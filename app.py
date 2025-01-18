from flask import Flask, render_template, jsonify, request
from database import jobs_dict, load_job_from_db, add_application_to_db

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
    loaded_job = load_job_from_db(int(id))
    return render_template("job.html", job=loaded_job)

@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):

    data = load_job_from_db(int(id)) #for ID and JOB Tile
    form_data = request.form

    add_application_to_db(data,form_data) # Give it to database

    return render_template("acknowledgement.html", user_form = form_data,data = data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
