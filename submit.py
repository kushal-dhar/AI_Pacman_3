#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

# implementation to check all posible orders
# it will exclude any if that order is already present in out visited array
def all_unique(S):
    arr = []
    length = len(S)

    #loop on the full length of array
    for i in range(0, length-1):
        for j in range(i+1,length):
            #### print "visited now: ",(S[j],S[i])
            #find the order r to check if it is unique or not
            temp = (S[j]-S[i])
            #### print "temp: arr:",(temp,arr)
            #### print "**********************************"
            #if order temp is already in arr then no need to computer further
            if (temp in arr):
                return False
            #if temp is unique than add it in possible order array
            arr.append(temp)
    return True

#implementation to find out successor functions
def successor(visited, length, elem):
    arr = []
    #loop for all the elements greater than elem till L
    for i in range(elem+1, length+1):
        #Add current node to the visited array
        visited.append(i)
        #check after adding i to visited we are getting
        #all the unique order differences or not
        #if yes than return all valid possible orders
        if (all_unique(visited)):
            arr.append(i)
        visited.pop()
    return arr

#implementation to fetch successors of the current under processing node
def fwd_successor(visited, check, length, elem):
    arr = []
    for i in range(elem+1, length+1):
        #if the frwd_check bit is not 0
        #i.e. if it is not already processed
        if check[i] != 0:
            visited.append(i)
            if (all_unique(visited)):
                arr.append(i)
            visited.pop()
    #returning the unique visited array
    return arr

#check forward constrain for every node in check
def update_fwd_constrain(visited, check, elem):
    length = len(visited)

    print "visited: ",visited
    for i in range(0,length-1):
        for j in range(i+1,length):
            #if check[i] == 0 and check[j] == 0:
            dist = visited[j]-visited[i]
            if elem+dist < len(check):
                print "elem: dist, i, j",elem,dist, i , j
                check[elem+dist] = 0
    return check

#bt_recursive implementation
def bt_recursive(visited, l, m):
    #If length of visited array is m i.e. we have found the order M
    # elements than return visited array
    if len(visited) == m:
        return visited

    #Get the last element of visited array
    elem = visited[len(visited) - 1]
    #Find the successor functions of visited array
    successors = successor(visited,l,elem)
    print "successors: ",successors
    #process each child one by one
    for val in successors:
        #append child in visited
        visited.append(val)
        #recursively build visited array of unique orders
        if bt_recursive(visited,l,m):
            return visited
        else:
            visited.pop()

    return []


def bt_fwd_recursive(visited, fwd_check, l, m):
    #Termination condition, return if we get m order set
    if len(visited) == m:
        return visited

    elem = visited[len(visited) - 1]
    #fetch forward successors
    successors = fwd_successor(visited, fwd_check, l, elem)
    print "successors: ", successors
    #process each successor recursively for backtracking with forward checking
    for val in successors:
        check = fwd_check[:]
        check[val] = 0
        # check forward constrain for every node in check
        check = update_fwd_constrain(visited, check, val)
        print "check: val: ",val,check
        visited.append(val)
        print "visited: ",visited
        # recursively call backtracking with forward constraint checking for rest of the elements
        if bt_fwd_recursive(visited, check, l, m):
            return visited
        else:
            visited.pop()

    return []

#Your backtracking function implementation
def BT(L, M):
    #Visited Nodes
    visited = []
    #Successors Nodes of current Popped Item
    successors = []

    #Start by appending the first node in visited array
    visited.append(0)
    #Called bt_recursive to recursively find out all the order M combination
    ret = bt_recursive(visited, L, M)
    print "arr: ",ret
    #check if valid orders is available or not than return
    # M value and orders array
    if len(ret) != 0:
        return M, ret
    #if no combination of orders present return empty array
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):
    visited = []
    fwd_check = []

    #Initiallizing all the bits to 1
    for i in range(0,L+1):
        fwd_check.append(1)

    visited.append(0)
    fwd_check[0] = 0

    #initiate recursive frwrd recursive checking
    ret = bt_fwd_recursive(visited, fwd_check, L, M)
    # check if valid orders is available or not than return
    # M value and orders array
    if len(ret) != 0:
        return M, ret
    # if no combination of orders present return empty array
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

def main():

    #check for BackTracking for L = 6 and M = 4 , BT(L,M)
    # l,arr = BT(6,4)
    #check for BackTracking with Forward Checking for L = 44 and M = 9, FC(44,9)
    l,arr = FC(44,9)
    print "arr: ",arr

if __name__ == "__main__":
    main()
