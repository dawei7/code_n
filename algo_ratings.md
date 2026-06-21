# cOde(n) Algorithms — Difficulty & Relevance

| Category | ID | Name | Complexity | Existing d | My d | My r |
|---|---|---|---|---:|---:|---:|
| **approximation** | | | | | | |
|  | `approx_01` | Vertex Cover (2-Approx) | O(n²) | 5 | **5** | **1** |
|  | `approx_02` | Set Cover (Greedy) | O(n²) | 4 | **5** | **1** |
|  | `approx_03` | TSP via MST (2-Approx) | O(n²) | 5 | **5** | **1** |
|  | `approx_04` | Christofides TSP (3/2-Approx) | O(n³) | 7 | **9** | **1** |
|  | `approx_05` | Fractional Knapsack (Greedy) | O(n log n) | 3 | **3** | **3** |
|  | `approx_06` | Bin Packing (First-Fit Decreasing) | O(n log n) | 4 | **5** | **1** |
|  | `approx_07` | 0/1 Knapsack FPTAS | O(n³) | 7 | **9** | **1** |
| **backtracking** | | | | | | |
|  | `backtrack_01` | Subset Sum (Decision) | O(2ⁿ) | 5 | **5** | **7** |
|  | `backtrack_02` | Permutations | O(2ⁿ) | 4 | **4** | **8** |
|  | `backtrack_03` | Combination Sum | O(2ⁿ) | 5 | **5** | **8** |
|  | `backtrack_04` | Word Break (Decision) | O(2ⁿ) | 5 | **5** | **7** |
|  | `backtrack_05` | Rat in a Maze | O(2ⁿ) | 4 | **4** | **6** |
|  | `backtrack_06` | Knight's Tour | O(2ⁿ) | 6 | **6** | **3** |
| **bit_manipulation** | | | | | | |
|  | `bit_01` | Count Set Bits | O(n) | 2 | **2** | **6** |
|  | `bit_02` | Power of Two Check | O(1) | 1 | **1** | **6** |
|  | `bit_03` | Single Number (XOR) | O(n) | 3 | **2** | **7** |
|  | `bit_04` | Power Set | O(2ⁿ) | 3 | **3** | **8** |
|  | `bit_05` | Single Number III | O(n) | 4 | **3** | **5** |
|  | `bit_06` | Bit Flips to Convert | O(n) | 3 | **3** | **5** |
|  | `bit_07` | Swap Odd and Even Bits | O(1) | 3 | **2** | **5** |
|  | `bit_08` | Divide Without / | O(log n) | 4 | **3** | **5** |
|  | `bit_09` | Multiply Without * | O(log n) | 3 | **3** | **5** |
|  | `bit_10` | Missing Number | O(n) | 2 | **2** | **7** |
|  | `bit_11` | Bitwise AND of Range | O(log n) | 5 | **5** | **5** |
|  | `bit_12` | Reverse Bits | O(1) | 3 | **2** | **5** |
| **branch_and_bound** | | | | | | |
|  | `bb_01` | 0/1 Knapsack | O(2ⁿ) | 5 | **6** | **1** |
|  | `bb_02` | Job Assignment (Hungarian) | O(2ⁿ) | 6 | **8** | **1** |
|  | `bb_03` | 0/1 Knapsack (Least-Cost B&B) | O(2ⁿ) | 6 | **7** | **1** |
|  | `bb_04` | 8-Puzzle (Branch and Bound) | O(2ⁿ) | 6 | **7** | **1** |
|  | `bb_05` | N-Queen (Branch and Bound) | O(n²) | 5 | **6** | **1** |
|  | `bb_06` | TSP via Reduced Matrix (B&B) | O(n²) | 7 | **8** | **1** |
| **divide_conquer** | | | | | | |
|  | `dc_01` | Power (x to the n) | O(log n) | 3 | **3** | **8** |
|  | `dc_02` | Majority Element | O(n) | 3 | **3** | **8** |
|  | `dc_03` | Kth Smallest (Quickselect) | O(n) | 5 | **5** | **8** |
|  | `dc_04` | Karatsuba Multiplication | O(n log n) | 6 | **6** | **1** |
|  | `dc_05` | Closest Pair of Points | O(n²) | 6 | **6** | **2** |
|  | `dc_06` | Strassen Matrix Multiplication | O(n log n) | 7 | **7** | **1** |
|  | `dc_07` | Skyline Problem | O(n²) | 5 | **5** | **5** |
|  | `dc_08` | Count Inversions | O(n log n) | 4 | **5** | **5** |
|  | `dc_09` | Median of Two Sorted Arrays | O(log n) | 6 | **6** | **8** |
|  | `dc_10` | Floor Square Root | O(log n) | 3 | **3** | **8** |
|  | `dc_11` | Modular Exponentiation | O(log n) | 4 | **5** | **8** |
|  | `dc_12` | Tiling Problem (2 x N board) | O(n) | 4 | **5** | **5** |
|  | `dc_13` | Allocate Minimum Number of Pages | O(n log n) | 6 | **5** | **7** |
|  | `dc_14` | Staircase Search in Sorted 2D Matrix | O(n²) | 4 | **3** | **7** |
|  | `dc_15` | Convex Hull (Divide and Conquer) | O(n log n) | 6 | **6** | **1** |
|  | `dc_16` | Quickhull Convex Hull | O(n log n) | 6 | **6** | **1** |
|  | `dc_17` | Min and Max (D&C tournament) | O(n) | 3 | **3** | **3** |
|  | `dc_18` | Frequency in Limited Range (sorted array) | O(log n) | 4 | **5** | **5** |
|  | `dc_19` | Maximum Subarray Sum (Divide and Conquer) | O(n log n) | 5 | **4** | **8** |
| **dynamic** | | | | | | |
|  | `dp_01` | Fibonacci | O(n) | 3 | **2** | **9** |
|  | `dp_02` | Climbing Stairs | O(n) | 3 | **2** | **9** |
|  | `dp_03` | Knapsack | O(n²) | 6 | **5** | **8** |
|  | `dp_04` | Longest Common Subsequence | O(n²) | 6 | **5** | **8** |
|  | `dp_05` | Coin Change | O(n²) | 5 | **5** | **8** |
|  | `dp_06` | Subset Sum | O(n²) | 5 | **5** | **8** |
|  | `dp_07` | Longest Increasing Subsequence | O(n log n) | 5 | **5** | **8** |
|  | `dp_08` | Edit Distance | O(n²) | 6 | **5** | **8** |
|  | `dp_09` | Rod Cutting | O(n²) | 5 | **5** | **8** |
|  | `dp_10` | Unique Paths | O(n²) | 4 | **5** | **8** |
|  | `dp_11` | House Robber | O(n) | 3 | **3** | **9** |
|  | `dp_12` | Min Cost Path | O(n²) | 4 | **5** | **8** |
|  | `dp_13` | Matrix Chain Multiplication | O(n³) | 7 | **6** | **2** |
|  | `dp_14` | Palindromic Partitioning | O(n²) | 6 | **5** | **8** |
|  | `dp_15` | Word Break | O(n²) | 4 | **5** | **8** |
|  | `dp_16` | Egg Dropping | O(n³) | 7 | **6** | **2** |
|  | `dp_17` | Partition Equal Subset Sum | O(n²) | 5 | **5** | **8** |
|  | `dp_18` | Max Product Subarray | O(n) | 5 | **5** | **8** |
|  | `dp_19` | Longest Palindromic Subsequence | O(n²) | 5 | **5** | **8** |
|  | `dp_20` | Shortest Common Supersequence (Length) | O(n²) | 5 | **5** | **8** |
|  | `dp_21` | Boolean Parenthesization | O(n³) | 6 | **7** | **2** |
|  | `dp_22` | Egg Dropping | O(n²) | 6 | **7** | **2** |
|  | `dp_23` | Min Cost Climbing Stairs | O(n) | 3 | **2** | **9** |
|  | `dp_24` | Palindromic Partitioning (Min Cuts) | O(n²) | 6 | **5** | **8** |
|  | `dp_25` | Matrix Chain Multiplication | O(n³) | 6 | **6** | **2** |
|  | `dp_26` | Optimal Binary Search Tree | O(n³) | 7 | **7** | **2** |
|  | `dp_27` | Floyd-Warshall Path | O(n³) | 5 | **5** | **5** |
|  | `dp_28` | Bellman-Ford (SSSP) | O(n³) | 4 | **5** | **5** |
|  | `dp_29` | Longest Increasing Subsequence (Patience Sort) | O(n log n) | 4 | **6** | **4** |
|  | `dp_30` | Coin Change (Count Ways) | O(n²) | 3 | **4** | **8** |
| **fenwick** | | | | | | |
|  | `fenwick_01` | Build Fenwick Tree | O(n) | 3 | **4** | **1** |
|  | `fenwick_02` | Range Sum Query (BIT) | O(n log n) | 3 | **4** | **1** |
|  | `fenwick_03` | 2D Fenwick Tree (Sub-matrix Sum) | O(n) | 5 | **5** | **1** |
|  | `fenwick_04` | Range Update + Point Query (BIT) | O(n log n) | 4 | **5** | **1** |
|  | `fenwick_05` | Range Update + Range Query (BIT) | O(n log n) | 5 | **5** | **1** |
|  | `fenwick_06` | Count Inversions (BIT) | O(n log n) | 4 | **5** | **1** |
|  | `fenwick_07` | K-th Smallest (Order-Statistic BIT) | O(n log n) | 5 | **5** | **1** |
| **flow** | | | | | | |
|  | `flow_01` | Ford-Fulkerson Max Flow | O(2ⁿ) | 6 | **7** | **1** |
|  | `flow_02` | Edmonds-Karp | O(n³) | 6 | **7** | **1** |
|  | `flow_03` | Bipartite Matching | O(n³) | 6 | **7** | **1** |
|  | `flow_04` | Dinic's Max Flow | O(n²) | 6 | **8** | **1** |
|  | `flow_05` | Minimum s-t Cut | O(n²) | 5 | **7** | **1** |
|  | `flow_06` | Push-Relabel Max Flow | O(n³) | 7 | **9** | **1** |
| **geometric** | | | | | | |
|  | `geometric_01` | Closest Pair of Points | O(n²) | 6 | **5** | **1** |
|  | `geometric_02` | Convex Hull (Graham Scan) | O(n log n) | 6 | **5** | **1** |
|  | `geometric_03` | Line Segment Intersection | O(1) | 4 | **4** | **1** |
|  | `geometric_04` | Point in Polygon (Ray Casting) | O(n) | 4 | **5** | **1** |
|  | `geometric_05` | Convex Hull (Jarvis March) | O(n²) | 4 | **5** | **1** |
|  | `geometric_06` | Rectangle Overlap (Axis-Aligned) | O(1) | 2 | **2** | **6** |
|  | `geometric_07` | Max Points on Same Line | O(n²) | 5 | **5** | **1** |
| **graphs** | | | | | | |
|  | `graph_01` | Graph Representation | O(n) | 2 | **2** | **8** |
|  | `graph_02` | Breadth-First Search | O(n²) | 4 | **4** | **10** |
|  | `graph_03` | Depth-First Search | O(n²) | 4 | **4** | **10** |
|  | `graph_04` | Dijkstra | O(n²) | 6 | **5** | **8** |
|  | `graph_05` | Bellman-Ford | O(n³) | 6 | **5** | **5** |
|  | `graph_06` | Floyd-Warshall | O(n³) | 6 | **5** | **5** |
|  | `graph_07` | Topological Sort | O(n²) | 5 | **5** | **8** |
|  | `graph_08` | Kruskal's MST | O(n log n) | 6 | **5** | **5** |
|  | `graph_09` | Union-Find (DSU) | O(n) | 4 | **5** | **8** |
|  | `graph_10` | Prim's MST | O(n²) | 6 | **5** | **5** |
|  | `graph_11` | Cycle Detection | O(n²) | 4 | **5** | **8** |
|  | `graph_12` | Bipartite Check | O(n²) | 4 | **5** | **8** |
|  | `graph_13` | Articulation Points | O(n²) | 6 | **7** | **1** |
|  | `graph_14` | Bridges | O(n²) | 6 | **7** | **1** |
|  | `graph_15` | Tarjan's SCC | O(n²) | 6 | **7** | **1** |
|  | `graph_16` | Kosaraju's SCC | O(n²) | 6 | **6** | **1** |
|  | `graph_17` | 0-1 BFS | O(n²) | 5 | **5** | **8** |
|  | `graph_18` | A* Search | O(n²) | 6 | **5** | **8** |
|  | `graph_19` | M-Coloring Problem | O(2ⁿ) | 5 | **5** | **2** |
|  | `graph_20` | Travelling Salesman (Held-Karp DP) | O(2ⁿ) | 7 | **7** | **1** |
|  | `graph_21` | Hamiltonian Path Existence | O(2ⁿ) | 6 | **6** | **1** |
| **greedy** | | | | | | |
|  | `greedy_01` | Activity Selection | O(n log n) | 4 | **4** | **7** |
|  | `greedy_02` | Fractional Knapsack | O(n log n) | 4 | **3** | **3** |
|  | `greedy_03` | Huffman Coding | O(n log n) | 5 | **4** | **7** |
|  | `greedy_04` | Job Sequencing | O(n²) | 5 | **4** | **7** |
|  | `greedy_05` | Optimal Merge Pattern | O(n log n) | 4 | **4** | **7** |
|  | `greedy_06` | Gas Station | O(n) | 4 | **4** | **7** |
|  | `greedy_07` | Jump Game | O(n) | 4 | **4** | **7** |
|  | `greedy_08` | Candy Distribution | O(n) | 5 | **4** | **7** |
|  | `greedy_09` | Lemonade Change | O(n) | 2 | **2** | **7** |
|  | `greedy_10` | Minimum Coins | O(n log n) | 3 | **3** | **7** |
|  | `greedy_11` | Egyptian Fraction | O(n²) | 4 | **4** | **2** |
|  | `greedy_12` | Max Trains for Stoppage | O(n log n) | 4 | **4** | **7** |
|  | `greedy_13` | Stable Marriage (Gale-Shapley) | O(n²) | 5 | **4** | **7** |
| **hashing** | | | | | | |
|  | `hash_01` | Two Sum | O(n) | 3 | **2** | **10** |
|  | `hash_02` | Subarray Sum Equals K | O(n) | 5 | **4** | **10** |
|  | `hash_03` | Longest Substring Without Repeating | O(n) | 4 | **4** | **10** |
|  | `hash_04` | Group Anagrams | O(n log n) | 4 | **4** | **10** |
|  | `hash_05` | Count Distinct in Window | O(n) | 4 | **4** | **10** |
|  | `hash_06` | Longest Consecutive Sequence | O(n log n) | 4 | **4** | **10** |
| **heap** | | | | | | |
|  | `heap_01` | Build Max Heap | O(n) | 4 | **4** | **5** |
|  | `heap_02` | Kth Largest Element | O(n log n) | 5 | **4** | **7** |
|  | `heap_03` | Top K Frequent Elements | O(n log n) | 5 | **4** | **7** |
|  | `heap_04` | Median in a Stream | O(n log n) | 6 | **5** | **8** |
|  | `heap_05` | Sliding Window Maximum | O(n log n) | 5 | **5** | **8** |
|  | `heap_06` | Kth Smallest in Sorted Matrix | O(n²) | 5 | **4** | **7** |
| **linked_list** | | | | | | |
|  | `linked_list_01` | Reverse Linked List | O(n) | 2 | **2** | **10** |
|  | `linked_list_02` | Detect Cycle in Linked List | O(n) | 3 | **2** | **9** |
|  | `linked_list_03` | Merge Two Sorted Linked Lists | O(n) | 3 | **3** | **8** |
|  | `linked_list_04` | Find Middle of Linked List | O(n) | 2 | **2** | **9** |
|  | `linked_list_05` | Reverse in Groups of K | O(n) | 5 | **4** | **8** |
| **math** | | | | | | |
|  | `math_01` | GCD (Euclidean) | O(log n) | 2 | **2** | **4** |
|  | `math_02` | Sieve of Eratosthenes | O(n log n) | 3 | **3** | **3** |
|  | `math_03` | Modular Exponentiation | O(log n) | 4 | **4** | **5** |
|  | `math_04` | Karatsuba Multiplication | O(n log n) | 5 | **5** | **1** |
|  | `math_05` | Big Integer Add (Strings) | O(n) | 2 | **3** | **4** |
|  | `math_06` | Carmichael Function | O(n log n) | 5 | **5** | **1** |
|  | `math_07` | Extended Euclidean Algorithm | O(log n) | 4 | **4** | **2** |
|  | `math_08` | Modular Multiplicative Inverse | O(log n) | 4 | **4** | **2** |
|  | `math_09` | Miller-Rabin Primality Test | O(log n) | 5 | **7** | **1** |
|  | `math_10` | Euler Totient Function | O(n log n) | 3 | **4** | **1** |
| **queue** | | | | | | |
|  | `queue_01` | Implement Queue using Stacks | O(1) | 4 | **4** | **5** |
|  | `queue_02` | Implement Stack using Queues | O(1) | 4 | **4** | **5** |
|  | `queue_03` | Generate Binary Numbers (1 to n) | O(n) | 3 | **3** | **5** |
|  | `queue_04` | First Non-Repeating Character in a Stream | O(n) | 4 | **3** | **5** |
|  | `queue_05` | Circular Queue (Array-based) | O(1) | 3 | **2** | **5** |
| **randomized** | | | | | | |
|  | `randomized_01` | Randomized Quicksort | O(n log n) | 4 | **4** | **2** |
|  | `randomized_02` | Reservoir Sampling | O(n) | 5 | **4** | **2** |
|  | `randomized_03` | Fisher-Yates Shuffle | O(n) | 3 | **3** | **4** |
|  | `randomized_04` | Randomized Binary Search | O(log n) | 4 | **4** | **2** |
|  | `randomized_05` | Karger's Min-Cut (Monte Carlo) | O(n²) | 6 | **7** | **1** |
|  | `randomized_06` | Estimating Pi via Monte Carlo | O(n) | 2 | **1** | **2** |
|  | `randomized_07` | Freivald's Algorithm (Matrix Product Check) | O(n²) | 6 | **6** | **1** |
| **recursion** | | | | | | |
|  | `recursion_01` | Power Sum | O(log n) | 2 | **2** | **8** |
|  | `recursion_02` | Reverse String | O(n) | 2 | **1** | **8** |
|  | `recursion_03` | Print Subsequences | O(2ⁿ) | 4 | **3** | **8** |
|  | `recursion_04` | Tower of Hanoi | O(2ⁿ) | 3 | **3** | **4** |
| **searching** | | | | | | |
|  | `search_01` | Linear Search | O(n) | 1 | **1** | **8** |
|  | `search_02` | Binary Search | O(log n) | 3 | **2** | **10** |
|  | `search_03` | BFS Grid | O(n²) | 5 | **4** | **9** |
|  | `search_04` | DFS Grid | O(n²) | 4 | **4** | **9** |
|  | `search_05` | Ternary Search | O(log n) | 3 | **3** | **3** |
|  | `search_06` | Jump Search | O(log n) | 3 | **3** | **1** |
|  | `search_07` | Exponential Search | O(log n) | 4 | **3** | **1** |
|  | `search_08` | Interpolation Search | O(n) | 5 | **4** | **1** |
|  | `search_09` | Fibonacci Search | O(log n) | 4 | **4** | **1** |
|  | `search_10` | Sublist Search | O(n²) | 3 | **3** | **1** |
|  | `search_11` | Count Occurrences (Sorted) | O(log n) | 3 | **3** | **9** |
|  | `search_12` | Search in Rotated Sorted Array | O(log n) | 5 | **4** | **9** |
| **segment_tree** | | | | | | |
|  | `segtree_01` | Build Segment Tree | O(n) | 3 | **4** | **2** |
|  | `segtree_02` | Range Sum Query | O(log n) | 4 | **5** | **2** |
|  | `segtree_03` | Point Update | O(log n) | 3 | **4** | **2** |
|  | `segtree_04` | Range Minimum Query | O(log n) | 4 | **5** | **2** |
|  | `segtree_05` | Range Update with Lazy Propagation | O(n log n) | 6 | **7** | **1** |
|  | `segtree_06` | Range Min with Lazy Updates | O(n log n) | 7 | **7** | **1** |
| **sorting** | | | | | | |
|  | `sort_01` | Bubble Sort | O(n²) | 2 | **2** | **1** |
|  | `sort_02` | Selection Sort | O(n²) | 2 | **2** | **1** |
|  | `sort_03` | Insertion Sort | O(n²) | 3 | **2** | **1** |
|  | `sort_04` | Merge Sort | O(n log n) | 5 | **4** | **8** |
|  | `sort_05` | Quick Sort | O(n log n) | 5 | **4** | **8** |
|  | `sort_06` | Heap Sort | O(n log n) | 6 | **5** | **6** |
|  | `sort_07` | Counting Sort | O(n) | 4 | **3** | **6** |
|  | `sort_08` | Radix Sort | O(n) | 6 | **5** | **4** |
|  | `sort_09` | Bucket Sort | O(n) | 5 | **4** | **5** |
|  | `sort_10` | Shell Sort | O(n²) | 5 | **4** | **1** |
|  | `sort_11` | Cycle Sort | O(n²) | 5 | **5** | **1** |
|  | `sort_12` | Pancake Sort | O(n²) | 6 | **5** | **1** |
|  | `sort_13` | Tim Sort (Simplified) | O(n log n) | 5 | **6** | **1** |
|  | `sort_14` | Intro Sort (Simplified) | O(n log n) | 6 | **6** | **1** |
| **stack** | | | | | | |
|  | `stack_01` | Balanced Parentheses | O(n) | 2 | **2** | **9** |
|  | `stack_02` | Next Greater Element | O(n) | 4 | **4** | **8** |
|  | `stack_03` | Stock Span Problem | O(n) | 4 | **4** | **8** |
|  | `stack_04` | Largest Rectangle in Histogram | O(n) | 6 | **6** | **7** |
|  | `stack_05` | Min Stack | O(n) | 3 | **3** | **9** |
|  | `stack_06` | Trapping Rain Water | O(n) | 5 | **6** | **8** |
|  | `stack_07` | Infix to Postfix Conversion | O(n) | 4 | **4** | **8** |
|  | `stack_08` | Evaluate Reverse Polish Notation | O(n) | 3 | **3** | **7** |
| **strings** | | | | | | |
|  | `string_01` | Anagram Check | O(n) | 1 | **1** | **10** |
|  | `string_02` | Longest Palindromic Substring | O(n²) | 5 | **4** | **7** |
|  | `string_03` | KMP String Matching | O(n) | 7 | **7** | **1** |
|  | `string_04` | Naive Pattern Search | O(n²) | 3 | **4** | **7** |
|  | `string_05` | Longest Common Substring | O(n²) | 5 | **4** | **7** |
|  | `string_06` | Rabin-Karp | O(n) | 6 | **6** | **2** |
|  | `string_07` | Z-Algorithm | O(n) | 7 | **8** | **1** |
|  | `string_08` | Smallest Window | O(n²) | 7 | **5** | **8** |
|  | `string_09` | Run-Length Encoding | O(n) | 2 | **2** | **7** |
|  | `string_10` | Word Break (Strings) | O(n²) | 4 | **4** | **7** |
|  | `string_11` | Longest Common Substring | O(n²) | 4 | **4** | **7** |
|  | `string_12` | String to Integer (atoi) | O(n) | 3 | **3** | **8** |
|  | `string_13` | Z-Algorithm (Pattern Search) | O(n) | 5 | **8** | **1** |
|  | `string_14` | Longest Repeating Subsequence | O(n²) | 5 | **4** | **7** |
| **suffix_array** | | | | | | |
|  | `suffix_01` | Build Suffix Array | O(n²) | 4 | **8** | **1** |
|  | `suffix_02` | Pattern Search with Suffix Array | O(n log n) | 5 | **6** | **1** |
|  | `suffix_03` | LCP Array (Kasai's Algorithm) | O(n) | 5 | **7** | **1** |
|  | `suffix_04` | Count Distinct Substrings | O(n²) | 4 | **6** | **1** |
|  | `suffix_05` | Longest Repeated Substring | O(n²) | 3 | **6** | **1** |
| **trees** | | | | | | |
|  | `tree_01` | Preorder Traversal | O(n) | 3 | **2** | **9** |
|  | `tree_02` | Inorder Traversal | O(n) | 3 | **2** | **9** |
|  | `tree_03` | Postorder Traversal | O(n) | 3 | **2** | **9** |
|  | `tree_04` | Tree Height | O(n) | 2 | **2** | **9** |
|  | `tree_05` | Level-Order Traversal | O(n) | 3 | **3** | **9** |
|  | `tree_06` | BST Search | O(log n) | 3 | **2** | **9** |
|  | `tree_07` | Tree Diameter | O(n) | 4 | **4** | **9** |
|  | `tree_08` | BST Insert | O(log n) | 3 | **3** | **9** |
|  | `tree_09` | Mirror Tree | O(n) | 2 | **2** | **9** |
|  | `tree_10` | Max Path Sum | O(n) | 4 | **4** | **9** |
|  | `tree_11` | Balanced Tree Check | O(n) | 3 | **3** | **9** |
|  | `tree_12` | Symmetric Tree Check | O(n) | 3 | **3** | **9** |
|  | `tree_13` | Balanced Tree Check | O(n) | 3 | **3** | **9** |
|  | `tree_14` | Symmetric Tree Check | O(n) | 3 | **3** | **9** |
|  | `tree_15` | BST Delete | O(log n) | 5 | **5** | **8** |
|  | `tree_16` | Serialize / Deserialize | O(n) | 5 | **4** | **9** |
|  | `tree_17` | Lowest Common Ancestor | O(log n) | 4 | **4** | **9** |
|  | `tree_18` | Right Side View | O(n) | 3 | **4** | **9** |
|  | `tree_19` | Boundary Traversal | O(n) | 5 | **4** | **9** |
|  | `tree_20` | Binary Tree to BST | O(n log n) | 4 | **4** | **9** |
|  | `tree_21` | Root-to-Leaf Paths | O(n) | 3 | **4** | **9** |
|  | `tree_22` | AVL Insert (Simplified) | O(n log n) | 6 | **7** | **1** |
|  | `tree_23` | Kth Smallest in BST | O(n) | 2 | **3** | **8** |
| **trie** | | | | | | |
|  | `trie_01` | Trie Insert and Search | O(n) | 3 | **4** | **6** |
|  | `trie_02` | Word Count with Prefix | O(n) | 3 | **4** | **6** |
|  | `trie_03` | Longest Common Prefix | O(n) | 2 | **3** | **6** |
|  | `trie_04` | Delete Word from Trie | O(n) | 4 | **4** | **5** |

## Per-category summary

| Category | # | avg d (existing) | avg d (mine) | avg r (mine) |
|---|---:|---:|---:|---:|
| approximation | 7 | 5.0 | 5.9 | 1.3 |
| backtracking | 6 | 4.8 | 4.8 | 6.5 |
| bit_manipulation | 12 | 3.0 | 2.6 | 5.8 |
| branch_and_bound | 6 | 5.8 | 7.0 | 1.0 |
| divide_conquer | 19 | 4.7 | 4.8 | 5.2 |
| dynamic | 30 | 5.0 | 4.9 | 6.6 |
| fenwick | 7 | 4.1 | 4.7 | 1.0 |
| flow | 6 | 6.0 | 7.5 | 1.0 |
| geometric | 7 | 4.4 | 4.4 | 1.7 |
| graphs | 21 | 5.2 | 5.2 | 5.3 |
| greedy | 13 | 4.1 | 3.7 | 6.3 |
| hashing | 6 | 4.0 | 3.7 | 10.0 |
| heap | 6 | 5.0 | 4.3 | 7.0 |
| linked_list | 5 | 3.0 | 2.6 | 8.8 |
| math | 10 | 3.7 | 4.1 | 2.4 |
| queue | 5 | 3.6 | 3.2 | 5.0 |
| randomized | 7 | 4.3 | 4.1 | 2.0 |
| recursion | 4 | 2.8 | 2.2 | 7.0 |
| searching | 12 | 3.6 | 3.2 | 5.2 |
| segment_tree | 6 | 4.5 | 5.3 | 1.7 |
| sorting | 14 | 4.6 | 4.1 | 3.2 |
| stack | 8 | 3.9 | 4.0 | 8.0 |
| strings | 14 | 4.6 | 4.6 | 5.7 |
| suffix_array | 5 | 4.2 | 6.6 | 1.0 |
| trees | 23 | 3.4 | 3.3 | 8.6 |
| trie | 4 | 3.0 | 3.8 | 5.8 |

## Where my difficulty disagrees with existing by >= 2

| ID | Category | Name | Existing | Mine | Reason |
|---|---|---|---:|---:|---|
| `approx_04` | approximation | Christofides TSP (3/2-Approx) | 7 | 9 |  |
| `approx_07` | approximation | 0/1 Knapsack FPTAS | 7 | 9 |  |
| `bb_02` | branch_and_bound | Job Assignment (Hungarian) | 6 | 8 |  |
| `dp_29` | dynamic | Longest Increasing Subsequence (Patience Sort) | 4 | 6 |  |
| `flow_04` | flow | Dinic's Max Flow | 6 | 8 |  |
| `flow_05` | flow | Minimum s-t Cut | 5 | 7 |  |
| `flow_06` | flow | Push-Relabel Max Flow | 7 | 9 |  |
| `math_09` | math | Miller-Rabin Primality Test | 5 | 7 |  |
| `string_08` | strings | Smallest Window | 7 | 5 |  |
| `string_13` | strings | Z-Algorithm (Pattern Search) | 5 | 8 |  |
| `suffix_01` | suffix_array | Build Suffix Array | 4 | 8 |  |
| `suffix_03` | suffix_array | LCP Array (Kasai's Algorithm) | 5 | 7 |  |
| `suffix_04` | suffix_array | Count Distinct Substrings | 4 | 6 |  |
| `suffix_05` | suffix_array | Longest Repeated Substring | 3 | 6 |  |
