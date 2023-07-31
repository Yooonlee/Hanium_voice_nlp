import json

path1 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/phishing_Data_1517_new.json"
path2 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/phishing_Data_18_new.json"
path3 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/주요영역별회의음성인식데이터_new.json"
#json 불러오기
with open(path1) as file_1:
	data1 = json.load(file_1)
 
with open(path2) as file_2:
	data2 = json.load(file_2)
 
with open(path3) as file_3:
	data3 = json.load(file_3)
# 간단히 합치고 json으로 dump
out_file_path = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/PhishingDataConcat.json"

with open(out_file_path, "w" , encoding='utf-8') as new_file:
	json.dump(data1+data2+data3, new_file, ensure_ascii=False)

