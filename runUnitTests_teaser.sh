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
    python extractText_teaser.py $line
done < tests

