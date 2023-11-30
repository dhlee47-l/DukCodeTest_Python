import datetime

today=datetime.datetime.today()
waiting_peop=14000605

def solution(waiting_peop):
  days_in_year=0
  for i in range(10,0,-1):
    days_in_year+=2**i
  year=(waiting_peop//1200) // days_in_year
  left_days=(waiting_peop//1200)%days_in_year

  days_in_month_sum=0
  month=0
  for i in range(10,0,-1):
    minus_days=days_in_month_sum #minus_days: 차감일
    days_in_month_sum+=2**i
    month+=1
    if days_in_month_sum>left_days:
      break

  day=left_days-minus_days
  lasting_peop=waiting_peop % 1200
  hour=lasting_peop//100+9

  boardtime=[25,40,55,70,85,100]
  hour_to_board=lasting_peop%100+1
  for i in boardtime:
    if i >hour_to_board:
      minute=boardtime.index(i)*10
      break
  if lasting_peop % 100 == 99:
    hour+=1
    minute=0

  if(today.minute+minute>60):
    minute=(today.minute+minute)-60
    hour+=1

  return f'{year+2020}년 {month}월 {day}일 {hour}시 {minute}분 출발'
print(solution(waiting_peop))