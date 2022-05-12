i = 0
f1lines = []
f2lines = []
countDraw = 0
countp1 = 0
countp2 = 0

with open("player1.txt") as f1:
    f1lines = f1.read().splitlines()
with open("player2.txt") as f2:
    f2lines = f2.read().splitlines()

while i < len(f1lines) and i < len(f2lines):
    if f1lines[i] == f2lines[i]:
        countDraw += 1
    elif f1lines[i] == "R" and f2lines[i] == "S":
        countp1 += 1
    elif f1lines[i] == "P" and f2lines[i] == "R":
        countp1 += 1
    elif f1lines[i] == "S" and f2lines[i] == "P":
        countp1 += 1
    else:
        countp2 += 1

    result = open("result.txt", "w")
    result.write("Player1 wins: " + str(countp1) + "\n")
    result.write("Player2 wins: " + str(countp2) + "\n")
    result.write("Draws: " + str(countDraw) + "\n")
    result.close()

    i += 1
