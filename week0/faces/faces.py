def main():
    text = input()
    new_txt = convert(text)
    print(new_txt)


def convert(string):
    new_txt = string.replace(":)","🙂")
    new_txt = new_txt.replace(":(","🙁")
    return new_txt

main()

