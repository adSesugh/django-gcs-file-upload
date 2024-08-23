# Google Cloud Storage and Django
This project is tutorial on how to upload files from django app to google cloud storage

### Tech stack
- Django
- Django Rest Framework
- Google-cloud-storage package

### Usage
- Clone the repo
- Create virtual environment probably in the root folder of the cloned project and activate it
- Run the below command to install all dependencies
```bash
    pip install -r requirements.txt
```
- Copy .env.example into .env file and replace the environment variables with appropriate values
- Go to google console and create a service account giving the right to write to the required bucket
- Download the service account in json format 
- Rename it to credentials.json and place in the root directory of your project.
- Run the below command to migrate models to database, 
```bash
python manage.py migrate
```
- Finally, run the project... see command below
```bash
python manage.py runserver
```