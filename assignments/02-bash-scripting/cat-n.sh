#!/usr/bin/env bash
FILE=$1
if [[ $# -eq 0 ]]; then 
echo "Usage: cat-n.sh FILE"
exit 1 

elif [[ ! -f "$FILE" ]]; then 
echo "$FILE is not a file" 
exit 1 

elif [[ -f $FILE ]]; then
i=0
while read -r LINE; do
i=$((i+1))
echo "$i $LINE"
done < "$FILE"
exit 0
fi


