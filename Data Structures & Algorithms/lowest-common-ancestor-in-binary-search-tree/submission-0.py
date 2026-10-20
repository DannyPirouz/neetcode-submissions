# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        curr = root
        pval = p.val
        qval = q.val

        while True:
            currval = curr.val
            if (pval > currval and qval < currval) or (pval < currval and qval > currval):
                return curr
            if pval > currval and qval > currval:
                curr = curr.right
            if pval < currval and qval < currval:
                curr = curr.left
            if pval == currval or qval == currval:
                return curr
            

