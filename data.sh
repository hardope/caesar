#!/bin/bash

# Replace 'your_file.txt' with your file name
file="/home/ubuntu/caesar/visit.txt"

# Activate your Python virtual environment
source /home/ubuntu/caesar/venv/bin/activate

# Check if the file exists and is empty
if [ -s "$file" ] && [ "$#" -ge 1 ]; then

    python /home/ubuntu/caesar/request.py write
    rm /home/ubuntu/caesar/visit.txt

    # Deactivate the virtual environment
    deactivate
else
    python /home/ubuntu/caesar/request.py read

fi

deactivate
