alist = [2,2,2,2,3,3,7]

def thanos(alist):

    temp_list = []

    for char in alist:
        if char not in temp_list:
            if alist.count(char) % 2 == 0:
                count = alist.count(char) / 2
            else:
                count = alist.count(char)

            for i in range(int(count)):
                temp_list.append(char)
            
        return temp_list
