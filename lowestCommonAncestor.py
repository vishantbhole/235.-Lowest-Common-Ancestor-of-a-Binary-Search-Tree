
# 235. Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

# Helper function to build a binary tree from a list (BFS style)
def buildTree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


# Helper function to find a node with a given value
def findNode(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return findNode(root.left, val)
    else:
        return findNode(root.right, val)

if __name__ == "__main__":
    sol = Solution()

    # Example tree: [6,2,8,0,4,7,9,None,None,3,5]
    root = buildTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    p = findNode(root, 2)
    q = findNode(root, 4)
    ans = sol.lowestCommonAncestor(root, p, q)
    print("LCA of 2 and 4:", ans.val if ans else None)
