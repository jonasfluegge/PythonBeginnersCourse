emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}

sentence = input("Please enter a sentence: ")
words = sentence.split()

x = 0

while x < len(words):
    if words[x] in emoji_dict:
        words[x] = emoji_dict.get(words[x])
        x += 1
    else:
        x += 1

words = " ".join(words)
print(words)
