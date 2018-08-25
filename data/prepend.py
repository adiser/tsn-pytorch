
import os

for filename in os.listdir(os.getcwd()):
    if ((filename.endswith(".txt")) and not(filename.endswith("dest.txt"))):
        with open(filename) as source:
            with open(filename[:-4] + "_dest.txt", "w+") as dest:
                for sourceline in source:
                    dest.write("../" + sourceline)

