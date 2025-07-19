Jainik's Blog - A Simple Flask Web Application
A clean, dynamic, and fully functional blog application built with Python and the Flask web framework. This project serves as an excellent starting point for learning the fundamentals of back-end web development, database management, and HTML templating.

Core Features
This application has full CRUD (Create, Read, Update, Delete) functionality for blog posts:

Create: Add new blog posts via a user-friendly web form.
Read: View all blog posts on the home page, sorted chronologically.
Update: Edit existing posts to correct typos or add new information.
Delete: Permanently remove posts from the blog.
User Feedback: Displays flash messages to confirm successful actions (e.g., "Post created successfully!").

Tech Stack
Backend: Python
Web Framework: Flask
Database: SQLite with Flask-SQLAlchemy (an Object-Relational Mapper)
Frontend: HTML5 with Jinja2 templating
Styling: Custom CSS

Setup and Installation
To get this project running on your local machine, follow these steps.

1. Prerequisites
Python 3.x
pip (Python's package installer)

2. Clone the Repository
If you are using Git, clone the repository. Otherwise, ensure all the project files are in a single folder.

git clone <your-repository-url>
cd <project-folder-name>

3. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.

# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

4. Install Dependencies
This project's dependencies are listed in requirements.txt. Install them with pip.

pip install -r requirements.txt

Note: If you don't have a requirements.txt file yet, you can create one by running this command in your activated virtual environment: pip freeze > requirements.txt

5. Initialize the Database
The first time you run the project, you need to create the blog.db database file and its tables.

# Open the special Flask shell
python -m flask shell

# Inside the shell, run these commands
>>> from app import db
>>> db.create_all()
>>> exit()

How to Run the Application
Once the setup is complete, you can start the Flask development server with this simple command:

python app.py

Now, open your web browser and navigate to https://www.google.com/search?q=http://127.0.0.1:5000 to see your blog in action!

Future Enhancements
This project has a solid foundation. Here are some ideas for future development:

User Authentication: Add user registration and login functionality so different authors can manage their own posts.

Comments Section: Allow readers to leave comments on individual posts.

Individual Post Pages: Create unique URLs and pages for each blog post.

Search Functionality: Implement a search bar to find posts by title or content.

Pagination: If the blog has many posts, add "Next" and "Previous" page buttons to navigate them.