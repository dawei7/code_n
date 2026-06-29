# Graphs - Clone a graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP50 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Graphs |
| Official Link | [PREP50](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_12/problems/PREP50) |

---

## Problem Statement

You are given the root of an [undirected graph](https://mathinsight.org/definition/undirected_graph#:~:text=An%20undirected%20graph%20is%20graph,is%20called%20a%20directed%20graph) having a single connected component. Each node in the graph contains a value and a list of neighbours.

Your task is to clone the given graph. The function takes one argument, the root of the undirected graph, and you are expected to return the root of the clone graph.

**Note:** After you will return the node of the cloned graph, the system will automatically checks if the cloned graph is correct or not. It will output $1$ if the output graph is perfectly cloned, else, it will print $0$.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node cloneGraph(Node root){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* cloneGraph(Node* root){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def cloneGraph(root):
```

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains multiple lines of input.
- First line contains one space-separated integer $N$, the number of nodes in the graph.
- The next $N$ lines contain neighbors of the $i^{th}$ node as a list starting from $0$.

---

## Output Format

The function you complete should return the required answer.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 5\cdot 10^4$
- $0 \leq u_i, v_i\leq N-1$

---

## Examples

**Example 1**

**Input**

```text
3
3
1
0 2
1
3
1 2
0
0
3
1 2
0 2
0 1
```

**Output**

```text
1
1
1
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1
0 2
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
1 2
0
0
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
1 2
0 2
0 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

We are given a root of an undirected graph. We have to clone that graph and return the root of the clone graph

## [](#approach-2)Approach

We iterate through the graph the create a new node for each node and call the function for all it’s children. The function returns the pointer to the new node it just cloned, which is pushed into the neighbors array of the parent node.

## [](#code-3)Code
``class Solution {
public:
    map<Node*, bool> vis;
    Node* cloneGraph(Node* node) {
        if(node==nullptr) return nullptr;
        vis[node] = true;
        Node* curnode = new Node(node->val);
        for(auto i: node->neighbors){
            if(!vis[i])
            curnode->neighbors.push_back(cloneGraph(i));
        }
        return curnode;
    }
};
``

</details>
