# cOde(n) Algorithms — Difficulty & Relevance

| Category | ID | Name | Complexity | Existing d | My d | My r |
|---|---|---|---|---:|---:|---:|
| **approximation** | | | | | | |
|  | `approx_01` | Vertex Cover (2-Approx) | O(n²) | 5 | **5** | **1** |
|  | `approx_02` | Set Cover (Greedy) | O(n²) | 4 | **5** | **2** |
|  | `approx_03` | TSP via MST (2-Approx) | O(n²) | 5 | **5** | **1** |
|  | `approx_04` | Christofides TSP (3/2-Approx) | O(n³) | 7 | **7** | **1** |
|  | `approx_05` | Fractional Knapsack (Greedy) | O(n log n) | 3 | **5** | **1** |
|  | `approx_06` | Bin Packing (First-Fit Decreasing) | O(n log n) | 4 | **5** | **1** |
|  | `approx_07` | 0/1 Knapsack FPTAS | O(n³) | 7 | **7** | **1** |
| **backtracking** | | | | | | |
|  | `backtrack_01` | Subset Sum (Decision) | O(2ⁿ) | 5 | **5** | **6** |
|  | `backtrack_02` | Permutations | O(2ⁿ) | 4 | **5** | **6** |
|  | `backtrack_03` | Combination Sum | O(2ⁿ) | 5 | **5** | **6** |
|  | `backtrack_04` | Word Break (Decision) | O(2ⁿ) | 5 | **5** | **6** |
|  | `backtrack_05` | Rat in a Maze | O(2ⁿ) | 4 | **5** | **6** |
|  | `backtrack_06` | Knight's Tour | O(2ⁿ) | 6 | **5** | **6** |
| **bit_manipulation** | | | | | | |
|  | `bit_01` | Count Set Bits | O(n) | 2 | **3** | **7** |
|  | `bit_02` | Power of Two Check | O(1) | 1 | **1** | **7** |
|  | `bit_03` | Single Number (XOR) | O(n) | 3 | **3** | **7** |
|  | `bit_04` | Power Set | O(2ⁿ) | 3 | **3** | **7** |
|  | `bit_05` | Single Number III | O(n) | 4 | **3** | **7** |
|  | `bit_06` | Bit Flips to Convert | O(n) | 3 | **3** | **7** |
|  | `bit_07` | Swap Odd and Even Bits | O(1) | 3 | **2** | **7** |
|  | `bit_08` | Divide Without / | O(log n) | 4 | **3** | **7** |
|  | `bit_09` | Multiply Without * | O(log n) | 3 | **3** | **7** |
|  | `bit_10` | Missing Number | O(n) | 2 | **3** | **7** |
|  | `bit_11` | Bitwise AND of Range | O(log n) | 5 | **3** | **7** |
|  | `bit_12` | Reverse Bits | O(1) | 3 | **2** | **7** |
| **branch_and_bound** | | | | | | |
|  | `bb_01` | 0/1 Knapsack | O(2ⁿ) | 5 | **6** | **3** |
|  | `bb_02` | Job Assignment (Hungarian) | O(2ⁿ) | 6 | **6** | **2** |
|  | `bb_03` | 0/1 Knapsack (Least-Cost B&B) | O(2ⁿ) | 6 | **6** | **3** |
|  | `bb_04` | 8-Puzzle (Branch and Bound) | O(2ⁿ) | 6 | **6** | **3** |
|  | `bb_05` | N-Queen (Branch and Bound) | O(n²) | 5 | **6** | **3** |
|  | `bb_06` | TSP via Reduced Matrix (B&B) | O(n²) | 7 | **6** | **2** |
| **divide_conquer** | | | | | | |
|  | `dc_01` | Power (x to the n) | O(log n) | 3 | **5** | **6** |
|  | `dc_02` | Majority Element | O(n) | 3 | **5** | **6** |
|  | `dc_03` | Kth Smallest (Quickselect) | O(n) | 5 | **5** | **6** |
|  | `dc_04` | Karatsuba Multiplication | O(n log n) | 6 | **6** | **6** |
|  | `dc_05` | Closest Pair of Points | O(n²) | 6 | **5** | **6** |
|  | `dc_06` | Strassen Matrix Multiplication | O(n log n) | 7 | **7** | **5** |
|  | `dc_07` | Skyline Problem | O(n²) | 5 | **5** | **6** |
|  | `dc_08` | Count Inversions | O(n log n) | 4 | **5** | **6** |
|  | `dc_09` | Median of Two Sorted Arrays | O(log n) | 6 | **5** | **6** |
|  | `dc_10` | Floor Square Root | O(log n) | 3 | **5** | **6** |
|  | `dc_11` | Modular Exponentiation | O(log n) | 4 | **5** | **6** |
|  | `dc_12` | Tiling Problem (2 x N board) | O(n) | 4 | **5** | **6** |
|  | `dc_13` | Allocate Minimum Number of Pages | O(n log n) | 6 | **5** | **6** |
|  | `dc_14` | Staircase Search in Sorted 2D Matrix | O(n²) | 4 | **5** | **6** |
|  | `dc_15` | Convex Hull (Divide and Conquer) | O(n log n) | 6 | **5** | **6** |
|  | `dc_16` | Quickhull Convex Hull | O(n log n) | 6 | **5** | **6** |
|  | `dc_17` | Min and Max (D&C tournament) | O(n) | 3 | **5** | **6** |
|  | `dc_18` | Frequency in Limited Range (sorted array) | O(log n) | 4 | **5** | **6** |
|  | `dc_19` | Maximum Subarray Sum (Divide and Conquer) | O(n log n) | 5 | **5** | **6** |
| **dynamic** | | | | | | |
|  | `dp_01` | Fibonacci | O(n) | 3 | **5** | **9** |
|  | `dp_02` | Climbing Stairs | O(n) | 3 | **5** | **9** |
|  | `dp_03` | Knapsack | O(n²) | 6 | **5** | **9** |
|  | `dp_04` | Longest Common Subsequence | O(n²) | 6 | **5** | **9** |
|  | `dp_05` | Coin Change | O(n²) | 5 | **5** | **9** |
|  | `dp_06` | Subset Sum | O(n²) | 5 | **5** | **9** |
|  | `dp_07` | Longest Increasing Subsequence | O(n log n) | 5 | **5** | **9** |
|  | `dp_08` | Edit Distance | O(n²) | 6 | **5** | **9** |
|  | `dp_09` | Rod Cutting | O(n²) | 5 | **5** | **9** |
|  | `dp_10` | Unique Paths | O(n²) | 4 | **5** | **9** |
|  | `dp_11` | House Robber | O(n) | 3 | **5** | **9** |
|  | `dp_12` | Min Cost Path | O(n²) | 4 | **5** | **9** |
|  | `dp_13` | Matrix Chain Multiplication | O(n³) | 7 | **6** | **9** |
|  | `dp_14` | Palindromic Partitioning | O(n²) | 6 | **5** | **9** |
|  | `dp_15` | Word Break | O(n²) | 4 | **5** | **9** |
|  | `dp_16` | Egg Dropping | O(n³) | 7 | **5** | **8** |
|  | `dp_17` | Partition Equal Subset Sum | O(n²) | 5 | **5** | **9** |
|  | `dp_18` | Max Product Subarray | O(n) | 5 | **5** | **9** |
|  | `dp_19` | Longest Palindromic Subsequence | O(n²) | 5 | **5** | **9** |
|  | `dp_20` | Shortest Common Supersequence (Length) | O(n²) | 5 | **5** | **9** |
|  | `dp_21` | Boolean Parenthesization | O(n³) | 6 | **6** | **9** |
|  | `dp_22` | Egg Dropping | O(n²) | 6 | **5** | **8** |
|  | `dp_23` | Min Cost Climbing Stairs | O(n) | 3 | **5** | **9** |
|  | `dp_24` | Palindromic Partitioning (Min Cuts) | O(n²) | 6 | **5** | **9** |
|  | `dp_25` | Matrix Chain Multiplication | O(n³) | 6 | **6** | **9** |
|  | `dp_26` | Optimal Binary Search Tree | O(n³) | 7 | **6** | **9** |
|  | `dp_27` | Floyd-Warshall Path | O(n³) | 5 | **5** | **9** |
|  | `dp_28` | Bellman-Ford (SSSP) | O(n³) | 4 | **5** | **9** |
|  | `dp_29` | Longest Increasing Subsequence (Patience Sort) | O(n log n) | 4 | **5** | **9** |
|  | `dp_30` | Coin Change (Count Ways) | O(n²) | 3 | **5** | **9** |
| **fenwick** | | | | | | |
|  | `fenwick_01` | Build Fenwick Tree | O(n) | 3 | **4** | **4** |
|  | `fenwick_02` | Range Sum Query (BIT) | O(n log n) | 3 | **4** | **4** |
|  | `fenwick_03` | 2D Fenwick Tree (Sub-matrix Sum) | O(n) | 5 | **4** | **4** |
|  | `fenwick_04` | Range Update + Point Query (BIT) | O(n log n) | 4 | **4** | **4** |
|  | `fenwick_05` | Range Update + Range Query (BIT) | O(n log n) | 5 | **4** | **4** |
|  | `fenwick_06` | Count Inversions (BIT) | O(n log n) | 4 | **4** | **4** |
|  | `fenwick_07` | K-th Smallest (Order-Statistic BIT) | O(n log n) | 5 | **4** | **3** |
| **flow** | | | | | | |
|  | `flow_01` | Ford-Fulkerson Max Flow | O(2ⁿ) | 6 | **6** | **2** |
|  | `flow_02` | Edmonds-Karp | O(n³) | 6 | **6** | **2** |
|  | `flow_03` | Bipartite Matching | O(n³) | 6 | **6** | **2** |
|  | `flow_04` | Dinic's Max Flow | O(n²) | 6 | **6** | **2** |
|  | `flow_05` | Minimum s-t Cut | O(n²) | 5 | **6** | **2** |
|  | `flow_06` | Push-Relabel Max Flow | O(n³) | 7 | **7** | **1** |
| **geometric** | | | | | | |
|  | `geometric_01` | Closest Pair of Points | O(n²) | 6 | **5** | **2** |
|  | `geometric_02` | Convex Hull (Graham Scan) | O(n log n) | 6 | **5** | **2** |
|  | `geometric_03` | Line Segment Intersection | O(1) | 4 | **4** | **2** |
|  | `geometric_04` | Point in Polygon (Ray Casting) | O(n) | 4 | **5** | **2** |
|  | `geometric_05` | Convex Hull (Jarvis March) | O(n²) | 4 | **5** | **2** |
|  | `geometric_06` | Rectangle Overlap (Axis-Aligned) | O(1) | 2 | **4** | **2** |
|  | `geometric_07` | Max Points on Same Line | O(n²) | 5 | **5** | **2** |
| **graphs** | | | | | | |
|  | `graph_01` | Graph Representation | O(n) | 2 | **5** | **8** |
|  | `graph_02` | Breadth-First Search | O(n²) | 4 | **5** | **8** |
|  | `graph_03` | Depth-First Search | O(n²) | 4 | **5** | **8** |
|  | `graph_04` | Dijkstra | O(n²) | 6 | **5** | **8** |
|  | `graph_05` | Bellman-Ford | O(n³) | 6 | **5** | **8** |
|  | `graph_06` | Floyd-Warshall | O(n³) | 6 | **5** | **8** |
|  | `graph_07` | Topological Sort | O(n²) | 5 | **5** | **8** |
|  | `graph_08` | Kruskal's MST | O(n log n) | 6 | **5** | **8** |
|  | `graph_09` | Union-Find (DSU) | O(n) | 4 | **5** | **8** |
|  | `graph_10` | Prim's MST | O(n²) | 6 | **5** | **8** |
|  | `graph_11` | Cycle Detection | O(n²) | 4 | **5** | **8** |
|  | `graph_12` | Bipartite Check | O(n²) | 4 | **5** | **8** |
|  | `graph_13` | Articulation Points | O(n²) | 6 | **5** | **8** |
|  | `graph_14` | Bridges | O(n²) | 6 | **5** | **8** |
|  | `graph_15` | Tarjan's SCC | O(n²) | 6 | **5** | **8** |
|  | `graph_16` | Kosaraju's SCC | O(n²) | 6 | **5** | **8** |
|  | `graph_17` | 0-1 BFS | O(n²) | 5 | **5** | **8** |
|  | `graph_18` | A* Search | O(n²) | 6 | **5** | **8** |
|  | `graph_19` | M-Coloring Problem | O(2ⁿ) | 5 | **5** | **8** |
|  | `graph_20` | Travelling Salesman (Held-Karp DP) | O(2ⁿ) | 7 | **6** | **8** |
|  | `graph_21` | Hamiltonian Path Existence | O(2ⁿ) | 6 | **5** | **8** |
| **greedy** | | | | | | |
|  | `greedy_01` | Activity Selection | O(n log n) | 4 | **4** | **7** |
|  | `greedy_02` | Fractional Knapsack | O(n log n) | 4 | **4** | **6** |
|  | `greedy_03` | Huffman Coding | O(n log n) | 5 | **4** | **6** |
|  | `greedy_04` | Job Sequencing | O(n²) | 5 | **4** | **7** |
|  | `greedy_05` | Optimal Merge Pattern | O(n log n) | 4 | **4** | **7** |
|  | `greedy_06` | Gas Station | O(n) | 4 | **4** | **7** |
|  | `greedy_07` | Jump Game | O(n) | 4 | **4** | **7** |
|  | `greedy_08` | Candy Distribution | O(n) | 5 | **4** | **7** |
|  | `greedy_09` | Lemonade Change | O(n) | 2 | **4** | **7** |
|  | `greedy_10` | Minimum Coins | O(n log n) | 3 | **4** | **7** |
|  | `greedy_11` | Egyptian Fraction | O(n²) | 4 | **4** | **7** |
|  | `greedy_12` | Max Trains for Stoppage | O(n log n) | 4 | **4** | **7** |
|  | `greedy_13` | Stable Marriage (Gale-Shapley) | O(n²) | 5 | **4** | **5** |
| **hashing** | | | | | | |
|  | `hash_01` | Two Sum | O(n) | 3 | **4** | **9** |
|  | `hash_02` | Subarray Sum Equals K | O(n) | 5 | **4** | **9** |
|  | `hash_03` | Longest Substring Without Repeating | O(n) | 4 | **4** | **9** |
|  | `hash_04` | Group Anagrams | O(n log n) | 4 | **4** | **9** |
|  | `hash_05` | Count Distinct in Window | O(n) | 4 | **4** | **9** |
|  | `hash_06` | Longest Consecutive Sequence | O(n log n) | 4 | **4** | **9** |
| **heap** | | | | | | |
|  | `heap_01` | Build Max Heap | O(n) | 4 | **5** | **6** |
|  | `heap_02` | Kth Largest Element | O(n log n) | 5 | **5** | **6** |
|  | `heap_03` | Top K Frequent Elements | O(n log n) | 5 | **5** | **6** |
|  | `heap_04` | Median in a Stream | O(n log n) | 6 | **5** | **6** |
|  | `heap_05` | Sliding Window Maximum | O(n log n) | 5 | **5** | **6** |
|  | `heap_06` | Kth Smallest in Sorted Matrix | O(n²) | 5 | **5** | **6** |
| **intro** | | | | | | |
|  | `intro_01` | Hello Grid | O(n) | 1 | **1** | **1** |
| **linked_list** | | | | | | |
|  | `linked_list_01` | Reverse Linked List | O(n) | 2 | **3** | **7** |
|  | `linked_list_02` | Detect Cycle in Linked List | O(n) | 3 | **3** | **7** |
|  | `linked_list_03` | Merge Two Sorted Linked Lists | O(n) | 3 | **3** | **7** |
|  | `linked_list_04` | Find Middle of Linked List | O(n) | 2 | **3** | **7** |
|  | `linked_list_05` | Reverse in Groups of K | O(n) | 5 | **3** | **7** |
| **math** | | | | | | |
|  | `math_01` | GCD (Euclidean) | O(log n) | 2 | **4** | **5** |
|  | `math_02` | Sieve of Eratosthenes | O(n log n) | 3 | **4** | **5** |
|  | `math_03` | Modular Exponentiation | O(log n) | 4 | **4** | **5** |
|  | `math_04` | Karatsuba Multiplication | O(n log n) | 5 | **5** | **5** |
|  | `math_05` | Big Integer Add (Strings) | O(n) | 2 | **4** | **5** |
|  | `math_06` | Carmichael Function | O(n log n) | 5 | **5** | **4** |
|  | `math_07` | Extended Euclidean Algorithm | O(log n) | 4 | **4** | **5** |
|  | `math_08` | Modular Multiplicative Inverse | O(log n) | 4 | **4** | **5** |
|  | `math_09` | Miller-Rabin Primality Test | O(log n) | 5 | **5** | **4** |
|  | `math_10` | Euler Totient Function | O(n log n) | 3 | **4** | **4** |
| **queue** | | | | | | |
|  | `queue_01` | Implement Queue using Stacks | O(1) | 4 | **2** | **4** |
|  | `queue_02` | Implement Stack using Queues | O(1) | 4 | **2** | **4** |
|  | `queue_03` | Generate Binary Numbers (1 to n) | O(n) | 3 | **3** | **4** |
|  | `queue_04` | First Non-Repeating Character in a Stream | O(n) | 4 | **3** | **4** |
|  | `queue_05` | Circular Queue (Array-based) | O(1) | 3 | **2** | **4** |
| **randomized** | | | | | | |
|  | `randomized_01` | Randomized Quicksort | O(n log n) | 4 | **5** | **3** |
|  | `randomized_02` | Reservoir Sampling | O(n) | 5 | **5** | **3** |
|  | `randomized_03` | Fisher-Yates Shuffle | O(n) | 3 | **5** | **3** |
|  | `randomized_04` | Randomized Binary Search | O(log n) | 4 | **5** | **3** |
|  | `randomized_05` | Karger's Min-Cut (Monte Carlo) | O(n²) | 6 | **6** | **1** |
|  | `randomized_06` | Estimating Pi via Monte Carlo | O(n) | 2 | **5** | **1** |
|  | `randomized_07` | Freivald's Algorithm (Matrix Product Check) | O(n²) | 6 | **6** | **1** |
| **recursion** | | | | | | |
|  | `recursion_01` | Power Sum | O(log n) | 2 | **3** | **7** |
|  | `recursion_02` | Reverse String | O(n) | 2 | **3** | **7** |
|  | `recursion_03` | Print Subsequences | O(2ⁿ) | 4 | **3** | **7** |
|  | `recursion_04` | Tower of Hanoi | O(2ⁿ) | 3 | **3** | **7** |
| **searching** | | | | | | |
|  | `search_01` | Linear Search | O(n) | 1 | **3** | **8** |
|  | `search_02` | Binary Search | O(log n) | 3 | **3** | **8** |
|  | `search_03` | BFS Grid | O(n²) | 5 | **3** | **8** |
|  | `search_04` | DFS Grid | O(n²) | 4 | **3** | **8** |
|  | `search_05` | Ternary Search | O(log n) | 3 | **3** | **8** |
|  | `search_06` | Jump Search | O(log n) | 3 | **3** | **8** |
|  | `search_07` | Exponential Search | O(log n) | 4 | **3** | **8** |
|  | `search_08` | Interpolation Search | O(n) | 5 | **3** | **8** |
|  | `search_09` | Fibonacci Search | O(log n) | 4 | **3** | **8** |
|  | `search_10` | Sublist Search | O(n²) | 3 | **3** | **8** |
|  | `search_11` | Count Occurrences (Sorted) | O(log n) | 3 | **3** | **8** |
|  | `search_12` | Search in Rotated Sorted Array | O(log n) | 5 | **3** | **8** |
| **segment_tree** | | | | | | |
|  | `segtree_01` | Build Segment Tree | O(n) | 3 | **5** | **3** |
|  | `segtree_02` | Range Sum Query | O(log n) | 4 | **5** | **3** |
|  | `segtree_03` | Point Update | O(log n) | 3 | **5** | **3** |
|  | `segtree_04` | Range Minimum Query | O(log n) | 4 | **5** | **3** |
|  | `segtree_05` | Range Update with Lazy Propagation | O(n log n) | 6 | **5** | **3** |
|  | `segtree_06` | Range Min with Lazy Updates | O(n log n) | 7 | **5** | **3** |
| **sorting** | | | | | | |
|  | `sort_01` | Bubble Sort | O(n²) | 2 | **4** | **8** |
|  | `sort_02` | Selection Sort | O(n²) | 2 | **4** | **8** |
|  | `sort_03` | Insertion Sort | O(n²) | 3 | **4** | **8** |
|  | `sort_04` | Merge Sort | O(n log n) | 5 | **4** | **8** |
|  | `sort_05` | Quick Sort | O(n log n) | 5 | **4** | **8** |
|  | `sort_06` | Heap Sort | O(n log n) | 6 | **4** | **8** |
|  | `sort_07` | Counting Sort | O(n) | 4 | **4** | **8** |
|  | `sort_08` | Radix Sort | O(n) | 6 | **4** | **8** |
|  | `sort_09` | Bucket Sort | O(n) | 5 | **4** | **8** |
|  | `sort_10` | Shell Sort | O(n²) | 5 | **4** | **8** |
|  | `sort_11` | Cycle Sort | O(n²) | 5 | **4** | **8** |
|  | `sort_12` | Pancake Sort | O(n²) | 6 | **4** | **8** |
|  | `sort_13` | Tim Sort (Simplified) | O(n log n) | 5 | **4** | **8** |
|  | `sort_14` | Intro Sort (Simplified) | O(n log n) | 6 | **4** | **8** |
| **stack** | | | | | | |
|  | `stack_01` | Balanced Parentheses | O(n) | 2 | **4** | **7** |
|  | `stack_02` | Next Greater Element | O(n) | 4 | **4** | **7** |
|  | `stack_03` | Stock Span Problem | O(n) | 4 | **4** | **7** |
|  | `stack_04` | Largest Rectangle in Histogram | O(n) | 6 | **4** | **7** |
|  | `stack_05` | Min Stack | O(n) | 3 | **4** | **7** |
|  | `stack_06` | Trapping Rain Water | O(n) | 5 | **4** | **7** |
|  | `stack_07` | Infix to Postfix Conversion | O(n) | 4 | **4** | **7** |
|  | `stack_08` | Evaluate Reverse Polish Notation | O(n) | 3 | **4** | **7** |
| **strings** | | | | | | |
|  | `string_01` | Anagram Check | O(n) | 1 | **4** | **7** |
|  | `string_02` | Longest Palindromic Substring | O(n²) | 5 | **4** | **7** |
|  | `string_03` | KMP String Matching | O(n) | 7 | **4** | **7** |
|  | `string_04` | Naive Pattern Search | O(n²) | 3 | **4** | **7** |
|  | `string_05` | Longest Common Substring | O(n²) | 5 | **4** | **7** |
|  | `string_06` | Rabin-Karp | O(n) | 6 | **4** | **7** |
|  | `string_07` | Z-Algorithm | O(n) | 7 | **4** | **7** |
|  | `string_08` | Smallest Window | O(n²) | 7 | **4** | **7** |
|  | `string_09` | Run-Length Encoding | O(n) | 2 | **4** | **7** |
|  | `string_10` | Word Break (Strings) | O(n²) | 4 | **4** | **7** |
|  | `string_11` | Longest Common Substring | O(n²) | 4 | **4** | **7** |
|  | `string_12` | String to Integer (atoi) | O(n) | 3 | **4** | **7** |
|  | `string_13` | Z-Algorithm (Pattern Search) | O(n) | 5 | **4** | **7** |
|  | `string_14` | Longest Repeating Subsequence | O(n²) | 5 | **4** | **7** |
| **suffix_array** | | | | | | |
|  | `suffix_01` | Build Suffix Array | O(n²) | 4 | **5** | **2** |
|  | `suffix_02` | Pattern Search with Suffix Array | O(n log n) | 5 | **5** | **2** |
|  | `suffix_03` | LCP Array (Kasai's Algorithm) | O(n) | 5 | **5** | **1** |
|  | `suffix_04` | Count Distinct Substrings | O(n²) | 4 | **5** | **2** |
|  | `suffix_05` | Longest Repeated Substring | O(n²) | 3 | **5** | **2** |
| **trees** | | | | | | |
|  | `tree_01` | Preorder Traversal | O(n) | 3 | **4** | **8** |
|  | `tree_02` | Inorder Traversal | O(n) | 3 | **4** | **8** |
|  | `tree_03` | Postorder Traversal | O(n) | 3 | **4** | **8** |
|  | `tree_04` | Tree Height | O(n) | 2 | **4** | **8** |
|  | `tree_05` | Level-Order Traversal | O(n) | 3 | **4** | **8** |
|  | `tree_06` | BST Search | O(log n) | 3 | **4** | **8** |
|  | `tree_07` | Tree Diameter | O(n) | 4 | **4** | **8** |
|  | `tree_08` | BST Insert | O(log n) | 3 | **4** | **8** |
|  | `tree_09` | Mirror Tree | O(n) | 2 | **4** | **8** |
|  | `tree_10` | Max Path Sum | O(n) | 4 | **4** | **8** |
|  | `tree_11` | Balanced Tree Check | O(n) | 3 | **4** | **8** |
|  | `tree_12` | Symmetric Tree Check | O(n) | 3 | **4** | **8** |
|  | `tree_13` | Balanced Tree Check | O(n) | 3 | **4** | **8** |
|  | `tree_14` | Symmetric Tree Check | O(n) | 3 | **4** | **8** |
|  | `tree_15` | BST Delete | O(log n) | 5 | **4** | **8** |
|  | `tree_16` | Serialize / Deserialize | O(n) | 5 | **4** | **8** |
|  | `tree_17` | Lowest Common Ancestor | O(log n) | 4 | **4** | **8** |
|  | `tree_18` | Right Side View | O(n) | 3 | **4** | **8** |
|  | `tree_19` | Boundary Traversal | O(n) | 5 | **4** | **8** |
|  | `tree_20` | Binary Tree to BST | O(n log n) | 4 | **4** | **8** |
|  | `tree_21` | Root-to-Leaf Paths | O(n) | 3 | **4** | **8** |
|  | `tree_22` | AVL Insert (Simplified) | O(n log n) | 6 | **5** | **8** |
|  | `tree_23` | Kth Smallest in BST | O(n) | 2 | **4** | **8** |
| **trie** | | | | | | |
|  | `trie_01` | Trie Insert and Search | O(n) | 3 | **3** | **5** |
|  | `trie_02` | Word Count with Prefix | O(n) | 3 | **3** | **5** |
|  | `trie_03` | Longest Common Prefix | O(n) | 2 | **3** | **5** |
|  | `trie_04` | Delete Word from Trie | O(n) | 4 | **3** | **5** |

## Per-category summary

| Category | # | avg d (existing) | avg d (mine) | avg r (mine) |
|---|---:|---:|---:|---:|
| approximation | 7 | 5.0 | 5.6 | 1.1 |
| backtracking | 6 | 4.8 | 5.0 | 6.0 |
| bit_manipulation | 12 | 3.0 | 2.7 | 7.0 |
| branch_and_bound | 6 | 5.8 | 6.0 | 2.7 |
| divide_conquer | 19 | 4.7 | 5.2 | 5.9 |
| dynamic | 30 | 5.0 | 5.1 | 8.9 |
| fenwick | 7 | 4.1 | 4.0 | 3.9 |
| flow | 6 | 6.0 | 6.2 | 1.8 |
| geometric | 7 | 4.4 | 4.7 | 2.0 |
| graphs | 21 | 5.2 | 5.0 | 8.0 |
| greedy | 13 | 4.1 | 4.0 | 6.7 |
| hashing | 6 | 4.0 | 4.0 | 9.0 |
| heap | 6 | 5.0 | 5.0 | 6.0 |
| intro | 1 | 1.0 | 1.0 | 1.0 |
| linked_list | 5 | 3.0 | 3.0 | 7.0 |
| math | 10 | 3.7 | 4.3 | 4.7 |
| queue | 5 | 3.6 | 2.4 | 4.0 |
| randomized | 7 | 4.3 | 5.3 | 2.1 |
| recursion | 4 | 2.8 | 3.0 | 7.0 |
| searching | 12 | 3.6 | 3.0 | 8.0 |
| segment_tree | 6 | 4.5 | 5.0 | 3.0 |
| sorting | 14 | 4.6 | 4.0 | 8.0 |
| stack | 8 | 3.9 | 4.0 | 7.0 |
| strings | 14 | 4.6 | 4.0 | 7.0 |
| suffix_array | 5 | 4.2 | 5.0 | 1.8 |
| trees | 23 | 3.4 | 4.0 | 8.0 |
| trie | 4 | 3.0 | 3.0 | 5.0 |

## Where my difficulty disagrees with existing by >= 2

| ID | Category | Name | Existing | Mine | Reason |
|---|---|---|---:|---:|---|
| `approx_05` | approximation | Fractional Knapsack (Greedy) | 3 | 5 |  |
| `bit_11` | bit_manipulation | Bitwise AND of Range | 5 | 3 |  |
| `dc_01` | divide_conquer | Power (x to the n) | 3 | 5 |  |
| `dc_02` | divide_conquer | Majority Element | 3 | 5 |  |
| `dc_10` | divide_conquer | Floor Square Root | 3 | 5 |  |
| `dc_17` | divide_conquer | Min and Max (D&C tournament) | 3 | 5 |  |
| `dp_01` | dynamic | Fibonacci | 3 | 5 |  |
| `dp_02` | dynamic | Climbing Stairs | 3 | 5 |  |
| `dp_11` | dynamic | House Robber | 3 | 5 |  |
| `dp_16` | dynamic | Egg Dropping | 7 | 5 |  |
| `dp_23` | dynamic | Min Cost Climbing Stairs | 3 | 5 |  |
| `dp_30` | dynamic | Coin Change (Count Ways) | 3 | 5 |  |
| `geometric_06` | geometric | Rectangle Overlap (Axis-Aligned) | 2 | 4 |  |
| `graph_01` | graphs | Graph Representation | 2 | 5 |  |
| `greedy_09` | greedy | Lemonade Change | 2 | 4 |  |
| `linked_list_05` | linked_list | Reverse in Groups of K | 5 | 3 |  |
| `math_01` | math | GCD (Euclidean) | 2 | 4 |  |
| `math_05` | math | Big Integer Add (Strings) | 2 | 4 |  |
| `queue_01` | queue | Implement Queue using Stacks | 4 | 2 |  |
| `queue_02` | queue | Implement Stack using Queues | 4 | 2 |  |
| `randomized_03` | randomized | Fisher-Yates Shuffle | 3 | 5 |  |
| `randomized_06` | randomized | Estimating Pi via Monte Carlo | 2 | 5 |  |
| `search_01` | searching | Linear Search | 1 | 3 |  |
| `search_03` | searching | BFS Grid | 5 | 3 |  |
| `search_08` | searching | Interpolation Search | 5 | 3 |  |
| `search_12` | searching | Search in Rotated Sorted Array | 5 | 3 |  |
| `segtree_01` | segment_tree | Build Segment Tree | 3 | 5 |  |
| `segtree_03` | segment_tree | Point Update | 3 | 5 |  |
| `segtree_06` | segment_tree | Range Min with Lazy Updates | 7 | 5 |  |
| `sort_01` | sorting | Bubble Sort | 2 | 4 |  |
| `sort_02` | sorting | Selection Sort | 2 | 4 |  |
| `sort_06` | sorting | Heap Sort | 6 | 4 |  |
| `sort_08` | sorting | Radix Sort | 6 | 4 |  |
| `sort_12` | sorting | Pancake Sort | 6 | 4 |  |
| `sort_14` | sorting | Intro Sort (Simplified) | 6 | 4 |  |
| `stack_01` | stack | Balanced Parentheses | 2 | 4 |  |
| `stack_04` | stack | Largest Rectangle in Histogram | 6 | 4 |  |
| `string_01` | strings | Anagram Check | 1 | 4 |  |
| `string_03` | strings | KMP String Matching | 7 | 4 |  |
| `string_06` | strings | Rabin-Karp | 6 | 4 |  |
| `string_07` | strings | Z-Algorithm | 7 | 4 |  |
| `string_08` | strings | Smallest Window | 7 | 4 |  |
| `string_09` | strings | Run-Length Encoding | 2 | 4 |  |
| `suffix_05` | suffix_array | Longest Repeated Substring | 3 | 5 |  |
| `tree_04` | trees | Tree Height | 2 | 4 |  |
| `tree_09` | trees | Mirror Tree | 2 | 4 |  |
| `tree_23` | trees | Kth Smallest in BST | 2 | 4 |  |
