

num=$1

# TODO: check num is a number and >= 2
# TODO: check num of command line args

# TODO: special case for 2

i=2

while [ $i -lt $num ]; do
    #  check divisor

    if [ $(( num % i)) -eq 0 ]; then
        echo "$num is not prime"
        exit 1
    fi

    i=$((i + 1))
done

echo "$num is prime"
exit 0
