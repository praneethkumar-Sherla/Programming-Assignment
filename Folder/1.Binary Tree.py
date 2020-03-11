class Node:
    def __init__(self, info):
        self.info=info
        self.left = None  
        self.right = None 
        self.level = None 

    def _str_(self):
        return self.info

class binarytree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
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

def lca(root, a, b):
    
    while True:
            
        if root.info>a and root.info>b:
            root=root.left
        
        elif root.info<a and root.info<b:
            root=root.right
            #print(lca.root)
        
        else:
            return root

tree = binarytree()
t=int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
