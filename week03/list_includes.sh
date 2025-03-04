#!/usr/bin/dash

for file in *.c; do

    if [ $file -eq "*.c" ]; then
        echo "no .c files found!"
        exit 1
    fi
    
    echo "$file includes:"
    grep -E '#include' "$file" |
    sed -E 's/^\s*#include\s*[<"]/\t/' |
    sed -E 's/[>"]\s*$//'

    # echo $file
done