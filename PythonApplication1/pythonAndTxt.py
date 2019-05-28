def readLinByLine(file):
    fh = open(file, mode="r", encoding="utf-8")
    for line in fh:
        print(line)
    fh.close()

def deleteEmptyLines(file):
    with open(file, mode='r', encoding='ansi') as f, open('C:\\Users\\r103co62\\Desktop\\test dva potpisa\\novi.csv', mode='w', encoding='ansi') as w:
        for line in f:
            if not line.strip():
                continue
            w.write(line)

def obrisiNeispravnePostanskeBrojeve(file):
        with open(file, mode='r', encoding='ansi') as f, open('C:\\Users\\r103co62\\Desktop\\test dva potpisa\\novi2.csv', mode='w', encoding='ansi') as w, open('C:\\Users\\r103co62\\Desktop\\test dva potpisa\\NeispravneAdrese.csv', mode='w', encoding='ansi') as n:
            for line in f:
                if '99999' in line:
                    n.write(line)
                else:
                    w.write(line)
    