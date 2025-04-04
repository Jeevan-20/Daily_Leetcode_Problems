from typing import Optional, List
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)
        
        return dfs(root)[1]

    @staticmethod
    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = deque([root])
        idx = 1
        
        while queue and idx < len(values):
            node = queue.popleft()
            
            if idx < len(values) and values[idx] is not None:
                node.left = TreeNode(values[idx])
                queue.append(node.left)
            idx += 1
            
            if idx < len(values) and values[idx] is not None:
                node.right = TreeNode(values[idx])
                queue.append(node.right)
            idx += 1
        
        return root
