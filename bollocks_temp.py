word_list = []
num_list = []
string = input(">>>")
word = ""
for char in string:
    if char == " " or char == ".":
        if word in word_list:
            index = word_list.index(word)
            num_list[index] += 1
        else:
            word_list.append(word)
            num_list.append(1)
        word = ""
        
    elif char != " ":
        word = word + char
    else:
        print("Error")

    if char == ".":
        for i in range(len(word_list)):
            word = word_list[i]
            num = num_list[i]
            print(word, ",", num)
