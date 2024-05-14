from tree_node import root

def sum_of_values_in_bst(root):
    if not root:
        return 0
    
    current_sum = root.val
    
    if root.left:
        current_sum += sum_of_values_in_bst(root.left)
    
    if root.right:
        current_sum += sum_of_values_in_bst(root.right)
    
    return current_sum

total_sum = sum_of_values_in_bst(root)
print("Сума всіх значень в BST:", total_sum)