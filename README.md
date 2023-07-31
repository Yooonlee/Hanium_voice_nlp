# Hanium_voice_nlp
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
