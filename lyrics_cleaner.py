# This script is used to clean up lyrics text files, removing data artifacts that can hurt model training
import re

# Load lyrics file
file_name = input("Specify file name: ")

try:
    file = open(f"./Lyrics/{file_name}.txt", "r", encoding="utf-8")
except:
    print(f"Could not open the requested file: {file_name}")

# Initialize new text file where cleaned lyrics will be written
file_cleaned = open(f"./Lyrics/{file_name}_cleaned.txt", "x", encoding="utf-8")

for line in file:
    # Remove line that contains song title
    if 'Lyrics' in line:
        line = ''

    # Remove 'Embed' or '##Embed' artifact that is written at end of song through Genius API
    elif 'Embed' in line:
        line = re.sub("[0-9]*Embed",'', line)
        
    # Write line to cleaned lyrics file
    file_cleaned.write(line)
print(f"Lyrics were cleaned and written to {file_name}_cleaned.txt")