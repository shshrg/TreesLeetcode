# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallest_node(self, node):
        min_ = node.val
        while node.left:
            min_ = node.left.val
            node = node.left
        return min_

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root and key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        
            root.val = self.smallest_node(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root