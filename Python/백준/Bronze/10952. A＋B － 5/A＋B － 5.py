while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if 0 < A < 10 and 0 < B < 10:
        print(A + B)