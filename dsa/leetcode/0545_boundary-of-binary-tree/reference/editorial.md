
## Solution

---
### Approach #1 Simple Solution [Accepted]

**Algorithm**

One simple approach is to divide this problem into three subproblems- left boundary, leaves and right boundary.

* Left Boundary: We keep on traversing the tree towards the left and keep on adding the nodes in the $res$ array, provided the current node isn't a leaf node. If at any point, we can't find the left child of a node, but its right child exists, we put the right child in the $res$ and continue the process. The following animation depicts the process.

<!--![Left_Boundary](images/545_Boundary_Left.gif)-->

![Slide 1](images/slideshow_545_Boundary_Of_Binary_Tree1_545_Boundary_Of_Binary_Tree1Slide1.JPG)

![Slide 2](images/slideshow_545_Boundary_Of_Binary_Tree1_545_Boundary_Of_Binary_Tree1Slide2.JPG)

![Slide 3](images/slideshow_545_Boundary_Of_Binary_Tree1_545_Boundary_Of_Binary_Tree1Slide3.JPG)

![Slide 4](images/slideshow_545_Boundary_Of_Binary_Tree1_545_Boundary_Of_Binary_Tree1Slide4.JPG)

![Slide 5](images/slideshow_545_Boundary_Of_Binary_Tree1_545_Boundary_Of_Binary_Tree1Slide5.JPG)

* Leaf Nodes: We make use of a recursive function `addLeaves(res,root)`, in which we change the root node for every recursive call. If the current root node happens to be a leaf node, it is added to the $res$ array. Otherwise, we make the recursive call using the left child of the current node as the new root. After this, we make the recursive call using the right child of the current node as the new root. The following animation depicts the process.

<!--![Leaf_Boundary](images/545_Boundary_Leaf.gif)-->

![Slide 1](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide7.JPG)

![Slide 2](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide8.JPG)

![Slide 3](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide9.JPG)

![Slide 4](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide10.JPG)

![Slide 5](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide11.JPG)

![Slide 6](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide12.JPG)

![Slide 7](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide13.JPG)

![Slide 8](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide14.JPG)

![Slide 9](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide15.JPG)

![Slide 10](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide16.JPG)

![Slide 11](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide17.JPG)

![Slide 12](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide18.JPG)

![Slide 13](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide19.JPG)

![Slide 14](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide20.JPG)

![Slide 15](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide21.JPG)

![Slide 16](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide22.JPG)

![Slide 17](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide23.JPG)

![Slide 18](images/slideshow_545_Boundary_Of_Binary_Tree2_545_Boundary_Of_Binary_Tree2Slide24.JPG)

* Right Boundary: We perform the same process as the left boundary. But, this time, we traverse towards the right. If the right child doesn't exist, we move towards the left child. Also, instead of putting the traversed nodes in the $res$ array, we push them over a stack during the traversal. After the complete traversal is done, we pop the element from over the stack and append them to the $res$ array. The following animation depicts the process.

<!--![Right_Boundary](images/545_Boundary_Right.gif)-->

![Slide 1](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide26.JPG)

![Slide 2](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide27.JPG)

![Slide 3](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide28.JPG)

![Slide 4](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide29.JPG)

![Slide 5](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide30.JPG)

![Slide 6](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide31.JPG)

![Slide 7](images/slideshow_545_Boundary_Of_Binary_Tree3_545_Boundary_Of_Binary_Tree3Slide32.JPG)

```java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {

    public boolean isLeaf(TreeNode t) {
        return t.left == null && t.right == null;
    }

    public void addLeaves(List<Integer> res, TreeNode root) {
        if (isLeaf(root)) {
            res.add(root.val);
        } else {
            if (root.left != null) {
                addLeaves(res, root.left);
            }
            if (root.right != null) {
                addLeaves(res, root.right);
            }
        }
    }

    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        if (!isLeaf(root)) {
            res.add(root.val);
        }
        TreeNode t = root.left;
        while (t != null) {
            if (!isLeaf(t)) {
                res.add(t.val);
            }
            if (t.left != null) {
                t = t.left;
            } else {
                t = t.right;
            }

        }
        addLeaves(res, root);
        Stack<Integer> s = new Stack<>();
        t = root.right;
        while (t != null) {
            if (!isLeaf(t)) {
                s.push(t.val);
            }
            if (t.right != null) {
                t = t.right;
            } else {
                t = t.left;
            }
        }
        while (!s.empty()) {
            res.add(s.pop());
        }
        return res;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$ One complete traversal for leaves and two traversals upto depth of binary tree for left and right boundary.

* Space complexity : $O(n)$ $res$ and $stack$ is used.

---

### Approach #2 Using PreOrder Traversal [Accepted]

**Algorithm**

Before we dive into this approach, let's look at the preorder traversal of a simple Binary Tree as shown below:

![Preorder Traversal](images/545_Preorder.png)

From the above figure, we can observe that our problem statement is very similar to the Preorder traversal. Actually, the order of traversal is the same(except for the right boundary nodes, for which it is the reverse), but we need to selectively include the nodes in the return result list. Thus, we need to include only those nodes in the result, which are either on the left boundary, the leaves or the right boundary.

In order to distinguish between the various kinds of nodes, we make use of a $flag$ as follows:

* Flag=0: Root Node.

* Flag=1: Left Boundary Node.

* Flag=2: Right Boundary Node.

* Flag=3: Others(Middle Node).

We make use of three lists $\text{left\\_boundary}$, $\text{right\\_boundary}$, $\text{leaves}$ to store the appropriate nodes and append the three lists at the end.

We go for the normal preorder traversal, but while calling the recursive function for preorder traversal using the left child or the right child of the current node, we also pass the $flag$ information indicating the type of node that the current child behaves like.

For obtaining the flag information about the left child of the current node, we make use of the function `leftChildFlag(node, flag)`. In the case of a left child, the following cases are possible, as can be verified by looking at the figure above:

* The current node is a left boundary node: In this case, the left child will always be a left boundary node. e.g. relationship between E & J in the above figure.

* The current node is a root node: In this case, the left child will always be a left boundary node. e.g. relationship between A & B in the above figure.

* The current node is a right boundary node: In this case, if the right child of the current node doesn't exist, the left child always acts as the right boundary node. e.g. G & N. But, if the right child exists, the left child always acts as the middle node. e.g. C & F.

Similarly, for obtaining the flag information about the right child of the current node, we make use of the function `rightChildFlag(node, flag)`. In the case of a right child, the following cases are possible, as can be verified by looking at the figure above:

* The current node is a right boundary node: In this case, the right child will always be a right boundary node. e.g. relationship between C & G in the above figure.

* The current node is a root node: In this case, the right child will always be a left boundary node. e.g. relationship between A & C in the above figure.

* The current node is a left boundary node: In this case, if the left child of the current node doesn't exist, the right child always acts as the left boundary node. e.g. B & E. But, if the left child exists, the left child always acts as the middle node.

Making use of the above information, we set the $flag$ appropriately, which is used to determine the list in which the current node has to be appended.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List < Integer > boundaryOfBinaryTree(TreeNode root) {
        List < Integer > left_boundary = new LinkedList < > (), right_boundary = new LinkedList < > (), leaves = new LinkedList < > ();
        preorder(root, left_boundary, right_boundary, leaves, 0);
        left_boundary.addAll(leaves);
        left_boundary.addAll(right_boundary);
        return left_boundary;
    }

    public boolean isLeaf(TreeNode cur) {
        return (cur.left == null && cur.right == null);
    }

    public boolean isRightBoundary(int flag) {
        return (flag == 2);
    }

    public boolean isLeftBoundary(int flag) {
        return (flag == 1);
    }

    public boolean isRoot(int flag) {
        return (flag == 0);
    }

    public int leftChildFlag(TreeNode cur, int flag) {
        if (isLeftBoundary(flag) || isRoot(flag))
            return 1;
        else if (isRightBoundary(flag) && cur.right == null)
            return 2;
        else return 3;
    }

    public int rightChildFlag(TreeNode cur, int flag) {
        if (isRightBoundary(flag) || isRoot(flag))
            return 2;
        else if (isLeftBoundary(flag) && cur.left == null)
            return 1;
        else return 3;
    }

    public void preorder(TreeNode cur, List < Integer > left_boundary, List < Integer > right_boundary, List < Integer > leaves, int flag) {
        if (cur == null)
            return;
        if (isRightBoundary(flag))
            right_boundary.add(0, cur.val);
        else if (isLeftBoundary(flag) || isRoot(flag))
            left_boundary.add(cur.val);
        else if (isLeaf(cur))
            leaves.add(cur.val);
        preorder(cur.left, left_boundary, right_boundary, leaves, leftChildFlag(cur, flag));
        preorder(cur.right, left_boundary, right_boundary, leaves, rightChildFlag(cur, flag));
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$ One complete traversal of the tree is done.

* Space complexity : $O(n)$ The recursive stack can grow upto a depth of $n$. Further, $\text{left\\_boundary}$, $\text{right\\_boundary}$ and $\text{leaves}$ combined together can be of size $n$.

---