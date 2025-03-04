#!/usr/bin/dash
start=1
inc=1
end=10
## process command line args
if test $# -eq 1; then
    end=$1
elif test $# -eq 2; then
    start="$1"
    end="$2"
elif [ "$#" -eq 3 ]; then
    start="$1"
    inc="$2"
    end="$3"
else
    echo "wrong num of args"
    exit 1
fi


if [ "$end" -eq "$end" ] 2> /dev/null; then
    echo "end is a number"
else
    echo "end is not a number !"
    exit 1
fi


i="$start"

while test $i -le $end ; do
    echo "$i"

    i=$((i + inc))
done
