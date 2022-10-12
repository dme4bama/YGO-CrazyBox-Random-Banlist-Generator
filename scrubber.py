#takes input banlist and reformats it for use in crazybox
f = open("Untitled Banlist.lflist.conf", "r")

output = ""

#st = f.readline()

for st in f:
    output += st.split(" ")[0] + "\n"
f = open("scrubbed.lflist.conf", "w")
f.write(output)
#print(output)

f.close()