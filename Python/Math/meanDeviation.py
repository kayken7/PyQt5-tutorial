mean_data = [3200, 5500, 6200, 4300, 7200, 9000, 5700]
sum = 0
number = len(mean_data)

for salary in mean_data:
    sum += salary

mean = int(sum/number)

print(f"합계 : {sum} 총원: {number} 평균: {mean} ")

deviation = []

for salary in mean_data:
    data = salary - mean
    deviation.append(data)
print('\n# ----- 편차 출력 ----- #\n')
print(deviation)

import math

variance_data = []
sum = 0

for value in deviation:
    data = math.pow((value), 2)
    variance_data.append(data)

print('\n# ----- 편차 제곱 ----- #\n')
print(variance_data)

for value in variance_data:
    sum += value

variance = sum/len(variance_data)
print(f'분산: {int(variance)}')


standard_deviation = math.sqrt(variance)
print(f'표준편차: {int(standard_deviation)}')


