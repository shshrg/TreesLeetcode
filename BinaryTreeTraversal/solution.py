# Pre-order traversal
def pre_order(node):
    result = []
    result += [node.data] if node else []
    if node and node.left:
        result += pre_order(node.left)
    if node and node.right:
        result += pre_order(node.right)
    return result

# In-order traversal
def in_order(node):
    result = []
    if node and node.left:
        result += in_order(node.left)
    result += [node.data] if node else []
    if node and node.right:
        result += in_order(node.right)
    return result

# Post-order traversal
def post_order(node):
    result = []
    if node and node.left:
        result += post_order(node.left)
    if node and node.right:
        result += post_order(node.right)
    result += [node.data] if node else []
    return result

