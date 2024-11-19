


list = []
with open("./passwords.txt") as file :
    with open("./result.txt", "w") as result:
        for line  in file :
            result.writelines(f'"{line.strip()}",')
            list.append(f'"{line.strip()}",')


for element in list :
    print(element)