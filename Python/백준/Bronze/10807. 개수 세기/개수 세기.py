N = int(input())

if not (1 <= N <= 100):
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != N:
    exit()

if any(num < -100 or num > 100 for num in numbers):
    exit()

v = int(input())

if not(-100 <= v <= 100):
    exit()

count = numbers.count(v)

print(count)