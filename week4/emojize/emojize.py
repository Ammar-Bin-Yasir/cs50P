import emoji

txt = input("Input: ")

if ":thumbsup:" in txt or ":earth_asia:" in txt:
    print(f"Output {emoji.emojize(txt, language='alias')}")
else:
    print(f"Output {emoji.emojize(txt)}")
