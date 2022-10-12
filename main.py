import random
#agressive
output = "!Crazy Box\n"

f = open("scrubbed.lflist.conf", "r")

for i in f:
    x = random.randrange(0, 4)
    if (x != 3):
        output += str(i).strip()
        output += " "
        output += str(x)
        output += "\n"
        #+= str(i).join(" ").join(str(x)).join("\n")


f.close()




f = open("CrazyBox.lflist.conf", "w")
f.write(output)
f.close()