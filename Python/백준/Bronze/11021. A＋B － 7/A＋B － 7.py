T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    if 0 < A < 10 and 0 < B < 10:
        print(f"Case #{i}: {A + B}")