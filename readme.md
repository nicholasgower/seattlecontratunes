# Setup Environment

Python version: 3.10.13

    git clone https://github.com/nicholasgower/seattlecontratunes.git

    cd seattlecontratunes/seattlecontratunes

    pip install --no-cache-dir -r requirements.txt

    python manage.py makemigrations

    python manage.py migrate

    python manage.py create superuser

    python manage.py runserver

## .env

"DEBUG"

"DJANGO_ALLOWED_HOSTS"

"INTERNAL_IPS"

"TIME_ZONE"

More soon, when database is changed to Postgres



## Secrets

Define the following system environment variables. In development, define them in your system's environmental variables. In Docker, define them by copying run/secrets_blank to run/secrets, and writing your secrets in their respective text file.

"DJANGO_SECRET_KEY" : The Django secret key

"EMAIL_HOST" : The SMTP email host for the server, to send automated emails. (Example: smtp.gmail.com)

"EMAIL_HOST_USER" : email username

"EMAIL_HOST_PASSWORD" : email password




# Todo:


DMCA Compliance

~~Search bar~~ **Completed 12/24/23** Only searches by name at the moment.

~~Automatic linking from tunes in medleys to tune pages~~ **Completed 12/24/23** Not perfect, but further improvements will likely require an API.

~~Change clef button~~ **Completed 12/21/23**

~~User-directed account creation~~ **Completed 12/26/23**

~~User-uploaded tunes~~ **Completed 12/26/2023**

User-edited tunes

User deletion of tunes uploaded by user (Not literal deletion, only making it hidden from users)
