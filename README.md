# Job Application Tracker

A simple web app to track your job applications. Built with Flask, SQLAlchemy, and Bootstrap. You can add applications, update status, filter by company or status, and expand notes. Designed as a portfolio project to showcase full-stack development skills.

## Features
- Add, update, and delete job applications
- Filter applications by company, job title, or status
- Expand/collapse long notes
- Responsive layout for desktop and mobile
- Flash messages for actions (save, update, delete)

## Setup & Installation
1. Clone the repository:
   git clone https://github.com/yourusername/job-app-tracker.git
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

## Technologies Used
- Python 3.14
- Flask
- Flask-SQLAlchemy
- Bootstrap 5
- SQLite
- HTML/CSS/JS

## Author
Mae Rischer
