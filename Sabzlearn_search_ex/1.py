f = open("cont.txt", "r+")

k = sorted(f)
m = open("next_text.txt", "w")
for i in k:
    i.rstrip("\n")
    m.write(i)

