#!/bin/bash -i

scriptpath=$(readlink -f "$0")
dir=$(dirname "$scriptpath")
cd "$dir" || exit


python seattlecontratunes/manage.py runserver 