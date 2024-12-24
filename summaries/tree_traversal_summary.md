# Tree Traversal Code Samples

Date: 12/8/2024
Yilin Zhao

## Recursive Traversal

<details>
<summary>Recursive-preorder traversal</summary>

### Explanation

```python
class Solution:
    def preorderTraversal(self, root):
        res=[]

        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        #call the dfs function
        dfs(root)

        #return the result
        return res
```

**Notes**
It start with, why we call return, if ndoe is None? Don't we need to return some value?

No, we don't need to return value, because this function is the worker of the array ```res```, so that the content in array is being dynamically modified while the dfs works! So return there means: I am ready, just return. The value is in the res, I won't return but you can access it!


</details>



<details>
<summary>Recursive-inorder traversal</summary>

### Explanation

```python
class Solution:
    def preorderTraversal(self, root):
        res=[]

        def dfs(node):
            if node is None:
                return


            #Some variations here--so, the key is the location of res.append(node.val)
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        #call the dfs function
        dfs(root)

        #return the result
        return res
```

**Notes**
Some variations in the middle block, we call dfs(node.left), then res.append(node.val), then dfs(node.right)


</details>


<details>
<summary>Recursive-postorder traversal</summary>

### Explanation

```python
class Solution:
    def preorderTraversal(self, root):
        res=[]

        def dfs(node):
            if node is None:
                #since the value are written to res[], we directly return here!
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        #call the main function
        dfs(root)
        return res
```

**Notes**
Some variations in the middle block, we call dfs(node.left), then res.append(node.val), then dfs(node.right)


</details>





## Iterative Traversal

<details>
<summary>Iterative-preorder traversal</summary>

### Explanation

```python
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        
        stack=[root]
        result=[]

        while stack:
            node=stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return result
```

**Notes**
The key here is we intialized a stack! We put any "pending" nodes onto that stack, and pop them out, and append them into array. The key is that we start with the middle nodes first, then start with the left, and right for preorder traversal. This sequence is same for the recursive version of dfs!


</details>



<details>
<summary>Iterative-inorder traversal</summary>

### Explanation

```python
# 中序遍历-迭代-LC94_二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result
```

**Notes**
I don't quite understand this one very much yet.

</details>


<details>
<summary>Recursive-postorder traversal</summary>

### Explanation

```python
# 后序遍历-迭代-LC145_二叉树的后序遍历
class Solution:
   def postorderTraversal(self, root: TreeNode) -> List[int]:
       if not root:
           return []
       stack = [root]
       result = []
       while stack:
           node = stack.pop()
           # 中结点先处理
           result.append(node.val)
           # 左孩子先入栈
           if node.left:
               stack.append(node.left)
           # 右孩子后入栈
           if node.right:
               stack.append(node.right)
       # 将最终的数组翻转
       return result[::-1]
```

**Notes**
Need to review this one.

</details>



## Level Order Traversal

<details>
<summary>Level Order Traversal (Using Length of queue)</summary>

### Explanation

```python
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue=collections.deque([root])
        result=[]

        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            result.append(level)
        
        return result
```

**Notes**
NULL

</details>


<details>
<summary>Iterative Level Order traversal</summary>

### Explanation

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        def traverse(node, level):
            if not node:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return levels
```

**Notes**
Need to review this one.

</details>

## Depth First Search


<details>
<summary>Depth First Search (Stack)</summary>

### Explanation

```python
def dfs_recursive(node):
    """
    Recursive DFS for a binary tree.
    
    :param node: Current TreeNode being visited
    """
    if not node:
        return
    
    print(node.value)  # Process the current node (e.g., print or some operation)
    
    dfs_recursive(node.left)   # Visit left subtree
    dfs_recursive(node.right)  # Visit right subtree
```

**Notes**
Need to review this one.

</details>