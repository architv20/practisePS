"""
Contains all the Tree Traversal Implementations

Coverage::

Strings
List
Array - 30-40 questions -Le
LinkedList - reverse 
Doubly LinkedList
Circular LinkedList
Heap-
Hash Table-
Queue-

Binary Search
Sort

level order
Boundary 
Right view
left view
bottom view

TREEs
    BFS:
        Recursively
        Iteratively

    DFS:
        PreOrder
            Recursively
            Iteratively

        InOrder
            Recursively
            Iteratively

        PostOrder
            Recursively
            Iteratively

GRAPHS:
    BFS:
        <to be added>
    DFS:
        <to be added>

"""


from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    def insertTreeNode(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if temp.value == newNode.value:
                return False
            if temp.value > newNode.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            if temp.value < newNode.value:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right
        return True
    
    def contains(self,value):
      
        temp = self.root
        while True:
        
            if temp.value == value:
                return True
            if temp.value > value:
                if temp.left is not None:
                    temp = temp.left
                  
                else:
                    return False

            if temp.value < value:
                if temp.right is not None:
                    temp = temp.right
               
                else:
                    return False
        return False

    def deleteNode(self,value):
        temp = self.root
        toBeDeleted = None
        parentTemp = self.root
        while True:
            if temp.value == value:
                toBeDeleted = temp 
                temp3 = temp.right
                if temp3:
                    while True:
                        if temp3.left:
                            temp3 = temp3.left
                        else:
                            return False
                else: 
                    temp3 = temp3.left

                toBeDeleted.value = temp3.value
                if temp.left:
                    temp = temp.left
                break
            elif temp.value > value:
                if temp.left == None:
                    return False
                temp = temp.left
            else:
                if temp.right == None:
                    return False
                temp = temp.right

        return temp.value

    def deleteNodeRSB(self,value):
        temp = self.root
        toBeDeleted = None
        tempParent = self.root
        while True:
            if temp.value == value:
                toBeDeleted = temp 
                break
            elif temp.value > value:
                if temp.left == None:
                    return False
                temp = temp.left
            else:
                if temp.right == None:
                    return False
                temp = temp.right

        t1 = toBeDeleted
        

        return temp.value
#  '''
#         temp3 = temp.right
#                 if temp3:
#                     while True:
#                         if temp3.left:
#                             temp3 = temp3.left
#                         else:
#                             return False
#                 else: 
#                     temp3 = temp3.left

#                 toBeDeleted.value = temp3.value
#                 if temp.left:
#                     temp = temp.left
# '''

    def bfs(self):
        results = []
        queue =  deque()
        currentNode = self.root
        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue.popleft()
            results.append(currentNode.value)
         
            if currentNode.left is not None:
                queue.append(currentNode.left)

            if currentNode.right is not None:
                queue.append(currentNode.right)

        return results


    def bfsRecursively(self):
        results = []
        queue = deque()
        
        if self.root is not None:
            queue.append(self.root)

        self._traverse(queue, results)
        
        return results

    def _traverse(self, queue, results):
        if not queue:
            return 

        currentNode = queue.popleft()
        results.append(currentNode.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        self._traverse(queue, results)


    def dfsPostorder(self):
        results = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            results.append(currentNode.value)
            
        traverse(self.root)
        return results




    def dfsPreOrderWithoutRecursion(self):
        results = []
        stack = deque()
        currentNode = self.root
        if self.root is not None:
            stack.append(currentNode)
        
        while stack:
            currentNode = stack.pop()
            results.append(currentNode.value)       

            if currentNode.right is not None:
                stack.append(currentNode.right)
            
            if currentNode.left is not None:
                stack.append(currentNode.left)
            
        return results
    

    
    
    def dfsInOrderWithoutRecursion(self):
        results = []
        stack = deque()
        currentNode = self.root

        while stack or currentNode:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            results.append(currentNode.value)
            
            currentNode = currentNode.right                  
        
        return results
         
    def dfs_post_order(self):
        stack = []
        result = []
        current_node = self.root
        last_visited = None

        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            peek_node = stack[-1]

            if peek_node.right and peek_node.right != last_visited:
                current_node = peek_node.right
            else:
                result.append(peek_node.value)
                last_visited = stack.pop()

        return result

    

    def dfsPreOrder(self):
        results = []

        def traverse(currentNode):
            results.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            
        
        traverse(self.root)
        return results
    

    def dfsPostorder(self):
        results = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            results.append(currentNode.value)
            
        traverse(self.root)
        return results
    

    def dfsInOrder(self):
        results = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            results.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return results
    



t = Tree()
t.insertTreeNode(10)
t.insertTreeNode(8)
t.insertTreeNode(12)
t.insertTreeNode(6)
t.insertTreeNode(9)

t.insertTreeNode(11)
t.insertTreeNode(15)

print(t.deleteNodeRSB(150))



# print("I'm root:: ",t.root.value)
# print("I'm right of root: ",t.root.right.value)
# print("I'm left of root: ", t.root.left.value)

# print("This is the position of right and left of the RIGHT-th Node in the Tree:\n")
# print(t.root.right.left.value)
# print(t.root.right.right.value)


# print("This is the position of right and left of the LEFT-th Node in the Tree:\n")
# print(t.root.left.left.value)
# print(t.root.left.right.value)


# print("\n check to see if value exists in the Tree: ",t.contains(2))


# print("This is BFS: ", t.bfs())

# print("\n This is BFS but Recursively:",t.bfsRecursively())
# print("\nThis is DFS - PreOrder: ", t.dfsPreOrder())

# print("\nThis is DFS - InOrder: ", t.dfsInOrder())


# print("\nThis is DFS - PreOrder: ", t.dfsPostorder())



# print("\nThis is DFS - PreOrder without using Recursion::\n\n ", t.dfsPreOrderWithoutRecursion())

# print("\nThis is DFS - InOrder without using Recursion::\n\n ", t.dfsInOrderWithoutRecursion())

# print("\nThis is DFS - Post without using Recursion::\n\n ", t.dfs_post_order())
