#build.ps1
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

docker swarm init --advertise-addr 127.0.0.1


docker compose up --build --detach #Builds docker compose in the background, allowing future lines to run

docker exec seattlecontratunes-web-1 python manage.py makemigrations #Migrate the database, syncing database definitions in models.py with database

docker exec seattlecontratunes-web-1 python manage.py migrate 

docker exec seattlecontratunes-web-1 python manage.py createsuperuser --noinput #Creates default superuser from contents of .env

docker compose down #Shutdown docker compose instance

docker compose up #Rerun docker compose without rebuilding, as all required building is done, and database is up to date with models. I don't know if a restart is necessary, but the cost of doing so is low.