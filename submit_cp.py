#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

#Your backtracking function implementation
class Stack:
    def __init__(self):
        self.items = []
        self.visited = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

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

def BT(L, M):
    "*** YOUR CODE HERE ***"

    S = Stack()
    found = False
    arr = []
    level = 0
    nodes = 0

    S.items.append(0)
    while (not S.isEmpty()):
        nodes += 1
        print "items now: ",S.items
        item = S.pop()
        S.visited.append(item)
        if (len(S.visited) == M):
            return (L,S.visited)
        arr = successor(S,L,item)
        print "arr: ,successor: ",(item,arr,S.visited)
        if not arr:
            print "successor now: ",S.visited
            for i in S.visited:
                #print "i: ",i,item
                #if i >= item:
                #pos = S.visited.index(i)
                pos = 0
                pos = len(S.visited) - 1 - S.visited[::-1].index(item)
                S.visited = S.visited[:pos]
                print "visited now: ",S.visited
                break
        else:
            level += 1
            for i in arr:
                S.items.append(i)

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
