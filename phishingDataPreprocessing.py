import json
import re
from collections import defaultdict
file_path = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/보이스피싱데이터/"
file1 = "2015-2017 클로바노트.txt"
file2 = "2018(거의다 텍스트로 제공됨)-2020.docx.txt"
file_name1 = file_path + file1
file_name2 = file_path + file2


from typing import List
def PhishingDataPreprocessing1(file_name) -> List:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.split('\n')
    # print(content)
    data = []
    dict = {}
    dict['text'] = []
    dict['index'] = None
    dict['label'] = None
    subtext= ''
    for text in content:
        try:
            if(int(text) in list(range(80))):
                if(subtext):
                    dict['label'] = 1
                    dict['text'] = subtext
                    data.append(dict.copy())
                    # print(data)
                dict['text'] = []
                dict['index'] = None
                dict['label'] = None
                subtext = ''
                index = int(text)
                dict['index'] = index
                # print(dict['index'])
        except:
            text = text.strip()
            if('피해자' in text or '사기범' in text):
                if('피해자' in text):
                    text = text.replace('피해자', ' 피해자: ')
                    # re.sub('피해자', '피해자:', text)
                    subtext += text
                    # dict['text'].append(text)
                elif('사기범'  in text):
                    text = text.replace('사기범', ' 사기범: ')
                    # re.sub('사기꾼', '사기꾼:', text)
                    subtext += text
                    # dict['text'].append(text)
            elif(text == ''):
                continue
            else:
                subtext += text
                # dict['text'].append(text)
    # print(data)
    return data
    
data1 = PhishingDataPreprocessing1(file_name1)        
# print(data1)
out_file_path1 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/phishing_Data_1517_new.json"
# json 형식으로 저장
# ensure_ascii=False : 데이터를 한글로 저장
with open(out_file_path1, 'w', encoding='utf-8') as outfile:
    json.dump(data1, outfile, ensure_ascii=False)

####################################

def PhishingDataPreprocessing2(file_name) -> List:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.split('\n')
    data = []
    dict = {}
    dict['text'] = []
    dict['index'] = None
    dict['label'] = None
    subtext= ''
    index = 1
    for text in content:
        text = text.strip()
        print(text)
        if(text == ''):
            if(subtext):
                dict['index'] = index
                dict['text'] = subtext
                dict['label'] = 1
                data.append(dict.copy())
                index += 1
                dict['text'] = []
                subtext = ''
                dict['label'] = None
            continue
        elif('피해자' in text or '사기범' in text):
            if('피해자' in text):
                text = text.replace('피해자 :', ' 피해자:')
                # re.sub('피해자', '피해자:', text)
                subtext += text
                # dict['text'].append(text)
            elif('사기범'  in text):
                text = text.replace('사기범 :', ' 사기범:')
                # re.sub('사기꾼', '사기꾼:', text)
                subtext += text
            # subtext += text
            # dict['text'].append(text)
    return data

out_file_path2 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/phishing_Data_18_new.json"
data2 = PhishingDataPreprocessing2(file_name2)        

# json 형식으로 저장
# ensure_ascii=False : 데이터를 한글로 저장
with open(out_file_path2, 'w', encoding='utf-8') as outfile:
    json.dump(data2, outfile, ensure_ascii=False)





