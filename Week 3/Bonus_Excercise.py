while True:
    shift_input = input("Please enter the number of places to shift: ")
    if 0 <= int(shift_input) <= 25 and shift_input.isdecimal():
        break
    else:
        continue
sentence_input = input("Please enter a sentence: ").lower()
result = ""

for i in range(len(sentence_input)):
    char = sentence_input[i]
    if not char.isalnum():
        result += sentence_input[i]
    else:
        result += chr((ord(char) + int(shift_input) - 97) % 26 + 97)

print("The encrypted sentence is: ", result)
