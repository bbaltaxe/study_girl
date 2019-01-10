#!/bin/bash

#update lambda
zip study_chat.zip main.py
aws lambda update-function-code --function-name="study_chat" --zip-file="fileb:///Users/breanna/Documents/Research/study_girl/study_chat.zip" || exit 1
rm study_chat.zip

#push to git
#git add .
#git commit
#git push


