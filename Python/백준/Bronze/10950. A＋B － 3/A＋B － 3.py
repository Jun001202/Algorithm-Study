T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    if 0 < A < 10 and 0 < B < 10:
        print(f"{A + B}")