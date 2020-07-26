words = input().split()
for word in words:
    if word.lower().startswith(("https://", "http://", "www.")):
        print(word)