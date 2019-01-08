#!/bin/bash 
aws lambda invoke --function-name study_chat out.txt
printf "~~~~~~~~Output~~~~~~~~\n"
cat out.txt
printf "\n"
rm out.txt
