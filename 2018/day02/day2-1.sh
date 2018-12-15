#!/bin/bash

CNT2=0
CNT3=0
while read line; do
    #echo $line
    RESULT=$(echo $line | grep -o . | sort | uniq -c)
    echo $RESULT | grep 2 2>&1 >/dev/null && CNT2=$(( CNT2 + 1 ))
    echo $RESULT | grep 3 2>&1 >/dev/null && CNT3=$(( CNT3 + 1 ))
done < input.txt
echo $CNT2
echo $CNT3
echo $(( CNT2 * CNT3 ))