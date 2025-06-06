name=input("please enter your name: ")
with open("name.txt", "w") as file:
    file.write(name+"\n")

with open("name.txt", "r") as file:
    content=file.read()
    print("your name is:",content)

with open("numbers.txt", "w") as file:
    lines = ["17\n", "42\n", "400\n"]
    file.writelines(lines)

total=0

with open("numbers.txt", "r") as file:
    line_count = 0
    line = file.readline()

    while line and line_count < 2:
        total+=int(line.strip())
        line_count += 1
        line = file.readline()
print(total)

with open("numbers.txt", "r") as file:
    line_count2 = 0
    line=file.readline()
    while line:
        line_count2+=1
        line=file.readline()
print(line_count2)