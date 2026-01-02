import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


load_dotenv()
#Create Flask app 
app = Flask(__name__)
#SQLite database 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "sqlite:///jobs.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#key for flash messsages
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

db=SQLAlchemy(app)

#Application class
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    date_applied = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False)
    notes= db.Column(db.Text(300), nullable=True)

#if __name__ =="__main__":
with app.app_context():
    db.create_all()
   # app.run(debug=True)

#test data- runs ONLY if no existing entries
def test_data():
    if not Application.query.first():
        test_applications = [
            Application(company="Acme Corp", job_title="Software Engineer", date_applied=datetime.strptime("2025-12-01", "%Y-%m-%d").date(), status="applied", notes="Excited about this role."),
            Application(company="Globex Inc", job_title="Backend Developer", date_applied=datetime.strptime("2025-11-20", "%Y-%m-%d").date(), status="interview", notes="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            Application(company="Initech", job_title="Full Stack Engineer", date_applied=datetime.strptime("2025-11-11", "%Y-%m-%d").date(), status="offer", notes="Offer received, reviewing."),
            Application(company="Umbrella Corp", job_title="Data Scientist", date_applied=datetime.strptime("2025-12-01", "%Y-%m-%d").date(), status="rejected", notes="Rejection email recd. 10/12/2025."),
            Application(company="Hooli", job_title="DevOps Engineer", date_applied=datetime.strptime("2025-11-05", "%Y-%m-%d").date(), status="applied", notes="Looking forward to hearing back."),
            Application(company="Stark Industries", job_title="Frontend Developer", date_applied=datetime.strptime("2025-11-10", "%Y-%m-%d").date(), status="interview", notes="First interview completed."),
            Application(company="Wayne Enterprises", job_title="Software Architect", date_applied=datetime.strptime("2025-12-10", "%Y-%m-%d").date(), status="applied", notes="Batman works here. What more do you need?"),
            Application(company="Oscorp", job_title="QA Engineer", date_applied=datetime.strptime("2025-11-18", "%Y-%m-%d").date(), status="offer", notes="Offer accepted!"),
            Application(company="Wonka Industries", job_title="Product Manager", date_applied=datetime.strptime("2025-10-01", "%Y-%m-%d").date(), status="applied", notes="Excited about innovative projects and potential for long-term growth within the company."),
            Application(company="Tyrell Corp", job_title="AI Specialist", date_applied=datetime.strptime("2025-10-05", "%Y-%m-%d").date(), status="interview", notes="Second interview scheduled."),
        ]
        db.session.add_all(test_applications)
        db.session.commit()

with app.app_context():
    test_data()




#home route 
@app.route("/", methods= ["GET", "POST"])
def home():

    #Add data from job application form to SQL
    if request.method=="POST":
        company = request.form.get("company")
        job_title= request.form.get("jobTitle")
        date_str = request.form.get("dateApplied")
        status = request.form.get("status")
        notes = request.form.get("notes")

        if date_str:
            date_applied = datetime.strptime(date_str, "%Y-%m-%d").date()
        else: 
            date_applied= None

        new_application = Application(
            company=company,
            job_title=job_title,
            date_applied = date_applied,
            status=status,
            notes=notes
        )

        db.session.add(new_application)
        db.session.commit()

        flash("Application saved", "success")
        return redirect("/")
    
    #Filter by key word or status 
    query = Application.query
    search_term = request.args.get("q", "").strip()
    filter_status = request.args.get("status_filter", "").strip()

    if search_term:
        query = query.filter(
            (Application.company.ilike(f"%{search_term}%")) |
            (Application.job_title.ilike(f"%{search_term}%"))
        )
    
    if filter_status:
        query = query.filter_by(status=filter_status)

    applications = query.order_by(Application.date_applied.desc()).all()
    return render_template('index.html', applications=applications)


#delete application card
@app.route('/delete/<int:app_id>', methods=["POST"])
def delete_app(app_id):
    app_to_delete = Application.query.get_or_404(app_id)
    db.session.delete(app_to_delete)
    db.session.commit()
    flash("Application deleted", "danger")
    return redirect('/')

#update job application status
@app.route('/update/<int:app_id>', methods=["POST"])
def update_status(app_id):
    status_update = Application.query.get_or_404(app_id)
    status_update.status = request.form.get("status")
    db.session.commit()
    flash("Status updated", "info")
    return redirect("/")