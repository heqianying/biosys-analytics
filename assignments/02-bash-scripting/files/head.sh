#!/usr/bin/env bash
FILE=$1
NUM_LINES=$2
if [[ $# -eq 0 ]]; then
echo " Usage: head.sh FILE_NUMM_LINES"
exit 1


elif [[ ! -f "$FILE" ]]; then
echo "$FILE is not a file"
exit 1

elif [[ ! -f "$FILE"_"$NUM_LINES" ]]; then
echo " $FILE IS MISSING NUM_LINES "
exit 2

elif [[ -f "$FILE"_"$NUM_LINES" ]]; then
i=0
for i in $(seq 1 "$NUM_LINES"); do
i=$((i+1))
echo $i $LINE
done < $FILE_$NUM_LINES
exit 0
fi
