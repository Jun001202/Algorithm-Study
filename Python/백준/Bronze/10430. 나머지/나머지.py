A, B, C =map(int, input().split())

if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
    print((A+B)%C)
    print(((A%C)+(B%C))%C)
    print((A*B)%C)
    print(((A%C)*(B%C))%C)