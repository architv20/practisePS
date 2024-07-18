class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        nd = Node(value)
        temp = self.root
        while True:
            if temp == None:
                self.root = nd
                return True
            elif temp.value > value:
                if temp.left is None:
                    temp.left = nd
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = nd
                    return True
                temp = temp.right
    
    def check(self,value):
        temp = self.root
        while True:
            if temp.value == value:
                return True
            elif temp.value > value:
                if temp.left is not None:
                    temp = temp.left
                else:  
                    return False
            else:
                if temp.right is not None:
                    temp = temp.right
                else: 
                    return False
    
    def delete(self,value):
        temp = self.root
        while True:
            if temp.value == value:
                
                return True
            elif(temp.value > value):
                if temp.left is not None:
                    temp = temp.left
                else:
                    return False
            else: 
                if temp.right is not None:
                    temp = temp.right
                else:
                    return False

    def BFS(self):
        queue = []
        results = []
        current_node = self.root
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)     
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    # root->left->right 
    def dfs_pre_order(self):
        results = [] 
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    # left->right->root
    def dfs_post_order(self):
        results = [] 
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    # left->root->right
    def dfs_in_order(self):
        results = [] 
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
if __name__ == "__main__":
    t = BST()
    t.insert(47)
    t.insert(21)
    t.insert(76) 
    t.insert(18)
    t.insert(27)
    t.insert(52)
    t.insert(82)
    print(t.BFS())
    print(t.dfs_pre_order())
    print(t.dfs_post_order())
    print(t.dfs_in_order())

    # print(t.check(1))
    # print(t.delete(1))
    # print(t.check(1))
