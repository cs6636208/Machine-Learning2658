from anytree import Node, RenderTree

# Points
points = [(7,2),(5,9),(9,6),(4,7),(8,1),(7,6)]

# Manually built KD-tree structure from earlier
root = Node("(7,6) split x")
left = Node("(5,9) split y", parent=root)
right = Node("(7,2) split y", parent=root)

Node("(4,7)", parent=left)

Node("(8,1)", parent=right)
Node("(9,6)", parent=right)

# Render tree
tree_str = ""
for pre, fill, node in RenderTree(root):
    tree_str += "%s%s\n" % (pre, node.name)

tree_str
