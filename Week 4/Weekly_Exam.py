arr = []
out = ""
with open("key.txt", "r") as data:
    for line in data:
        arr.append(line.split())
    print(arr)

with open("secret.txt", "r") as data:
    lines = data.readlines()
    start = 0
    end = int(arr[0][0])
    for i in range(int(arr[1][0])):
        for j in range(start, end):
            lines[j] = lines[j].strip()
            out = out + lines[j]
        out = out + "\n"
        start += int(arr[0][0])
        end += int(arr[0][0])
    print(out)

public = open("public.txt", "w")
public.write(out)
public.close()
