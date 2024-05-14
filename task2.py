from tree_node import root

def find_min_in_bst(root):
    if not root:
        return None
    
    while root.left:
        root = root.left
    
    return root.val

min_val = find_min_in_bst(root)
print("Найменше значення в BST:", min_val)