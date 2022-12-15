file = open("morse.txt","r")
file = file.read()
file = file.split(" ")
output = open("morse_without_spaces.txt","a")
for line in file:
    output.write(line)
output.close()
