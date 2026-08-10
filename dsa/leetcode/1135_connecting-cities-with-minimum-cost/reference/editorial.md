
## Solution

---

### Approach 1: Minimum Spanning Tree (Using Kruskal's algorithm)

**Intuition**

If we model the cities and connections as a graph, each connection is an edge (undirected) and each city is a node of the graph. We need to find a subset of edges which connects all the nodes of the graph with the minimum possible total weight. This is by definition the Minimum Spanning Tree or [MST](https://en.wikipedia.org/wiki/Minimum_spanning_tree) of a graph.

**Algorithm**

There are a [variety of algorithms](https://en.wikipedia.org/wiki/Minimum_spanning_tree#Algorithms) that we can use to obtain the MST of a graph. We will use Kruskal's algorithm here, which is implemented using the [Disjoint set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) Union-Find data structure.

In order to obtain the MST using Kruskal's algorithm, we first sort all the connections (edges) present in the graph based on their weights (in increasing order) and will iterate over them one by one. The objective here is to greedily pick edges that will help us to connect more nodes in the graph. Each time we find a new edge which *does not* result in a cycle with the edges selected so far, we add that edge in the final MST. We keep doing this till we have obtained the MST which connects all the nodes in the graph (i.e. connects all the cities using the connections).

Disjoint-set union find can be implemented in a couple of ways. A plain union find is shown below which keeps the track of the parent of each node (initially parent of `i` is set to itself, i.e. `i`) and performs the union and find using a helper method `getRoot`.

```cpp
/** Vanilla Disjoint-set Union Find **/
class DisjointSet {
private:
    vector<int> parents;

public:
    void Union(int a, int b) {
        int rootA = Find(a);
        int rootB = Find(b);
        // If both a and b have same root, i.e. they both belong to the same set, hence we don't need to take union
        if (rootA == rootB) return;
        // Take union by assigning rootA as the parent of rootB
        this->parents[rootB] = rootA;
    }

    int Find(int a) {
        // Traverse all the way to the top (root) going through the parent nodes
        while (a != this->parents[a]) {
            a = this->parents[a];
        }
        return a;
    }

    bool isInSameGroup(int a, int b) {
        // Return true if both a and b belong to the same set, otherwise return false
        return Find(a) == Find(b);
    }

    DisjointSet(int N) {
        this->parents.resize(N + 1);
        // Set the initial parent node to itself
        for (int i = 1; i <= N; ++i) {
            this->parents[i] = i;
        }
    }
};
```

The above implementation can be made faster by incorporating **Path compression**. Here, while obtaining the root, we compress the path by assigning the grandparent of the node as the parent (thereby skipping connections and moving nodes closer to the root). We modify the `Find` method to implement path compression.

```cpp
int Find(int a) {
    while (a != this->parents[a]) {
        // Path compression
        // a's grandparent is now a's parent
        this->parents[a] = this->parents[parents[a]];
        a = this->parents[a];
    }
    return a;
}
```

This can be made even faster using a technique known as **Weighted Union**. In this technique, in addition to the parent nodes, we also keep the weights of each of the nodes. Every time we take union, the root node with more weight (i.e. having more elements in the corresponding set) is used as the parent node of the other node. We initialize the weight corresponding to each node as 1 initially, as each element belongs to it's own set in the beginning. Below is the implementation of this idea (we modify `Union` method).

```cpp
class DisjointSet {
private:

    vector<int> parents;
    vector<int> weights;

public:

    void Union(int a, int b) {
        int rootA = Find(a);
        int rootB = Find(b);
        // If both a and b have same root, i.e. they both belong to the same set, hence we don't need to take union
        if (rootA == rootB) return;

        // Weighted union
        if (this->weights[rootA] > this->weights[rootB]) {
            // In case rootA is having more weight
            // 1. Make rootA as the parent of rootB
            // 2. Increment the weight of rootA by rootB's weight
            this->parents[rootB] = rootA;
            this->weights[rootA] += this->weights[rootB];
        } else {
            // Otherwise
            // 1. Make rootB as the parent of rootA
            // 2. Increment the weight of rootB by rootA's weight
            this->parents[rootA] = rootB;
            this->weights[rootB] += this->weights[rootA];
        }
    }

    DisjointSet(int N) {
        this->weights.resize(N + 1);
        this->parents.resize(N + 1);
        // 1. Set the initial weights to 1
        // 2. Set the initial parent node to itself
        for (int i = 1; i <= N; ++i) {
            this->weights[i] = 1;
            this->parents[i] = i;
        }
    }
};
```

If we combine both **Path compression** and **Weighted Union**, it takes $\log^{\ast} N$ for the union and find operations in case of Disjoint-set union [link](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Proof_of_O(log*(n))_time_complexity_of_Union-Find).
Here $\log^{\ast} N$ is an extremely slow-growing inverse Ackermann function a.k.a [Iterated logarithm](https://en.wikipedia.org/wiki/Iterated_logarithm) and practically does not exceed 5. Hence it can be treated as a constant for implementation purposes.

We can combine all the concepts we have seen above in order to implement Kruskal's algorithm for obtaining MST of a graph. Below is the implementation of this.

```cpp
class DisjointSet {
private:
    vector<int> weights; // Used to store weights of each nodes
    vector<int> parents;

public:
    void Union(int a, int b) {
        int rootA = Find(a);
        int rootB = Find(b);
        // If both a and b have same root, i.e. they both belong to the same set, hence we don't need to take union
        if (rootA == rootB) return;

        // Weighted union
        if (this->weights[rootA] > this->weights[rootB]) {
            // In case rootA is having more weight
            // 1. Make rootA as the parent of rootB
            // 2. Increment the weight of rootA by rootB's weight
            this->parents[rootB] = rootA;
            this->weights[rootA] += this->weights[rootB];
        } else {
            // Otherwise
            // 1. Make rootB as the parent of rootA
            // 2. Increment the weight of rootB by rootA's weight
            this->parents[rootA] = rootB;
            this->weights[rootB] += this->weights[rootA];
        }
    }

    int Find(int a) {
        // Traverse all the way to the top (root) going through the parent nodes
        while (a != this->parents[a]) {
            // Path compression
            // a's grandparent is now a's parent
            this->parents[a] = this->parents[parents[a]];
            a = this->parents[a];
        }
        return a;
    }

    bool isInSameGroup(int a, int b) {
        // Return true if both a and b belong to the same set, otherwise return false
        return Find(a) == Find(b);
    }

    // Initialize weight for each node to be 1
    DisjointSet(int N) {
        this->parents.resize(N + 1);
        this->weights.resize(N + 1);
        // Set the initial parent node to itself
        for (int i = 1; i <= N; ++i) {
            this->parents[i] = i;
            this->weights[i] = 1;
        }
    }
};

class Solution {
public:
    int minimumCost(int N, vector<vector<int>>& connections) {
        DisjointSet *disjointset = new DisjointSet(N);
        // Sort connections based on their weights (in increasing order)
        sort(connections.begin(), connections.end(),
            [](const vector<int> &a, const vector<int> &b) {
                return a[2] < b[2];
            });
        // Keep track of total edges added in the MST
        int total = 0;
        // Keep track of the total cost of adding all those edges
        int cost = 0;
        for (int i = 0; i < connections.size(); ++i) {
            int a = connections[i][0];
            int b = connections[i][1];
            // Do not add the edge from a to b if it is already connected
            if (disjointset->isInSameGroup(a, b)) continue;
            // If a and b are not connected, take union
            disjointset->Union(a, b);
            // increment cost
            cost += connections[i][2];
            // increment number of edges added in the MST
            total++;
        }
        // If all N nodes are connected, the MST will have a total of N - 1 edges
        if (total == N - 1) {
            return cost;
        } else {
            return -1;
        }
    }
};
```

**Complexity Analysis**

* Time complexity: Assuming $N$ to be the total number of nodes (cities) and $M$ to be the total number of edges (connections). Sorting all the $M$ connections will take $O(M \cdot \log M)$. Performing union find each time will take $\log^{\ast} N$ (Iterated logarithm). Hence for M edges, it's $O(M \cdot \log^{\ast} N)$ which is practically $O(M)$ as the value of iterated logarithm, $\log^{\ast} N$ never exceeds 5.

* Space complexity: $\mathcal{O}(N)$, space required by `parents` and `weights`.