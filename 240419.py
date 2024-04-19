scores = []
while True:
  score=input("학생의 점수를 입력하세요:")
  if score.isdigit():
    scores.append(int(score)) #int 쓰면 숫자 형태로 값 추가
  else:
    break
print(scores)
scores=list(map(int,scores))
print(scores)
print("합계 :",sum(scores))
print("인원수 :",len(scores))
print("평균 : ", sum(scores)/len(scores))