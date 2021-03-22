def hailstone(n):
    temp = 0
    my_list = [n]
    while my_list[-1] != 1:
        if my_list[-1]%2 == 0:
            temp = my_list[-1]//2
            my_list.append(temp)
        else:
            temp = my_list[-1]*3 + 1
            my_list.append(temp)
    return my_list


print(hailstone(5))