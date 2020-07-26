from collections import defaultdict
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data or self.data == 0:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # def insert(self, val):
    #     if not self.root:
    #         self.root = Node(val)
    #     else:
    #         node = self.root
    #         while (True):
    #             if (node.info > val):
    #                 if node.left:
    #                     node = node.left
    #                 else:
    #                     node.left = Node(val)
    #                     break
    #             else:
    #                 if node.right:
    #                     node = node.right
    #                 else:
    #                     node.right = Node(val)
    #                     break
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.data == 0 or self.data:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=" ")

    def levelorder(self, root):
        elements = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            elements.append(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return elements

    def reverse_levelorder(self, rootnode):
        if self.data is None:
            return
        queue = []
        queue.append(rootnode)
        elements = []

        while len(queue) > 0:
            elements.append(queue[0].data)
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        elements.reverse()
        return elements
    def traversal_without_recursion(self,root):
        stack = []
        elements = []
        current = root

        while current !=None or len(stack) !=0:
            while current!=None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            elements.append(current.data)
            current = current.right
        print(elements)

    from collections import defaultdict

    def topView(self,root):
        if root is None:
            return None
        queue = [(root, 0)]
        hashtable = defaultdict(list)
        for node, level in queue:
            if node is not None:
                hashtable[level].append(node.info)
            if node.left is not None:
                queue.extend([(node.left, level - 1)])
            if node.right is not None:
                queue.extend([(node.right, level + 1)])
        if hashtable:
            for level in range(min(hashtable.keys()),
                               max(hashtable.keys()) + 1):
                print(hashtable[level][0], end=' ')
        else:
            return None
    def leftview(self, root):
        elements = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            elements.append(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)


        return elements

    def rightview(self, root):
        elements = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            elements.append(queue[0].data)
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)

        return elements

    def search(self, value):
        if self.data == value:
            return True
        elif value > self.data:
            if self.right:
                return self.right.search(value)
        else:
            if self.left:
                return self.left.search(value)
        return False


    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)
    def size(self,root):
        queue = []
        c = 0
        if root.data:
          queue.append(root)
        while len(queue) > 0:
            node = queue.pop()
            c +=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return c
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def delete(self,value):
        if self.search(value):
            if value < self.data:
                if self.left:
                    self.left = self.left.delete(value)
            elif value > self.data:
                if self.right:
                    self.right = self.right.delete(value)
            else:
                if self.left is None or self.right is None:
                    return None
                if self.left is None:
                    return self.right
                if self.right is None:
                    return self.left
                maxi = self.find_max()
                self.data = maxi
                self.left = self.left.delete(value)
        return self

    s = 0

    def sumOfLeafNodes(self,root):
        s = 0
        if root == None:
            return 0
        if root.left == None and root.right == None:
            s += root.data
        s += root.left.sumOfLeafNodes(root.left)
        s += root.right.sumOfLeafNodes(root.right)
        return s
    def invertTree(self,root):
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

def lca(root, v1, v2):
    if root == None:
        return
    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    elif root.info < v1 and root.info < v2:
        return lca(root.left, v1, v2)
    else:
        return root

if __name__ == "__main__":
    root = Node(8)  # 7,1,0,3,2,5,4,6,9,8,10
    root.insert(6) #8 6 5 7 11 12 13 10 9
    root.insert(5)
    root.insert(7)
    root.insert(11)
    root.insert(12)
    root.insert(13)
    root.insert(10)
    root.insert(9)

    print(lca(root,9,12))
    root.insert(36)
    root.insert(33)
    root.insert(40)
    print(root.delete(40))
    print("Inorder")
    root.inorder()
    root.invertTree(root)
    print()
    root.inorder()
    print()
    print("Preorder")
    root.preorder()
    print()
    print("Postorder")
    root.postorder()
    print()
    print("Level Order")
    print(list(root.levelorder(root)))
    print("Reversed Level Order")
    print(list(root.reverse_levelorder(root)))
    print(root.search(4))
    print(root.height(root))
    print(root.size(root))
    print("max = ",root.find_max(),"min = ",root.find_min())
    print("leftview",root.leftview(root))
    print("Right view",root.rightview(root))
    print(root.traversal_without_recursion(root))
    root.inorder()
    print(root.sumOfLeafNodes(root))