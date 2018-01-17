#!/bin/sh

RESULT=0

for var in "$@"
do
    ## will print an extra + at the end.
    ## But I dont care. ;)
    echo -n "$var + "
    RESULT=$(($RESULT+$var))
done

echo " = $RESULT"