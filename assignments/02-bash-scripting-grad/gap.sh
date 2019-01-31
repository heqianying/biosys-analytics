#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do 
  DIR="$( cd -P "$( biosys-analytics/data/gapminder "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" 
done
DIR="$( cd -P "$( biosys-analytics/data/gapminder "$SOURCE" )" >/dev/null 2>&1 && pwd )"
find "$DIR" -type f -iname '[a-z]*' > "$FILES"

while read -r FILENAME; do
BASENAME=$(basename "$FILENAME")
printf "%3d: %s\n" $i "$FILENAME"
done < "$FILES"

if [[ ! $FILES -lt 1 ]]; then
echo "There are no countries starting with "$FILES""
exit 1
fi
