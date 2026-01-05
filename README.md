## 📝 Job Application Tracker

A simple web app to track your job applications. Built with Flask, SQLAlchemy, and Bootstrap. You can add applications, update status, filter by company or status, and expand notes. Designed as a portfolio project to showcase full-stack development skills.


## 🛠️ Tech Stack
Backend: Python (Flask), SQLAlchemy ORM
Database: SQLite (Relational)
Frontend: Jinja2 Templates, Bootstrap 5, Vanilla JavaScript
Deployment: Render (Web Service)

## ✨ Key Features
Full CRUD Integration: Seamlessly add, view, update, and delete application records.
Dynamic Filtering: Search and filter applications by company name, job title, or status.
Relational Data Management: Utilizes SQLAlchemy to handle structured data and persistent storage.
Responsive UI: A mobile-first dashboard featuring expandable notes for interview details. 
User Feedback: Integrated Flask Flash messaging system for real-time action confirmation.

## 🚀 Live demo: 
https://job-app-tracker-75gk.onrender.com
(Note: Hosted on Render's free tier. Please allow 30-60 seconds for the initial spin-up.)

## Setup & Installation
1. Clone the repository:
   git clone https://github.com/ApplePiandIceCream/job_app_tracker.git
   cd job-app-tracker
2. Create a virtual environment:
   python -m venv venv
3. Activate the virtual environment:
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies:
   pip install -r requirements.txt
5. Create a `.env` file in the project root and add:
   SECRET_KEY=your_secret_key_here
   SQLALCHEMY_DATABASE_URI=sqlite:///jobs.db
6. Initialize the database:
   python
   >>> from app import db
   >>> db.create_all()
7. Run the app locally:
   flask run
   - Open http://127.0.0.1:5000/ in your browser

## Deployment
- Push the repository to GitHub
- Deploy on a platform like Render, Railway, or Heroku
- Set the `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI` environment variables on the host
- The database will be created automatically on first run

## Notes
- The "Show more" button for notes expands long notes with minimal JavaScript
- The application cards are color-coded and responsive
- Flash messages confirm actions without interrupting workflow
- All form data is saved in the SQLite database defined in `.env`

## 🧠 Lessons Learned
**ORM Optimization:** Gained experience mapping Python objects to relational database tables using SQLAlchemy.

**Environment Management:** Implemented python-dotenv to securely manage sensitive API keys and database URIs.

**Deployment Pipelines:** Managed the transition from local SQLite development to cloud-based hosting on Render.

## Author
Mae Rischer
