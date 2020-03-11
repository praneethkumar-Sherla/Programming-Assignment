class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class binarytree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            present = self.root
         
            while True:
                if val < present.info:
                    if present.left:
                        present = present.left
                    else:
                        present.left = Node(val)
                        break
                elif val > present.info:
                    if present.right:
                        present = present.right
                    else:
                        present.right = Node(val)
                        break
                else:
                    break

def level(root):
    lis = []
    lis.append(root)
    while(len(lis)>0):
        node = lis.pop(0)
        print (node,end=' ')
        if node.left:
            lis.append(node.left)
        if node.right:
            lis.append(node.right)
    else:
        print(' ')
       



tree = binarytree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

level(tree.root)
