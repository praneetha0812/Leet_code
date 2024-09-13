# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None

        # Initialize a stack with the root node
        st = [root]
        
        # Iterate until the stack is empty
        while st:
            node = st.pop()
            
            if node:
                # Swap the left and right children
                hold = node.left
                node.left = node.right
                node.right = hold
                
                # Add children to the stack for further processing
                st.append(node.left)
                st.append(node.right)
        
        return root
