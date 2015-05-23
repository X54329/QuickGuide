#!/bin/bash
while read line
do
    strarray=($line)
    echo
    echo
    echo $line
    echo -----------------------------------------------------------------------------------------------
    echo 
    echo 
    python extractText.py "${strarray[0]}"
done < tests

