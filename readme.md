# Setup Environment

## Debug environment 
Python version: 3.10.13

    git clone https://github.com/nicholasgower/seattlecontratunes.git

    cd seattlecontratunes/seattlecontratunes

    pip install --no-cache-dir -r requirements.txt

    python manage.py makemigrations

    python manage.py migrate

    python manage.py create superuser

    python manage.py runserver

## Running Production Server with Docker

The included Docker image is the recommended method of running this server in production.

    sudo bash build.sh





## .env

"DEBUG"

"DJANGO_ALLOWED_HOSTS"

"INTERNAL_IPS"

"TIME_ZONE"





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

# License

Copyright © 2024 Nicholas Gower

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details. 
