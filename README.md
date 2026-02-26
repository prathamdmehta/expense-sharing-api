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

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashExpense_Sharing/  ├── expense_sharing/        # Django project (settings, urls, wsgi)  │   ├── settings.py  │   ├── urls.py  │   └── ...  ├── core/                   # Main app with models, views, serializers  │   ├── models.py  │   ├── views.py  │   ├── serializers.py  │   └── ...  ├── manage.py  ├── Dockerfile  ├── docker-compose.yml  └── requirements.txt   `

Getting Started (Docker)
------------------------

Prerequisites
-------------

*   Docker
    
*   Docker Compose
    

1\. Clone the repository
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashgit clone https://github.com/your-username/expense-sharing.git  cd expense-sharing   `

2\. Build and run with Docker
-----------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose up --build   `

This will:

*   Build the API image
    
*   Run database migrations
    
*   Start the Django development server at http://localhost:8000/
    

Creating a Superuser
--------------------

To access the Django admin:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose exec api python manage.py createsuperuser   `

Then open:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   texthttp://localhost:8000/admin/   `

Log in with the username and password you just created.

Useful Commands
---------------

Restart containers:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose restart   `

Stop containers:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose down   `

View logs:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose logs -f   `

Run migrations manually:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashdocker compose exec api python manage.py migrate   `

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
