class Tree():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        spaces = " " * self.getlevel() * 5
        prefix = spaces + "=>" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def buildTree():
    root = Tree("Food")
    child1 = Tree("Vegeterian")
    child2 = Tree("Non Vegeterian")
    subchild1veg = Tree("Sambar")
    subchild2veg = Tree("dal")
    subchild3veg = Tree("curd")
    subchild1non = Tree("Chicken")
    subchild2non = Tree("Mutton")
    subchild3non = Tree("Egg")
    child1.addChild(subchild1veg)
    child1.addChild(subchild2veg)
    child1.addChild(subchild3veg)
    child2.addChild(subchild1non)
    child2.addChild(subchild2non)
    child2.addChild(subchild3non)
    root.addChild(child1)
    root.addChild(child2)
    root.printTree()



if __name__ == '__main__':
    buildTree()

