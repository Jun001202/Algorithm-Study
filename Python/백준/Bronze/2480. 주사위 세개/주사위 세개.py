A, B, C = map(int, input().split())

if 1 <= A <= 6 and 1 <= B <= 6 and 1 <= C <= 6:
    if A == B == C:
        print(10000 + A * 1000)
    elif A == B or A == C:
        print(1000 + A * 100)
    elif B == C:
        print(1000 + B * 100)
    else:
        print(max(A, B, C) * 100)