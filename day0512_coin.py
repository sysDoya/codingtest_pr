"""
문제: 거스름돈
카운터에는 사용할 500원, 100원, 50원, 10원짜리 동전이 무한하게 준비되어 있다
손님에게 거슬러 줘야 할 돈이 N원 일때 거슬러 줘야 할 동전의 최소 개수를 구하라 
거슬러야 할 돈 N은 항상 10의 배수다 
"""
import time
start_time = time.time()

N= int(input('손님이 낸 금액을 입력하세요: '))
count = 0

coin = [500, 100, 50, 10]

for i in coin:
  count += N // i 
  N %= i

end_time = time.time()
print('걸린시간: ', end_time - start_time)
print(count)

"""
출력 결과
손님이 낸 금액을 입력하세요: 1260
걸린시간:  2.3917789459228516
6
"""