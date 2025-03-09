import sys

input_data = sys.stdin.read().splitlines()

for i in input_data:
    A, B = map(int, i.split())
    if 0 < A < 10 and 0 < B < 10:
        print(A + B)