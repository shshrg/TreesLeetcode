def get_levels_dict(node, level = 0, result = {}):
    if node:
        if level in result.keys():
            result[level].append(node.value)
        else:
            result[level] = [node.value]
    if node and node.left:
        result.update(get_levels_dict(node.left, level+1, result))
    if node and node.right:
        result.update(get_levels_dict(node.right, level+1, result))
    return result

def tree_by_levels(node):
    return sum(get_levels_dict(node).values(), [])
    