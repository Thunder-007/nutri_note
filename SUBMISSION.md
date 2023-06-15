# How to run?

Clone the repo and navigate to the project directory.Then run the following commands.

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Edit the database environment variables (Refer the env.example file) finally run the following command.

```bash
python manage.py runserver
``` 

The api is hosted at https://nutrinote.azurewebsites.net/ as docker container uses postgres sql.
The documentation is being done, suggestions and criticism are encouraged.
Please email harsha@harsha07.tech to get the access for the docker instance and database vm on azure. I will create a
azure role for the mail id. 

