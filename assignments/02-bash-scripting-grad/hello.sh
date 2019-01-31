#!/usr/bin/env bash


GREETINGS=$1
NAME=${2:-Human}

if [[ $# -eq 0 ]]; then 
printf "Usage: %s hello.sh GREETING [NAME]\n"
exit 1 

elif [[ $# -gt 2 ]]; then 
echo "Usage: %s hello.sh GREETING [NAME]\n" 
exit 1 


elif [[ $2 -eq 0 ]]; then
echo ""$GREETINGS","$NAME"!"
exit 0

else
echo ""$GREETINGS","$NAME"!"
fi
