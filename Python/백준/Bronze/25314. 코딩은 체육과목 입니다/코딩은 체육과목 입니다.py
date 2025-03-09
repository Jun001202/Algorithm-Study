N = int(input())

if 4 <= N <= 1000 and N % 4 == 0:
    print("long " * (N // 4) + "int")