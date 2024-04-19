txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

tool_set = {'Python', 'Java', 'Ruby'}
x='->'.join(tool_set)
print(x)


number_list = [x**2 for x in range(10) if x % 2 == 0]
print(number_list)

numm = [x for x in range(11) if x % 2 == 0]
print(numm)


#S로 시작하는 도시명으로 리스트를 생성
citys =  ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
new_list = [city for city in citys if city.startswith('S')]
print(new_list)

#lambda, filter 사용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = list(filter(lambda x: x%2==0,numbers))
print(odd_nums) 

#enumerate 사용
tools =  ['Python', 'Java', 'JavaScript']
tool_list = [(idx,tool) for idx, tool in enumerate(tools, start=1)] #start=1 하면 인덱스번호 1부터 시작
print(tool_list)

def convert_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
scores = [88, 92, 78, 60, 75, 95]
new =



# 나이 리스트 중에서 18세 이상 나이만 추출
ages = [5, 12, 17, 18, 24, 32]
ages_list = list(filter(lambda x: x>=18,ages))
print(ages_list)