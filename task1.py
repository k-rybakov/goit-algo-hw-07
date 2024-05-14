from tree_node import root

def find_max_in_bst(root):
    if not root:
        return None
    
    while root.right:
        print(root.val)
        root = root.right
        
    return root.val

max_val = find_max_in_bst(root)
print("Найбільше значення в BST:", max_val)
