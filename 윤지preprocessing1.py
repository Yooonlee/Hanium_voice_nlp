import os

def convert_text_format(input_file, output_file): #클로바 노트에서만 필요한 기능. 이름과 내용이 다른 줄에 있는 걸 같은 줄로 모아줌.
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            current_speaker = None
            current_dialogue = ""

            for line in f_in:
                line = line.strip()

                if line in {"사기범", "피해자"}:
                    if current_speaker and current_dialogue:
                        f_out.write(f"{current_speaker} : {current_dialogue}\n")
                    current_speaker = line
                    current_dialogue = ""
                else:
                    current_dialogue += line + " "

            # Save the last dialogue
            if current_speaker and current_dialogue:
                f_out.write(f"{current_speaker} : {current_dialogue}\n")

def combine_consecutive_speeches(dialogue): #사기범이나 피해자가 연속으로 말한 내용이 있을 때 그걸 하나로 합쳐주는 함수
    combined_dialogue = []
    current_speaker = None
    current_speech = ""

    for line in dialogue:
        line = line.strip()  # remove leading/trailing whitespaces
        if not line:  # if line is empty
            continue
        speaker, speech = line.split(" : ", 1)  # split by first occurrence of " : "
        if speaker == current_speaker:  # if the speaker hasn't changed, append the speech to the current speech
            current_speech += " " + speech
        else:  # if the speaker has changed, append the current speech to the dialogue and start a new speech
            if current_speaker is not None:  # if this isn't the first line of the dialogue
                combined_dialogue.append(f"{current_speaker} : {current_speech}")
            current_speaker = speaker
            current_speech = speech

    # Append the final speech to the dialogue
    if current_speaker is not None:
        combined_dialogue.append(f"{current_speaker} : {current_speech}")

    return combined_dialogue

#Now modify the function for reading and writing files : 파일을 열어서 내용을 list 형태로 저장하고, 위에 있는 function을 실행하고 출력 파일에 저장

def combine_consecutive_speeches_in_file(dialogue, output_file_name):
        
    combined_dialogue = combine_consecutive_speeches(dialogue)
    
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for line in combined_dialogue:
            if (line == combined_dialogue[-1]):
                    line = line.replace("clovanote.naver.com", "")  # Remove "clover" from the last line : 클로바 노트 처리를 위해서만 필요함.
            output_file.write(line + '\n')  # Write each line to the output file followed by a newline character


# New function to handle all files in a directory
def process_all_files_in_directory(input_directory, output_directory, specific_line):
    # Make sure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop over all files in the input directory
    for filename in os.listdir(input_directory):
        # If the file is a text file
        if filename.endswith(".txt"):
            input_file_name = os.path.join(input_directory, filename)
            output_file_name = os.path.join(output_directory, filename)

            # Combine consecutive speeches and write to output file
            with open(input_file_name, 'r', encoding='utf-8') as input_file:
                dialogue = input_file.readlines()
            combine_consecutive_speeches_in_file(dialogue, output_file_name)

if __name__ == "__main__":

    #클로바 노트에서만 필요한 코드
    input_folder = "C:/Users/USER/Desktop/stt/clover_note"  # 입력 파일들이 있는 폴더명
    output_folder = 'C:/Users/USER/Desktop/stt/basic1'
    for input_file in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, input_file)
        if os.path.isfile(input_file_path):  # 파일인 경우에만 변환 작업 수행
            output_file = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}.txt")
            convert_text_format(input_file_path, output_file)

    #네이버 클라우드 api 결과에서도 필요한 코드
    input_directory = 'C:/Users/USER/Desktop/stt/basic1'
    output_directory = 'C:/Users/USER/Desktop/stt/basic2'
    specific_line = 'clovanote.naver.com'
    process_all_files_in_directory(input_directory, output_directory, specific_line)