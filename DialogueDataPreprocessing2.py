# import json
# import re
# import os
# from collections import defaultdict
# from typing import List
# file_path = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/정상대화데이터/002.주요 영역별 회의 음성인식 데이터/01.데이터/"

# list1 = ['1.Training/라벨링데이터/', '2.Validation/라벨링데이터/']
# list2 = ['공중파방송/', '기타녹음/', '라디오/', '인터넷방송/']
# list3 = ['경제/', '사회/']

# # 전체 파일로 확장
# data = []
# index = 0
# for i in list1:
#     file_path1 = file_path + i
#     for j in list2:
#         file_path2 = file_path1 + j
#         for k in list3:
#             try:
#                 file_path3 = file_path2 + k
#                 file_list = os.listdir(file_path3)
#                 # file_list =  각 디렉토리의 파일의 리스트
#                 for i in file_list:
#                     file_name = file_path3 + i
#                     with open(file_name, 'r', encoding='utf-8') as file:
#                         content = file.read()
#                     content = json.loads(content)
#                     dict = {}
#                     dict['text'] = []
#                     dict['index'] = None
#                     # 각 파일에서 data로 더해줌 
#                     # 단 하나의 json 파일안에 대화내용이 길어서 25문장씩 끊어서 1개의 대화를 만듦 
#                     for i, full in enumerate(content['utterance']):
#                         speaker = full['speaker_role'] + ":"
#                         con = full['original_form']
#                         dict['text'].append(speaker + " "+ con) 
#                         if(i > 1  and ( (i % 25) == 0)):
#                             index  += i/25
#                             dict['index'] = int(index)
#                             data.append(dict.copy())
#                             dict['text'] = []
#                             dict['index'] = None
#             except:
#                 continue


# # print(data)


# out_file_path1 = "/Users/kylee/Desktop/대외활동및공부/한이음/보이스피싱/데이터/주요영역별회의음성인식데이터.json"
# # # json 형식으로 저장
# # # ensure_ascii=False : 데이터를 한글로 저장
# with open(out_file_path1, 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)

