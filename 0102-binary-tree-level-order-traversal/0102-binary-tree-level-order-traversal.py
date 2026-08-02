# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = 0
        queue = deque([(root,0)])
        curr_level = []
        while queue:
            node,node_level = queue.popleft()
            if node_level != level:
                ans.append(curr_level.copy())
                level += 1
                curr_level = []
            if not node:
                continue
            curr_level.append(node.val)
            queue.append((node.left,level+1))
            queue.append((node.right,level+1))
        if curr_level:
            ans.append(curr_level.copy())

        return ans





