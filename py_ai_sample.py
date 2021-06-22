import sys
import math
import json


with open('temp.json') as json_file:
    json_data = json.load(json_file)


MAX_NUMBER = 16000


my_position = [] #내 돌의 위치정보(좌표)
your_position = [] #상대방 돌의 위치정보(좌표)

for key in json_data["my_position"].keys():
    my_position.append(json_data["my_position"][key]) #내 포지션 배열에 돌 좌표 하나씩 기입

for key in json_data["your_position"].keys():
    your_position.append(json_data["your_position"][key]) #상대포지션도 마찬가지

#내가 가지고 있는 돌들 중에서 가장 가까운 위치에 있는 상대방의 돌을 알아내서 공격하는 알고리즘
current_stone_number = 0 #
index = 0
min_length = MAX_NUMBER #16000
x_length = MAX_NUMBER
y_length = MAX_NUMBER

#내 돌을 하나씩 잡으며 잡을 때마다 상대 돌과의 거리를 하나씩 계산하여 최소값 구현
for my in my_position:
    for your in your_position:
        x_distance = abs(my[0] - your[0]) #내 돌과 상대 돌과의 x축거리
        y_distance = abs(my[1] - your[1]) #내 돌과 상대 돌과의 y축거리
        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance) #내 돌과 상대 돌 사이의 현재 거리
        if min_length > current_distance: #현재거리가 최소거리보다 작다면
            current_stone_number = index 
            min_length = current_distance #현재거리를 최소거리로 삼는다.
            x_length = your[0] - my[0] #최소거리에서의 x축거리
            y_length = your[1] - my[1] #최소거리에서의 y축거리

    index = index + 1

#Return values
message = ""
stone_number = current_stone_number #최종 도출된 최소거리에 있는 상대방의 돌을 스톤 넘버에 넣어준다.
##x축, y축 거리에 비례해서 힘조절
stone_x_strength = x_length * 5 #비례상수 곱하기
stone_y_strength = y_length * 5
result = [stone_number, stone_x_strength, stone_y_strength, message]


print(str(result)[1:-1].replace("'", ""))
