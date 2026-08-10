## Solution Article

---

### Approach 1: DFS (Depth-First Search) with sorting

**Intuition**

The order in which the elements (nodes) will be collected in the final answer depends on the "height" of these nodes. The height of a node is the number of edges from the node to the deepest leaf. The nodes that are located in the i<sup>th</sup> height will be appear in the i<sup>th</sup> collection in the final answer. For any given node in the binary tree, the height is obtained by adding 1 to the maximum height of any children. Formally, for a given node of the binary tree $\text{root}$, it's height can be represented as

$\text{height(root)} = \text{1} + \text{max(height(root.left), height(root.right))}$

Where $\text{root.left}$ and $\text{root.right}$ are left and right children of the root respectively

**Algorithm**

In our first approach, we'll simply traverse the tree recursively in a depth first search manner using the function `int getHeight(node)`, which will return the height of the given node in the binary tree. Since height of any node depends on the height of it's children node, hence we traverse the tree in a post-order manner (i.e. height of the childrens are calculated first before calculating the height of the given node). Additionally, whenever we encounter a null node, we simply return -1 as it's height.

Next, we'll store the pair `(height, val)` for all the nodes which will be sorted later to obtain the final answer. The sorting will be done in increasing order considering the height first and then the val. Hence we'll obtain all the pairs in the increasing order of their height in the given binary tree.

Below is the implementaion of this approach

```cpp
class Solution {
public:

    vector<pair<int, int>> pairs;

    int getHeight(TreeNode *root) {

        // return -1 for null nodes
        if (!root) return -1;

        // first calculate the height of the left and right children
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);

        // based on the height of the left and right children, obtain the height of the current (parent) node
        int currHeight = max(leftHeight, rightHeight) + 1;

        // collect the pair -> (height, val)
        this->pairs.push_back({currHeight, root->val});

        // return the height of the current node
        return currHeight;
    }

    vector<vector<int>> findLeaves(TreeNode* root) {
        this->pairs.clear();

        getHeight(root);

        // sort all the (height, val) pairs
        sort(this->pairs.begin(), this->pairs.end());

        int n = this->pairs.size(), height = 0, i = 0;
        vector<vector<int>> solution;
        while (i < n) {
            vector<int> nums;
            while (i < n && this->pairs[i].first == height) {
                nums.push_back(this->pairs[i].second);
                i++;
            }
            solution.push_back(nums);
            height++;
        }
        return solution;
    }
};
```

**Complexity Analysis**

* Time Complexity: Assuming $N$ is the total number of nodes in the binary tree, traversing the tree takes $O(N)$ time. Sorting all the pairs based on their height takes $O(N \log N)$ time. Hence overall time complexity of this approach is $O(N \log N)$

* Space Complexity: $O(N)$, the space used by `pairs` and the recursion call stack during `getHeight`.

---

### Approach 2: DFS (Depth-First Search) without sorting

We've seen in approach 1 that there is an additional sorting that is being performed, which increases the overall time complexity to $O(N \log N)$. The question we can ask here is, can we do better than this? To answer this, we try to remove the sorting by directly placing all the values in their respective positions, i.e. instead of using the `pairs` array to collect all the `(height, val)` pairs and then sorting them based on their heights, we'll directly obtain the solution by placing each element (`val`) to its correct position in the solution array. To clarify, in the given binary tree, `[4, 3, 5]` goes into the first position, `[2]` goes into the second position and `[1]` goes into the third position in the solution array.

To do this, we modify our `getHeight` method to directly insert the node's value in the solution array at the correct location. Solution array is kept empty in the beginning and as we encounter elements with increasing height, we'll keep increasing the size of the solution array to accomodate for these elements. For example, if our solution array currently is `[[4, 3, 5]]` and if we want to insert 2 at the second position, we first create the space for 2 by increasing the size of the solution array by 1 and then insert 2 at it's correct location.

* $[[4, 3, 5]] -> [[4, 3, 5], []] # increase the size of solution array$

* $[[4, 3, 5], []] -> [[4, 3, 5], [2]] # insert 2 at it's correct location$

Below is the implementation of the above mentioned approach.

```cpp
class Solution {
private:

    vector<vector<int>> solution;

public:

    int getHeight(TreeNode *root) {

        // return -1 for null nodes
        if (!root) {
            return -1;
        }

        // first calculate the height of the left and right children
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);

        // based on the height of the left and right children, obtain the height of the current (parent) node
        int currHeight = max(leftHeight, rightHeight) + 1;

        // create space for node located at `currHeight` if not already exists
        if (this->solution.size() == currHeight) {
            this->solution.push_back({});
        }

        // insert the value at the correct position in the solution array
        this->solution[currHeight].push_back(root->val);

        // return the height of the current node
        return currHeight;
    }

    vector<vector<int>> findLeaves(TreeNode* root) {
        this->solution.clear();

        getHeight(root);

        return this->solution;
    }
};
```

**Complexity Analysis**

* Time Complexity: Assuming $N$ is the total number of nodes in the binary tree, traversing the tree takes $O(N)$ time and storing all the pairs at the correct position also takes $O(N)$ time. Hence overall time complexity of this approach is $O(N)$.

* Space Complexity: $O(N)$, the space used by the recursion call stack.
