# "Crypto App"

## About ✨

#### Crypto App 
This simple project, where you can to try to interactive with some popular blockchains. The application is built using the Django and Django Rest frameworks, DB is SQLite3. 

## Deployment
- [Live Crypto App](http://18.193.248.158)

## Installation 💻
To run this project, follow these steps:

1. Clone this repository to your local machine;
2. Install the required packages and activate virtual environment,  by running ```poetry install``` after ```poetry shell```
3. Set the required environment variables, you neend to add actual data in /configs;
4. Create DB , add file db.sqlite3 in directory blockchain_test/db.sqlite3
5. Make migrations, by running ```python manage.py migrate```
6. Create superuser, by running ```python manage.py createsuperuser```
7. Start the server by running ```python manage.py runserver```
8. Add data to DB, use ```http://127.0.0.1/admin```
9. Check main app, see ```http://127.0.0.1/```

Or,
You can use docker tools))),
1. Add file db.sqlite3 in directory blockchain_test/db.sqlite3
2. Run ```docker compose up -d```
3. Next repeat steps 6, 8, 9
