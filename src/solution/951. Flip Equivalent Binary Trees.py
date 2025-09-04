## 951. Flip Equivalent Binary Trees 
# Problem Link: https://leetcode.com/problems/flip-equivalent-binary-trees/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        #check if both the root are None. If so then return True
        #check if one of them is None. If so then return False
        #Check if the root x and root y value is different. If so then
        #return False
        #we check two things recursively:
        #check if the left sub tree node and right sub tree node of both the tree is same
        #call it recursively.
        #now check the swap value. check the left node of root x with right node of root y. And
        #right node of root x with left node of root y. If after swaping the values, if is same 
        #then we gets True.
        #at the end return the or of swap and no swap. 

        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        no_swap = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

        swap = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        return swap or no_swap

        








