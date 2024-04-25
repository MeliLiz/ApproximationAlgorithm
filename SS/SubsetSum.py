
# Function to return an ordered list merging two ordered lists
def merge_lists(l1, l2):
    # Copy the lists to avoid modifying the original lists
    list1 = l1.copy()
    list2 = l2.copy()
    
    list = []
    while(len(list1) != 0 and len(list2) != 0):
        if list1[0] < list2[0]:
            list.append(list1[0])
            list1.pop(0)
        else:
            list.append(list2[0])
            list2.pop(0)
            
    if(len(list1) == 0):
        list += list2
    else:
        list += list1
    return list
    
# Function to return a trimmed sorted list
# Receives a sorted list and a delta value
def trim(list, delta):
    m = len(list)
    l1 = [list[0]] # y1 = list[0]
    last = list[0]
    for i in range(1, m):
        if list[i] > last + delta:
            l1.append(list[i])
            last = list[i]
    return l1
    
if __name__ == "__main__":
    list1 = [1, 3, 5]
    list2 = [2, 4, 6, 8, 10]
    
    l = trim([1, 3, 5, 7, 9, 11, 13, 15], 3)
    print (l)