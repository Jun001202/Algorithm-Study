H, M = map(int, input().split())

if 0 <= H <= 23 and 0 <= M <= 59:

    M -= 45
    if M < 0:
        M += 60
        H -= 1
    if H < 0:
        H = 23

print(H, M)