#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

def all_unique(S):
    arr = []
    length = len(S)

    for i in range(0, length-1):
        for j in range(i+1,length):
            #print "visited now: ",(S.visited[j],S.visited[i])
            temp = (S[j]-S[i])
            #print "temp: arr:",(temp,arr)
            if (temp in arr):
                return False
            arr.append(temp)
    return True

def successor(visited, length, elem):
    arr = []
    for i in range(elem+1, length+1):
        visited.append(i)
        if (all_unique(visited)):
            arr.append(i)
        visited.pop()
    return arr

def fwd_successor(visited, check, length, elem):
    arr = []
    for i in range(elem+1, length+1):
        if check[i] != 0:
            visited.append(i)
            if (all_unique(visited)):
                arr.append(i)
            visited.pop()
    return arr

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

def bt_recursive(visited, l, m):
    if len(visited) == m:
        return visited
    elem = visited.pop()
    visited.append(elem)
    successors = successor(visited,l,elem)
    print "successors: ",successors
    for val in successors:
        visited.append(val)
        if bt_recursive(visited,l,m):
            return visited
        else:
            visited.pop()

    return []


def bt_fwd_recursive(visited, fwd_check, l, m):
    if len(visited) == m:
        return visited
    elem = visited.pop()
    visited.append(elem)
    successors = fwd_successor(visited, fwd_check, l, elem)
    print "successors: ", successors
    for val in successors:
        check = fwd_check[:]
        check[val] = 0
        check = update_fwd_constrain(visited, check, val)
        print "check: val: ",val,check
        visited.append(val)
        print "visited: ",visited
        if bt_fwd_recursive(visited, check, l, m):
            return visited
        else:
            visited.pop()

    return []

#Your backtracking function implementation
def BT(L, M):
    "*** YOUR CODE HERE ***"
    visited = []
    successors = []

    visited.append(0)
    ret = bt_recursive(visited, L, M)
    print "arr: ",ret
    if len(ret) != 0:
        return M, ret
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    visited = []
    fwd_check = []
    for i in range(0,L+1):
        fwd_check.append(1)

    visited.append(0)
    fwd_check[0] = 0
    ret = bt_fwd_recursive(visited, fwd_check, L, M)
    if len(ret) != 0:
        return M, ret
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

def main():

    l,arr = FC(44,9)
    print "arr: ",arr

if __name__ == "__main__":
    main()
