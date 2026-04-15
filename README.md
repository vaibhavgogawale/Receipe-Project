🍽️ Recipe Web Application (Django)
📌 Overview

This is a Django-based web application that allows users to explore, share, and interact with recipes. 
The application includes features like tagging, comments, email sharing, and similar recipe recommendations.

🚀 Features:
📖 View list of recipes
🔍 Filter recipes by tags
💬 Add comments on recipes
📧 Share recipes via email
🔗 SEO-friendly URLs
🔁 Similar recipe recommendations

🛠️ Tech Stack:
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Libraries: django Crispy_form

⚙️ Installation:
Clone the repository:
git clone https://github.com/vaibhavgogawale/Receipe-Project.git
cd Receipe-Project
Create virtual environment:
python -m venv env
env\Scripts\activate   # Windows

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py makemigrations
python manage.py migrate

Run server:
python manage.py runserver
