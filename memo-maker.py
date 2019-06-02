from bs4 import BeautifulSoup
import requests

filePath = "speffs-memo.txt"

print("Starting. Downloading letter pair page...")
data = requests.get("https://www.speedsolving.com/wiki/index.php/List_of_letter_pairs").text
soup = BeautifulSoup(data, "html.parser")
print("Finished downloading letter pair page.\n")


def write_memos(memos):
    file_out = open(filePath, "w")
    for memo in memos:
        file_out.write(memo + "\n")
    file_out.close()


def get_memo(pair):
    ul = soup.find(id=pair).parent.parent.findNext("ul").findAll("li")
    memos = [m.text for m in ul]

    print("Pair: {}\n".format(pair))
    for i in range(len(memos)):
        if memos[i] == "...":
            break

        print("[{}]: {}".format(i, memos[i]))

    print()
    option = input("Choice: ")

    if option.isdigit() and 0 <= int(option) < len(memos):
        choice = memos[int(option)]
    else:
        choice = option

    print("Using {} -> \"{}\"\n".format(pair, choice))

    return "{}: {}".format(pair, choice)


fileIn = open(filePath)
memos = [line[:-1] for line in fileIn]
fileIn.close()

for i in range(len(memos)):
    if len(memos[i]) == 4:
        memos[i] = get_memo(memos[i][0:2])
        write_memos(memos)
