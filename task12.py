word = input()
if "f" in word:
    if word.count("f") > 1:
        print(word.find("f"))
        print(word.rfind("f"))
    else:
        print(word.find("f"))