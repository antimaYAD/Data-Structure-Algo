class TreeNode :
    def __init__(self, val):
        self.data = val
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_len(self):
        level = 0
        p = self.parent
        while p: 
            level += 1
            p = p.parent
        return level 
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
        
def build_tree():
    root = TreeNode("season")
    
    winter = TreeNode("Winter")    
    winter.add_child(TreeNode("Sweater"))
    winter.add_child(TreeNode("Socks"))
    winter.add_child(TreeNode("Shols"))
        
    rain = TreeNode("Rainy")
    rain.add_child(TreeNode("Umbrella"))
    rain.add_child(TreeNode("Raincoat"))
    rain.add_child(TreeNode("Jumboots"))
        
    summer = TreeNode("Summer")
    summer.add_child(TreeNode("T-shirt"))
    summer.add_child(TreeNode("Shorts"))
    summer.add_child(TreeNode("Sunglasses"))
    
    root.add_child(winter)
    root.add_child(rain)
    root.add_child(summer)
    
    
    return root
    
if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
    pass