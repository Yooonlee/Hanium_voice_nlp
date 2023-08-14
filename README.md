# Hanium_voice_nlp

### 보이스피싱 나머지 데이터는 맨 뒤에 넣음
#### chatgpt : 순서가 중요합니다. 첫 번째 파일(file1)의 내용 뒤에 두 번째 파일(file2)의 내용이 추가되기 때문에, file1이 길고 file2가 짧으면 문제 없이 작동할 것입니다. 하지만 그 반대의 경우 file2의 내용이 너무 길면 메모리 문제로 인해 짤릴 수 있습니다.

### 각자 이름으로 Branch를 만들어 업로드 해주시면 감사하겠습니다
#### 정상 데이터 - 002.주요 영역별 회의 음성인식 데이터 중에서 -  공중파 방송(사회,경제) , 라디오(사회,경제), 기타녹음(사회,경제), 인터넷방송(경제)만 사용하였습니다.(유사한 도메인의 데이터 선택) 
#### 정상 데이터 - 003.주제별 텍스트 일상 대화 데이터의 경우 일단 생략하였습니다. 

### 데이터/파일 설명
#### JsonDataConcat.py : Json Concat
#### phishingDataPreprocessing.py : 보이스피싱 데이터 전처리
#### DialogueDataPreprocessing.py : 정상 데이터 전처리
#### phishing_Data_18_new.json : 2018(거의다 텍스트로 제공됨)-2020.docx.txt 전처리 
#### phishing_Data_1517_new.json : 2015-2017 클로바노트.txt 전처리
#### 주요영역별회의음성인식데이터.json : 정상데이터(절반)_보이스피싱데이터.zip(일부 선택) 전처리 
#### PhishingDataConcat.json  : phishing_Data_18_new.json + phishing_Data_1517_new.json + 주요영역별회의음성인식데이터.json
