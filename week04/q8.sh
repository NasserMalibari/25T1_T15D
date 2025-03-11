

while read zid; do
    ./q7.sh $zid
    # acc "$zid" | 
    # tr ',' '\n' | 
    # grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' | 
    # sed -E  's/.*([A-Z]{4}[0-9]{4}).*/\1/'
    # echo "zid is $zid"
done < zids | sort | uniq -c | sort -n -f1