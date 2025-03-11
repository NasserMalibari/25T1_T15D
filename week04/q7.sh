

if [ $# -ne 1 ]; then
    echo "usage: ./q7.sh <zid>"
    exit 1
fi

acc "$1" | 
tr ',' '\n' | 
grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' | 
sed -E  's/.*([A-Z]{4}[0-9]{4}).*/\1/'
