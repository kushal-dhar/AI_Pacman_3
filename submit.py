#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

def all_unique(S):
    arr = []
    length = len(S.visited)

    for i in range(0, length-1):
        for j in range(i+1,length):
            #print "visited now: ",(S.visited[j],S.visited[i])
            temp = (S.visited[j]-S.visited[i])
            #print "temp: arr:",(temp,arr)
            if (temp in arr):
                return False
            arr.append(temp)
    return True

def successor(S, length, elem):
    arr = []
    for i in range(elem+1, length+1):
        #print "I: ",i
        S.visited.append(i)
        #print "S.visisted: ",S.visited
        if (all_unique(S)):
            #print "i: ",(elem, i)
            arr.append(i)
        S.visited.pop()
    arr.reverse()
    return arr

#Your backtracking function implementation
def BT(L, M):
    "*** YOUR CODE HERE ***"
    visited = []
    successors = []

    visited.append(0)
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

def main():
    l,arr = BT(11,5)
    print "arr: ",arr

if __name__ == "__main__":
    main()
