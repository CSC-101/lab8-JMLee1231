#part1
#the function divides a single list into a list of lists of size 3 and the remaining elements
#input list of integers to be subdivided
#output list of lists that contain 3 integers at most
def groups_of_3(list1: list[int]) -> list[list[int]]:
    alpha_list = []
    num = 0
    while num<len(list1):
        new_list = []
        new_list.append(list1[num])
        if num+1<len(list1):
            new_list.append(list1[num + 1])
        if num+2<len(list1):
            new_list.append(list1[num + 2])
        alpha_list.append(new_list)
    return alpha_list

#part2
