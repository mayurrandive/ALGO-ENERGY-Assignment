1. make virtual environment
2. activate environment "source <path to activate file>"
3. copy below into .env file and set up postgres and make db with dbname ( ExpenseTracker )

DB_USERNAME=postgres
DB_NAME=ExpenseTracker
DB_HOST=localhost
DB_PASSWORD=postgres
DB_PORT=5432

4. change directory to backend and install all packages in stored req.txt using "pip install -r req.txt"
5. run backend 
    "python manage.py makemigrations"
    "python manage.py migrate"
    "python manage.py runserver"
6. change directory to frontend (AwesomeProject) and install frontend packages using "npm install"
7. run frontend "npm start"