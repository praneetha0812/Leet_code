# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def reverseNodes(child):
            if child == None:
                return;
             # Recursively invert left and right subtrees
            reverseNodes(child.left)
            reverseNodes(child.right)
            # Swap the left and right children
            hold = child.left
            child.left = child.right
            child.right = hold
        # Starting the recursive inversion from the root
        reverseNodes(root)
        return(root);
            
            
        