def ist_gerade(number):
    return number % 2 == 0


for n in range(100):
    if ist_gerade(n):
        print(n, "ist gerade")
    else:
        print(n, "ist ungerade")
