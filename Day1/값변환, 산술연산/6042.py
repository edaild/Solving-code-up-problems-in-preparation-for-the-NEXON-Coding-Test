# 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

a = input()
a = float(a)
print(format(a, '.2f'))

#2
f = float(input())
print(round(f,2))