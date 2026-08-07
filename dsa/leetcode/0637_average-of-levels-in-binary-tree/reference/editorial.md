[TOC]

## Solution

---
### Approach #1 Using Depth First Search [Accepted]

**Algorithm**

One of the methods to solve the given problem is to make use of Depth First Search. In DFS, we try to exhaust each branch of the given tree during the tree traversal before moving onto the next branch.

To make use of DFS to solve the given problem, we make use of two lists $count$ and $res$. Here, $\text{count}[i]$ refers to the total number of nodes found at the $i^{th}$ level(counting from root at level 0) till now, and $\text{res}[i]$ refers to the sum of the nodes at the $i^{th}$ level encountered till now during the Depth First Search.

We make use of a function `average(t, i, res, count)`, which is used to fill the $res$ and $count$ array if we start the DFS from the node $t$ at the $i^{th}$ level in the given tree. We start by making the function call `average(root, 0, res, count)`. After this, we do the following at every step:

1. Add the value of the current node to the $res$(or $sum$) at the index corresponding to the current level. Also, increment the $count$ at the index corresponding to the current level.

2. Call the same function, `average`, with the left and the right child of the current node. Also, update the current level used in making the function call.

3. Repeat the above steps till all the nodes in the given tree have been considered once.

4. Populate the averages in the resultant array to be returned.

The following animation illustrates the process.

![Slide 1](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide1.PNG)

![Slide 2](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide2.PNG)

![Slide 3](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide3.PNG)

![Slide 4](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide4.PNG)

![Slide 5](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide5.PNG)

![Slide 6](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide6.PNG)

![Slide 7](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide7.PNG)

![Slide 8](images/slideshow_637_Avg_of_Levels_DFS_637_Avg_of_Levels_DFSSlide8.PNG)

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
    public List < Double > averageOfLevels(TreeNode root) {
        List < Integer > count = new ArrayList < > ();
        List < Double > res = new ArrayList < > ();
        average(root, 0, res, count);
        for (int i = 0; i < res.size(); i++)
            res.set(i, res.get(i) / count.get(i));
        return res;
    }
    public void average(TreeNode t, int i, List < Double > sum, List < Integer > count) {
        if (t == null)
            return;
        if (i < sum.size()) {
            sum.set(i, sum.get(i) + t.val);
            count.set(i, count.get(i) + 1);
        } else {
            sum.add(1.0 * t.val);
            count.add(1);
        }
        average(t.left, i + 1, sum, count);
        average(t.right, i + 1, sum, count);
    }
}

```

**Complexity Analysis**

* Time complexity : $O(n)$. The whole tree is traversed once only. Here, $n$ refers to the total number of nodes in the given binary tree.

* Space complexity : $O(h)$. $res$ and $count$ array of size $h$ are used. Here, $h$ refers to the height(maximum number of levels) of the given binary tree. Further, the depth of the recursive tree could go upto $h$ only.

---
### Approach #2 Breadth First Search [Accepted]

**Algorithm**

Another method to solve the given problem is to make use of a Breadth First Search. In BFS, we start by pushing the root node into a $queue$. Then, we remove an element(node) from the front of the $queue$. For every node removed from the $queue$, we add all its children to the back of the same $queue$. We keep on continuing this process till the $queue$ becomes empty. In this way, we can traverse the given tree on a level-by-level basis.

But, in the current implementation, we need to do a slight modification, since we need to separate the nodes on one level from that of the other.

The steps to be performed are listed below:

1. Put the root node into the $queue$.

2. Initialize $sum$ and $count$ as 0 and $temp$ as an empty queue.

3. Pop a node from the front of the $queue$. Add this node's value to the $sum$ corresponding to the current level. Also, update the $count$ corresponding to the current level.

4. Put the children nodes of the node last popped into the a $temp$ queue(instead of $queue$).

5. Continue steps 3 and 4 till $queue$ becomes empty. (An empty $queue$ indicates that one level of the tree has been considered).

6. Reinitialize $queue$ with its value as $temp$.

7. Populate the $res$ array with the average corresponding to the current level.

8. Repeat steps 2 to 7 till the $queue$ and $temp$ become empty.

At the end, $res$ is the required result.

The following animation illustrates the process.

![Slide 1](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide1.PNG)

![Slide 2](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide2.PNG)

![Slide 3](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide3.PNG)

![Slide 4](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide4.PNG)

![Slide 5](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide5.PNG)

![Slide 6](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide6.PNG)

![Slide 7](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide7.PNG)

![Slide 8](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide8.PNG)

![Slide 9](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide9.PNG)

![Slide 10](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide10.PNG)

![Slide 11](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide11.PNG)

![Slide 12](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide12.PNG)

![Slide 13](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide13.PNG)

![Slide 14](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide14.PNG)

![Slide 15](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide15.PNG)

![Slide 16](images/slideshow_637_Average_Of_Levels_637_Average_Of_LevelsSlide16.PNG)

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
    public List < Double > averageOfLevels(TreeNode root) {
        List < Double > res = new ArrayList < > ();
        Queue < TreeNode > queue = new LinkedList < > ();
        queue.add(root);
        while (!queue.isEmpty()) {
            long sum = 0, count = 0;
            Queue < TreeNode > temp = new LinkedList < > ();
            while (!queue.isEmpty()) {
                TreeNode n = queue.remove();
                sum += n.val;
                count++;
                if (n.left != null)
                    temp.add(n.left);
                if (n.right != null)
                    temp.add(n.right);
            }
            queue = temp;
            res.add(sum * 1.0 / count);
        }
        return res;
    }
}

```

**Complexity Analysis**

* Time complexity : $O(n)$. The whole tree is traversed at most once. Here, $n$ refers to the number of nodes in the given binary tree.

* Space complexity : $O(m)$. The size of $queue$ or $temp$ can grow upto at most the maximum number of nodes at any level in the given binary tree. Here, $m$ refers to the maximum mumber of nodes at any level in the input tree.