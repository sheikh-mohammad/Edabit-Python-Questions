def stutter(word:str)->str:
    word = word.lower()
    return f"{word[0:2]}... {word[0:2]}... {word}?"

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))