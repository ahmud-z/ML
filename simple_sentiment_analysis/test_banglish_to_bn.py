word_dict = {
    "ami": "আমি",
    "ami": "আমি",
    "ame": "আমি",
    "kemon": "কেমন",
    "kamon": "কেমন",
    "kmn": "কেমন",
    "kamn": "কেমন",
    "valo": "ভাল",
    "vlo": "ভাল",
    "balo": "ভাল",
    "vhalo": "ভাল",
    "aci": "আছি",
    "acci": "আছি",
    "achi": "আছি",
    "cricket": "ক্রিকেট"
}

word = input("Enter a Banglish word: ")

demo = word.split()

for item in demo:
    for key, value in word_dict.items():
        if item == key:
            print(value, end=" ")
