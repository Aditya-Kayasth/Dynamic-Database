from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "type": "Full-time"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Bengaluru, India",
    "Salary": "Rs. 12,00,000",
    "type": "Full-time"
}, {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Bengaluru, India",
    "Salary": "Rs. 9,00,000",
    "type": "Contract"
}, {
    "id": 4,
    "title": "Backend Engineer",
    "location": "Bengaluru, India",
    "Salary": "Rs. 10,50,000",
    "type": "Full-time"
}, {
    "id": 5,
    "title": "UI/UX Designer",
    "location": "Mumbai, India",
    "Salary": "Rs. 8,00,000",
    "type": "Part-time"
}, {
    "id": 6,
    "title": "Full Stack Developer",
    "location": "Pune, India",
    "Salary": "Rs. 11,00,000",
    "type": "Full-time"
}, {
    "id": 7,
    "title": "Machine Learning Engineer",
    "location": "Chennai, India",
    "Salary": "Rs. 13,00,000",
    "type": "Full-time"
}, {
    "id": 8,
    "title": "Cloud Engineer",
    "location": "Hyderabad, India",
    "Salary": "Rs. 11,50,000",
    "type": "Part-time"
}, {
    "id": 9,
    "title": "Product Manager",
    "location": "Delhi, India",
    "Salary": "Rs. 14,00,000",
    "type": "Contract"
}, {
    "id": 10,
    "title": "Marketing Specialist",
    "location": "Mumbai, India",
    "Salary": "Rs. 7,50,000",
    "type": "Part-time"
}]


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
