
end=$1
i=2

while [ "$i" -lt "$end" ]; do

    # if looks at the exit status, 0 == true, non-zero == false
    if ./is_prime.sh "$i" > /dev/null
    then
        echo "$i"
    fi

    i=$(( i + 1))
done
