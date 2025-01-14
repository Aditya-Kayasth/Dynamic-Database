from flask import Flask, render_template, jsonify
from database import result_dicts
app = Flask(__name__)


@app.route('/jobs')
def list_jobs():
  return jsonify(result_dicts)


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=result_dicts)



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
