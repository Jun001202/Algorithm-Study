A, B = map(int, input().split())
C = int(input())

if 0 <= A <= 23 and 0 <= B <= 59 and 0 <= C <= 1000:

    B += C

    A += B // 60
    B %= 60

    A %= 24

    print(A, B)