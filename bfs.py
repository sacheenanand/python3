class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue =[root]
        next_q=[]
        level = []
        result =[]

        while queue!=[]:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_q.append(root.left)
                if root.right is not None:
                    next_q.append(root.right)
                result.append(level)
                level =[]
                queue = next_q
                next_q =[]
        return result


 class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        queue = [root] 
        next_q = []
        level = []
        result = []

        while queue!=[]:
            for root in queue:
                level.append(root.val) 
                if root.left is not None:
                    next_q.append(root.left)
                if root.right is not None:
                    next_q.append(root.right)
            result.append(level)
            level=[] 
            queue = next_q
            next_q=[]
        return result
    
# another method
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val) 
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
    


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []
        q = collections.deque()
        q.append(root)


        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        

        return result
            







                    



    



            

        
        



