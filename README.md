Expense Sharing API
===================

A simple **Django REST API** to create groups, add members, track expenses, and calculate how much each person owes or should receive.

This project is containerized with Docker so you can run it locally with a single command.

Features
--------

*   Create expense sharing **groups**
    
*   Add **members** to each group
    
*   Record **expenses** paid by any member
    
*   Automatically compute **balances** (who owes whom)
    
*   Django **admin panel** for managing all data
    
*   Fully **Dockerized** (no need to install Python or Django globally)
    

Tech Stack
----------

*   Python 3.x
    
*   Django
    
*   Django REST Framework
    
*   SQLite (default dev database)
    
*   Docker & Docker Compose
    

Project Structure (simplified)
------------------------------
`
Expense_Sharing/
├── expense_sharing/        # Django project (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/                   # Main app with models, views, serializers
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
`

Getting Started (Docker)
------------------------

Prerequisites
-------------

*   Docker
    
*   Docker Compose
    

1\. Clone the repository
------------------------
`
git clone https://github.com/your-username/expense-sharing.git
cd expense-sharing
`

2\. Build and run with Docker
-----------------------------

`   bashdocker compose up --build   `

This will:

*   Build the API image
    
*   Run database migrations
    
*   Start the Django development server at http://localhost:8000/
    

Creating a Superuser
--------------------

To access the Django admin:

`   bashdocker compose exec api python manage.py createsuperuser   `

Then open:

`   texthttp://localhost:8000/admin/   `

Log in with the username and password you just created.

Useful Commands
---------------

Restart containers:

`   bashdocker compose restart   `

Stop containers:

`   bashdocker compose down   `

View logs:

`   bashdocker compose logs -f   `

Run migrations manually:

`   bashdocker compose exec api python manage.py migrate   `

API Endpoints (examples)
------------------------

Replace or extend based on your actual URLs:

*   GET /api/groups/ – list all groups
    
*   POST /api/groups/ – create a group
    
*   GET /api/groups// – retrieve a specific group
    
*   POST /api/expenses/ – add a new expense
    
*   GET /api/balances// – get who owes whom in a group
    

Environment & Configuration
---------------------------

By default, the project uses SQLite and development settings in expense\_sharing/settings.py.

You can adjust:

*   DEBUG
    
*   ALLOWED\_HOSTS
    
*   Database config
    

for production deployment.

Contributions
-------------

Feel free to:

*   Open issues
    
*   Suggest improvements
    
*   Submit pull requests
    

License
-------

Add your preferred license here (e.g. MIT, Apache 2.0).
