#build.ps1
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

docker swarm init --advertise-addr 127.0.0.1


docker compose up --build
#docker service create --secret="DJANGO_SECRET_KEY" 