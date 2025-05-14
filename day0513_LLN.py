'''
큰수의 법칙 
입력조건
첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다
(2<=N<=1000, 1<=M<=10000, 1<=K<=10000)
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다
입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력조건
첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다

입력예시
5 8 3
2 4 5 4 6

출력
46

N -> 숫자의 개수, M-> 총 더하는 횟수, K-> 연속해서 더할 수 있는 최대 횟수 
'''
import time

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
start_time = time.time()
num.sort(reverse = True)

first_num = num[0]
second_num = num[1]

x = m // (k+1)
y = m % (k+1)

result = (x * (first_num * k +second_num) + (y * first_num))
end_time = time.time()
print(result)
print(f'걸린 시간: {round(end_time - start_time, 1)}초')

'''
입력
5 8 3
2 5 6 3 1
출력
46
걸린 시간: 0.0초
'''