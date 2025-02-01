import json

# 텍스트 파일을 읽고, 라인별로 데이터 추출
input_file = 'servers.txt'  # 서버 정보가 들어있는 텍스트 파일
output_file = 'profiles.json'  # 생성할 JSON 파일

# 프로필을 담을 리스트
profiles = []

# 텍스트 파일을 열고 한 줄씩 읽기
with open(input_file, 'r') as file:
    for line in file:
        # 쉼표로 구분된 값 분리
        server_name, command = line.strip().split(',')
        
        # JSON 형식에 맞는 프로필 객체 생성
        profile = {
            "Name": server_name,
            "Guid": server_name,
            "Custom Command": "Yes",
            "Command": command
        }
        
        # 프로필 리스트에 추가
        profiles.append(profile)

# JSON 파일로 저장
with open(output_file, 'w') as json_file:
    json.dump({"Profiles": profiles}, json_file, indent=4)

print(f"{output_file} 파일이 생성되었습니다.")
