import sys

T = int(sys.stdin.readline())

result = []

if 1 <= T <= 1000000:
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        if 1 <= A <= 1000 and 1 <= B <= 1000:
            result.append(str(A + B))

sys.stdout.write("\n".join(result) + "\n")