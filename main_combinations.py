kb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']
gb = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'ẞ']
z  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sz = ['!','?', '"', '§', '$', '%', '&', '/', '(', ')', '=', '?', '´', '`', '*', '+', '~', "'", '^', '#', '@', '€', '{', '[', ']', '}', '\\', '<', '>', '|', ',', ';', '.', ':', '-', '_']
chars = []

def combinator(amount: int, previous: str, file=None) -> None:
    if amount == 0:
        if file:
            file.write(previous + "\n")
        else:
            print(previous)
    else:
        for element in chars:
            combinator(amount - 1, previous + element, file)


if input(f'\nSollen Kleinbuchstaben ({len(kb)}) verwendet werden? (y/n)\n $ ') == 'y':
    chars.extend(kb)
if input(f'\nSollen Großbuchstaben ({len(gb)}) verwendet werden? (y/n)\n $ ') == 'y':
    chars.extend(gb)
if input(f'\nSollen Zahlen ({len(z)}) verwendet werden? (y/n)\n $ ') == 'y':
    chars.extend(z)
if input(f'\nSollen Sonderzeichen ({len(sz)}) verwendet werden? (y/n)\n $ ') == 'y':
    chars.extend(sz)

file = input("\nSollen alle Möglichkeiten in einer Datei gespeichert werden? (y/n)\n $ ")

if file == "y":
    with open("output.txt", "w", encoding="utf-8") as save:
        for i in range(1,17):
            combinator(amount = i, previous = "", file = save)
else:
    for i in range(1,17):
        combinator(amount = i, previous = "")

