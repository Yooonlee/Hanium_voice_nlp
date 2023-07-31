import os
import json


# Replace with your directory path
directory_path = "C:/Users/USER/Desktop/stt - 복사본 - 복사본/"
out_file_path = directory_path + "결과/phishing_Data.json"

data = []
index = 1

# Loop over all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        dict = {}
        dict['text'] = []
        dict['index'] = None

        with open(directory_path + filename, 'r', encoding='UTF-8') as file:
            # Read all lines in the file
            content = file.readlines()
            content = [line.strip() for line in content]

            for text in content:
                if text == '':
                    if dict['text']:
                        dict['index'] = index
                        data.append(dict.copy())
                        index += 1
                        dict['text'] = []
                    continue
                elif '피해자' in text or '사기범' in text:
                    dict['text'].append(text)

        # Process the last file's result
        if dict['text']:
            dict['index'] = index
            data.append(dict.copy())
            index += 1

# Save the result as a JSON file
with open(out_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
