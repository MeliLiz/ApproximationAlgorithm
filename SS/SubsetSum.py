
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
        if list[i] > last * (1+ delta):
            l1.append(list[i])
            last = list[i]
    return l1


# Approximation algorithm for the subset sum problem
# Takes a set S of n integers in arbitrary order, the target value t, and a parameter epsilon
def approx_subset_sum(S, n, t, epsilon):
    l0 = [0]
    for i in range(0, n):
        print( i, l0)
        # List adding xi to each element of l0
        list_added = [x + S[i] for x in l0]
        l1 = merge_lists(l0, list_added)
        print(l1)
        l1 = trim(l1, epsilon / (2 * n))
        print (l1)
        # Remove every element greater than t
        l1 = [x for x in l1 if x <= t]
        print(l1)
        l0 = l1
    return l0[len(l0)-1]


    
if __name__ == "__main__":
    S = input("Enter the list of integers (Only numbers separated by commas): ")
    t = int(input("Enter the target value: "))
    epsilon = float(input("Enter the epsilon value (0 < epsilon < 1): "))
    if epsilon <= 0 or epsilon >= 1:
        print("Invalid epsilon value")
        exit()
    S = S.split(",")
    # Remove the white spaces from the list
    S = [x.strip() for x in S]
    # Remove the [] and {} from the list
    S = [x.replace("[", "").replace("]", "").replace("{", "").replace("}", "") for x in S]
    S = [int(x) for x in S]
    r = approx_subset_sum(S, len(S), t, epsilon)
    print(r)