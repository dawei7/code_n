"""``GET /api/docs/*`` - the in-app algorithm reference.

Three endpoints:

* ``GET /api/docs/overview``   - returns the raw text of
  ``docs/README.md`` (the general overview + interview path).
* ``GET /api/docs/index``      - returns a JSON list of all
  263 challenges, with a ``has_doc`` flag for whether a
  per-algorithm doc exists yet.
* ``GET /api/docs/{path:path}`` - returns the raw text of a
  single markdown file. Path-traversal safe.

The docs are static markdown files in ``DOCS_ROOT`` (see
``server.app.config``). In dev, ``DOCS_ROOT = <repo>/docs``;
in the packaged Electron app it's ``resources/docs/``. Challenge docs
are grouped by source family first so large corpora stay easy to load
selectively:

* ``docs/algorithms/neetcode/{category}/...``
* ``docs/algorithms/geeksforgeeks/{category}/...``
* ``docs/mathematical/geeksforgeeks/{category}/...``
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

from challenges.registry import CHALLENGE_REGISTRY
from rate_algos import rate
from server.app.config import DOCS_ROOT


router = APIRouter()


# --- NeetCode Category Learning Data -----------------------------

NEETCODE_CATEGORY_INFO = {
    "neetcode_arrays": {
        "name": "Arrays & Hashing",
        "type": "Derived Challenge / Base Data Structure",
        "base_algo": "Hash Table Key-Value Lookups & Frequency Arrays",
        "concept": "Hashing maps keys to values in O(1) average time, replacing O(n) nested loop scans with constant-time membership lookups in a hash map or hash set.",
        "walkthrough": "Use a hash map or hash set to store elements as you iterate. Check if the complement or the existing item is already in the map/set to answer the query in constant time.",
        "time_explain": "We traverse the array of size N exactly once, performing O(1) hash table lookups.",
        "space_explain": "We store up to N elements in the hash map/set to facilitate constant-time lookups.",
        "math_principles": "- **Hash Collisions & Pigeonhole Principle**: If we insert more keys than available buckets, collisions occur; hash tables handle this using chaining or open addressing.\n- **Time-Space Trade-off**: We trade O(N) space complexity to reduce time complexity from O(N²) to O(N).",
        "math_equations": "Time: $T(N) = O(N)$ \nSpace: $S(N) = O(N)$",
        "pedagogic_insights": "Instead of checking all pairs, store what you have seen so far in a set. This shifts the lookup cost from a linear scan to a direct memory mapping."
    },
    "neetcode_two_pointers": {
        "name": "Two Pointers",
        "type": "Derived Challenge",
        "base_algo": "Pointer Convergence & Multi-pointer Traversal",
        "concept": "Using two coordinate indices (usually at opposite boundaries L and R, or moving at different speeds) to search/match values in-place.",
        "walkthrough": "Place one pointer at the start (L) and another at the end (R). Based on comparison rules, increment L or decrement R until they meet, narrowing down the candidate space.",
        "time_explain": "Each step advances at least one pointer, leading to at most N iterations.",
        "space_explain": "Only a constant number of pointer variables are stored, preserving O(1) space.",
        "math_principles": "- **Range Reduction**: By sorting the inputs (if not sorted), we can mathematically prove that if sum(L, R) > target, no larger R can pair with L, so we safely decrement R.\n- **Monotonic Convergence**: The index variable L increments or R decrements monotonically, bounding the loop bounds.",
        "math_equations": "Invariants: $0 \\le L < R \\le n - 1$. Pointer progression guarantees termination in $O(N)$ steps.",
        "pedagogic_insights": "Sorting allows us to make a binary decision at each step (too high vs too low), transforming a quadratic pair search space into a linear traversal."
    },
    "neetcode_sliding_window": {
        "name": "Sliding Window",
        "type": "Derived Challenge",
        "base_algo": "Dynamic Window Resizing (Expanding & Shrinking)",
        "concept": "Maintaining a continuous subarray boundary [L, R] that expands by moving R, and shrinks by moving L to satisfy a query constraint.",
        "walkthrough": "Iterate through the array with a right boundary pointer R. Add the new element to the current state. While the constraint is violated, shrink the window by moving L and updating state. Record the maximum/minimum valid window size.",
        "time_explain": "Both pointers L and R traverse the array of size N at most once, resulting in O(N) operations.",
        "space_explain": "Requires storing the window state (frequencies, counts) in a map/set of size bounded by the character set size.",
        "math_principles": "- **Amortized Analysis**: Although there is a nested loop to shrink the window, L only moves forward, meaning the inner loop runs at most N times over the entire runtime.\n- **Subarray Invariant**: Any subsegment [L, R] preserves a condition which we check incrementally rather than recomputing it.",
        "math_equations": "Window width $W = R - L + 1$.\nTotal possible subarrays of size $N$ is $\\frac{N(N+1)}{2}$.",
        "pedagogic_insights": "Instead of clearing the window and rebuilding it, we 'slide' it by adding the new element at R and removing the old element at L, saving redundant work."
    },
    "neetcode_stack": {
        "name": "Stack",
        "type": "Derived Challenge",
        "base_algo": "LIFO (Last In First Out) Monotonic Stack",
        "concept": "A stack processes elements where the last element inserted is the first one removed, maintaining order dependencies or finding next-greater/smaller elements.",
        "walkthrough": "Push elements or indexes onto the stack as you traverse. Compare incoming elements with the top of the stack. Pop elements when the relationship is satisfied (e.g. nested matching or monotonic order).",
        "time_explain": "Each element is pushed and popped from the stack at most once, leading to O(N) runtime.",
        "space_explain": "In the worst case, all N elements are pushed onto the stack.",
        "math_principles": "- **Grammar Parsing & Parentheses Invariants**: Nested structures follow a Dyck language grammar. A stack is the mathematical model (Pushdown Automaton) to parse context-free grammars.\n- **Monotonicity**: Monotonic stacks maintain sorted elements, keeping track of the local minima/maxima dynamically.",
        "math_equations": "Stack depth function $D(t) \\ge 0$ for all prefixes, and $D(\\text{end}) = 0$ for balanced grammar.",
        "pedagogic_insights": "The stack serves as a temporal memory of unresolved elements. When a matching or resolving element is seen, it resolves the most recent unresolved element first."
    },
    "neetcode_binary_search": {
        "name": "Binary Search",
        "type": "Base Algorithm / Derived Search Space",
        "base_algo": "Divide and Conquer Interval Halving",
        "concept": "Dividing the sorted search space in half at each step, checking the middle element to prune the invalid half.",
        "walkthrough": "Maintain low and high pointers. Compute mid = low + (high - low) // 2. If target matches mid, return it. If search criteria is met in the left half, move high to mid - 1, else move low to mid + 1.",
        "time_explain": "The search space size is halved in each iteration: N, N/2, N/4, ..., 1. This takes O(log N) steps.",
        "space_explain": "Uses constant variables for boundary pointers, keeping auxiliary space O(1).",
        "math_principles": "- **Logarithmic Halving**: Halving search space N leads to $\\log_2 N$ steps before size is 1.\n- **Decision Boundary**: Works on any sorted array or monotonic function where we can determine which half contains the solution.",
        "math_equations": "Recurrence Relation: $T(n) = T(n/2) + O(1)$, which solves to $O(\\log n)$ by Master Theorem.",
        "pedagogic_insights": "Binary search is not just for arrays. You can binary search on the solution space itself (e.g. min/max values) if the validation condition is monotonic."
    },
    "neetcode_linked_list": {
        "name": "Linked List",
        "type": "Base Data Structure",
        "base_algo": "Pointer Traversal & Floyd's Cycle Detection (Tortoise and Hare)",
        "concept": "A sequence of nodes where each node contains a value and a pointer to the next node. Algorithms utilize pointer swapping or fast/slow pointers.",
        "walkthrough": "Use temp pointer nodes. For reversing, swap next pointers using prev, curr, and temp variables. For cycle checks, move slow pointer by 1 step and fast pointer by 2 steps.",
        "time_explain": "Single traversal of the nodes in the list takes O(N) time.",
        "space_explain": "In-place pointer modifications require O(1) auxiliary space.",
        "math_principles": "- **Graph Topology & Cycle Detection**: A linked list with a cycle represents a functional graph with out-degree 1. Tortoise and Hare pointers meet because the fast pointer closes the gap by 1 each step.\n- **Modular Equivalence**: They meet at index $d$ where $d \\equiv 0 \\pmod C$ (with cyclic length C).",
        "math_equations": "Meeting Condition: $v_1 = 1 \\text{ step/iter}, v_2 = 2 \\text{ steps/iter}$. Meet point at $t = k \\cdot C$.",
        "pedagogic_insights": "Linked lists teach pointer manipulation. Always draw out the state of pointers before and after the swap to avoid cycles or losing references."
    },
    "neetcode_trees": {
        "name": "Trees",
        "type": "Base Data Structure",
        "base_algo": "Tree Traversal & Depth First Search (DFS) / Breadth First Search (BFS)",
        "concept": "A hierarchical tree structure. Traversals are preorder (visit, left, right), inorder (left, visit, right), or postorder (left, right, visit).",
        "walkthrough": "Use recursive functions for DFS to traverse subtrees. Use a queue for BFS (level-order traversal) to process nodes level by level.",
        "time_explain": "Every node is visited exactly once, yielding O(N) runtime.",
        "space_explain": "The recursion stack depth is equal to the height of the tree (O(H)), which is O(N) in worst case (skewed tree) and O(log N) in best case (balanced tree).",
        "math_principles": "- **Structural Induction**: Properties of trees are proved by showing they hold for the root node assuming they hold for the left and right subtrees.\n- **Recurrence Relations**: Calculations like tree height depend recursively on child node heights.",
        "math_equations": "Height recurrence: $H(\\text{node}) = 1 + \\max(H(\\text{left}), H(\\text{right}))$.",
        "pedagogic_insights": "Tree algorithms are naturally recursive. Solve the problem for subtrees, and combine the results at the root."
    },
    "neetcode_heap": {
        "name": "Heap / Priority Queue",
        "type": "Base Data Structure",
        "base_algo": "Binary Min/Max-Heap Heapification",
        "concept": "A complete binary tree that maintains the heap property: parent key is always less than/greater than child keys.",
        "walkthrough": "Use Python's `heapq` library. Push elements in O(log K) time. Pop minimum in O(log K) time to maintain a priority queue of top K elements.",
        "time_explain": "Inserting N elements into a heap of size K takes O(N log K) time.",
        "space_explain": "We store up to K elements in the heap.",
        "math_principles": "- **Complete Binary Tree Properties**: A heap of height H has between $2^H$ and $2^{H+1}-1$ nodes. Min/max retrieval is always O(1).\n- **Logarithmic Insertion**: Shifting elements up or down is bounded by the tree depth, which is $\\lfloor \\log_2 N \\rfloor$.",
        "math_equations": "Heap Indexing: For index $i$, left child is at $2i + 1$, right is at $2i + 2$, parent is at $\\lfloor (i-1)/2 \\rfloor$.",
        "pedagogic_insights": "A heap is ideal when you need to dynamically retrieve the min or max element while new elements are being added or removed."
    },
    "neetcode_backtracking": {
        "name": "Backtracking",
        "type": "Derived Challenge",
        "base_algo": "State-Space DFS with Pruning",
        "concept": "Systematically exploring all configurations in a decision tree. We backtrack (undo decision) when we hit a dead end or record a valid result.",
        "walkthrough": "Use recursion. At each step, choose an option, update the state, recurse to explore next choices, and then undo the option (backtrack) to explore other branches.",
        "time_explain": "Exponential or factorial complexity, e.g. O(2^N) or O(N!), due to exploring all permutations or combinations.",
        "space_explain": "Recursion stack depth is equal to the solution length, which is O(N).",
        "math_principles": "- **Combinatorics**: Backtracking maps combinations $C(n, k) = \\frac{n!}{k!(n-k)!}$ or permutations $P(n, k) = \\frac{n!}{(n-k)!}$ visually as a state tree.\n- **Pruning Invariants**: Pruning cuts branches of the decision tree early when we determine they cannot lead to a valid solution.",
        "math_equations": "Combination recurrence: $\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$. State tree size bounds: $O(2^n)$.",
        "pedagogic_insights": "Think of backtracking as traversing a graph of decisions. 'Do, Recurse, Undo' is the fundamental cycle."
    },
    "neetcode_tries": {
        "name": "Tries",
        "type": "Base Data Structure",
        "base_algo": "Prefix Tree Node Retrieval",
        "concept": "An alphabet-based search tree where nodes share common prefixes. Each node contains a map of characters to child nodes and an end-of-word boolean.",
        "walkthrough": "Create a TrieNode class. To insert, traverse character by character, creating nodes if they don't exist. To search, follow character paths; return false if a path is missing.",
        "time_explain": "Lookups and insertions take O(L) time, where L is the length of the string, independent of the dictionary size.",
        "space_explain": "Worst-case space is O(W * L), where W is the number of words, though shared prefixes reduce this significantly.",
        "math_principles": "- **String Prefix Relations**: Strings share a nested tree structure. Trie height is bounded by the longest word.\n- **N-ary Tree Branching**: Tries have a branching factor equal to the alphabet size (e.g. 26).",
        "math_equations": "Lookup Time: $O(L)$ where $L$ is word length. Space: $O(\\Sigma \\cdot N \\cdot L)$ where $\\Sigma$ is alphabet size.",
        "pedagogic_insights": "Tries are much faster than hashing for prefix matching ('starts with') queries because they share prefix paths."
    },
    "neetcode_graphs": {
        "name": "Graphs",
        "type": "Base Data Structure / Traversal",
        "base_algo": "Breadth First Search (BFS) & Depth First Search (DFS)",
        "concept": "Representing relationships using nodes (vertices V) and connections (edges E). BFS uses a queue (shortest path); DFS uses recursion (connectivity).",
        "walkthrough": "Build an adjacency list. Use a `visited` set. For BFS, pop node, visit neighbors, add unvisited to queue. For DFS, recursively visit unvisited neighbors.",
        "time_explain": "Every vertex and edge is processed at most once: O(V + E) complexity.",
        "space_explain": "We store the graph structure and visited set, requiring O(V + E) space.",
        "math_principles": "- **Graph Connectivity & Cycles**: Cycles exist if we visit an active node in the recursion path.\n- **Degree Sum Formula (Handshaking Lemma)**: Sum of vertex degrees is twice the number of edges $\\sum \\deg(v) = 2|E|$.",
        "math_equations": "Time complexity: $T = O(|V| + |E|)$. Space complexity: $S = O(|V|)$.",
        "pedagogic_insights": "BFS is guaranteed to find the shortest path in an unweighted graph because it explores nodes in concentric layers of increasing distance."
    },
    "neetcode_advanced_graphs": {
        "name": "Advanced Graphs",
        "type": "Derived Challenge",
        "base_algo": "Dijkstra's Shortest Path & Prim's Minimum Spanning Tree",
        "concept": "Finding shortest paths in weighted graphs or calculating minimum spanning trees using greedy choices and priority queues.",
        "walkthrough": "Use a min-heap to store nodes as (distance, node). Pop the closest node, update neighbors if a shorter path is found, and push back to heap.",
        "time_explain": "Heap operations take O(log V) time, leading to O((V + E) log V) total time.",
        "space_explain": "Heap and distance arrays store up to V elements: O(V) space.",
        "math_principles": "- **Greedy Subpath Correctness**: Dijkstra's algorithm works because the subpath of a shortest path is also a shortest path (optimal substructure).\n- **Topological Sorting**: A Directed Acyclic Graph (DAG) can be ordered linearly using Kahn's algorithm or DFS back-edges.",
        "math_equations": "Dijkstra relaxation: $d(v) = \\min(d(v), d(u) + w(u, v))$. Master bound: $O(E \\log V)$.",
        "pedagogic_insights": "Topological sorting is essential for task scheduling dependencies. Dijkstra's is equivalent to BFS but weighted by a min-heap."
    },
    "neetcode_dp1": {
        "name": "1-D Dynamic Programming",
        "type": "Derived Challenge",
        "base_algo": "1-D Bottom-up Tabulation & Memoization",
        "concept": "Solving overlapping subproblems by computing smaller subproblem solutions first and caching them in a 1-D array.",
        "walkthrough": "Define the base cases (e.g. dp[0], dp[1]). Write the recurrence relation dp[i] = f(dp[i-1], dp[i-2]). Loop from 2 to N, filling the array.",
        "time_explain": "We compute each state exactly once in O(1) time, yielding O(N) total time.",
        "space_explain": "Using an array of size N requires O(N) space, which can often be optimized to O(1) by storing only the last few states.",
        "math_principles": "- **Optimal Substructure**: The global optimal solution can be constructed from optimal solutions of its subproblems.\n- **Inductive Correctness**: If the recurrence holds from step k-1 to k, then by induction the final computed value is correct.",
        "math_equations": "Fibonacci recurrence: $dp[i] = dp[i-1] + dp[i-2]$. Knapsack-style: $dp[i] = \\min_j (dp[i - c_j] + 1)$.",
        "pedagogic_insights": "Instead of recalculating recursive subtrees, dynamic programming saves results. Draw the recursion tree to see the overlapping states."
    },
    "neetcode_dp2": {
        "name": "2-D Dynamic Programming",
        "type": "Derived Challenge",
        "base_algo": "2-D Bottom-up Tabulation / Interval DP",
        "concept": "Solving overlapping subproblems with two variables of state, typically represented as grid cells or interval indices.",
        "walkthrough": "Create a 2-D array of size M x N. Initialize the base rows/columns. Use nested loops to compute each cell dp[i][j] based on top, left, or diagonal neighbors.",
        "time_explain": "We compute M x N states, each taking O(1) time: O(M * N) time.",
        "space_explain": "Requires O(M * N) space for the 2-D grid, which can often be optimized to O(N) by storing only the previous row.",
        "math_principles": "- **DAG of State Transitions**: States form a directed acyclic graph. We must compute states in topological order (usually row-by-row or diagonal-by-diagonal).\n- **Optimal Subsegments**: In interval DP, we compute solutions for shorter intervals first.",
        "math_equations": "LCS recurrence: $dp[i][j] = dp[i-1][j-1] + 1$ if match else $\\max(dp[i-1][j], dp[i][j-1])$.",
        "pedagogic_insights": "2-D DP is common for grid paths, string comparisons, and matching problems. Identify what the row and column indices represent in your state."
    },
    "neetcode_greedy": {
        "name": "Greedy",
        "type": "Derived Challenge",
        "base_algo": "Locally Optimal Choices",
        "concept": "Making the choice that looks best at the moment, with the hope that it will lead to a global optimum.",
        "walkthrough": "Sort the elements if necessary. Iterate through the elements and make the immediate best choice, updating variables (e.g. current reach or end time).",
        "time_explain": "Often O(N log N) if sorting is required, or O(N) if we can iterate directly.",
        "space_explain": "Usually O(1) auxiliary space as we only store a few variables.",
        "math_principles": "- **Greedy Choice Property**: A global optimum can be reached by making local choices.\n- **Matroids**: Greedy algorithms are mathematically proven to yield optimal solutions for structures that form a matroid.",
        "math_equations": "Interval Scheduling: Sort by end time $E_i \\le E_{i+1}$. Always pick interval $i$ if $S_i \\ge \\text{last } E$.",
        "pedagogic_insights": "Greedy algorithms are simple but hard to prove. If you can't find a counterexample, think about how to prove correctness using induction."
    },
    "neetcode_intervals": {
        "name": "Intervals",
        "type": "Derived Challenge",
        "base_algo": "Sweep-line / Interval Sorting",
        "concept": "Sorting and processing ranges [start, end] to check for overlaps, merge intervals, or find minimum scheduling requirements.",
        "walkthrough": "Sort intervals by start time. Iterate through the sorted intervals. Compare the start of the current interval with the end of the previous merged interval to decide whether to merge or add a new interval.",
        "time_explain": "Sorting N intervals takes O(N log N) time, followed by a linear scan of O(N) time.",
        "space_explain": "Storing the merged intervals output requires up to O(N) space.",
        "math_principles": "- **Interval Algebra & Overlap**: Two intervals $[S_1, E_1]$ and $[S_2, E_2]$ overlap if and only if $\\max(S_1, S_2) < \\min(E_1, E_2)$.\n- **Order Theory**: Sorting creates a total order on the intervals based on starts, allowing single-pass sweep checks.",
        "math_equations": "Overlap Condition: $S_{\\text{curr}} < E_{\\text{prev}}$. Merge: $E_{\\text{prev}} \\gets \\max(E_{\\text{prev}}, E_{\\text{curr}})$.",
        "pedagogic_insights": "Sorting by start times simplifies interval logic because it guarantees that any overlap will happen with the most recently processed interval."
    },
    "neetcode_math": {
        "name": "Math & Geometry",
        "type": "Derived Challenge",
        "base_algo": "Number Theory, Vector Geometry, and Coordinate Transformations",
        "concept": "Leveraging mathematical properties such as prime factors, GCD, matrix coordinates, or vector algebra to solve queries directly.",
        "walkthrough": "Utilize Euclid's algorithm for GCD, or standard matrix rotation equations. Use coordinates to calculate geometric patterns.",
        "time_explain": "Varies from O(log N) for GCD/exponentiation to O(N^2) for matrix operations.",
        "space_explain": "Typically O(1) auxiliary space.",
        "math_principles": "- **Euclid's GCD Algorithm**: Based on the principle that the GCD of two numbers also divides their difference.\n- **Matrix Coordinate Rotations**: Rotating a grid corresponds to a geometric reflection and transpose operation.",
        "math_equations": "Euclid GCD: $\\gcd(a, b) = \\gcd(b, a \\bmod b)$. 2D rotation: $M_{\\text{new}}[j][n-1-i] = M_{\\text{old}}[i][j]$.",
        "pedagogic_insights": "Number theory and geometry problems can be solved in constant or logarithmic time if you can find the underlying mathematical formula or equation."
    },
    "neetcode_bit": {
        "name": "Bit Manipulation",
        "type": "Derived Challenge",
        "base_algo": "Bitwise Logic and Shifts",
        "concept": "Performing logical operations (AND, OR, XOR, NOT, shift) directly on the binary representation of integers.",
        "walkthrough": "Use `&` to mask bits, `^` to XOR, `<<` / `>>` to shift bits left/right. Use Brian Kernighan's algorithm `n & (n - 1)` to count set bits.",
        "time_explain": "Operations are processed in O(1) time or O(bits) which is O(1) for fixed 32-bit integers.",
        "space_explain": "Requires O(1) auxiliary space.",
        "math_principles": "- **Boolean Algebra & XOR identities**: $x \\oplus x = 0$, $x \\oplus 0 = x$, and commutative/associative laws.\n- **Two's Complement Representation**: Negative numbers are represented as $\\sim x + 1$.",
        "math_equations": "Brian Kernighan: $n \\gets n \\& (n - 1)$ clears the lowest set bit. Bit check: $(n \\gg i) \\& 1$.",
        "pedagogic_insights": "Bit manipulation is highly efficient because it operates directly on the CPU's register level. It's often used for state compression."
    }
}


def _clean_problem_description(description: str) -> str:
    """Keep the generated goal text focused.

    Some imported NeetCode specs still contain old inline example or
    external-reference sections. The dynamic reference view renders examples
    from structured samples below, so those embedded blocks would otherwise
    duplicate content and occasionally mention the wrong source family.
    """
    text = re.sub(
        r"\n+##\s+GeeksforGeeks Reference\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        description,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n+##\s+Example\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return text.strip()


def _format_problem_examples(spec, lang: str) -> str:
    if not spec.samples:
        return (
            "_Keine Beispiele in dieser lokalen Spezifikation._"
            if lang == "de"
            else "_No examples are included in this local specification._"
        )

    lines = []
    for i, sample in enumerate(spec.samples, start=1):
        if lang == "de":
            lines.append(
                f"**Beispiel {i}**\n\n"
                f"- Eingabe: `{sample.input_repr}`\n"
                f"- Ausgabe: `{sample.output_repr}`"
            )
        else:
            lines.append(
                f"**Example {i}**\n\n"
                f"- Input: `{sample.input_repr}`\n"
                f"- Output: `{sample.output_repr}`"
            )
    return "\n\n".join(lines)


def _format_parameter_contract(spec, lang: str) -> str:
    if lang == "de":
        input_lines = "\n".join(
            f"- `{name}`: {spec.inputs.get(name, 'Eingabewert')}"
            for name in spec.params
        )
        return f"**Eingaben**\n\n{input_lines}\n\n**Rueckgabe**\n\n{spec.returns}"

    input_lines = "\n".join(
        f"- `{name}`: {spec.inputs.get(name, 'input value')}"
        for name in spec.params
    )
    return f"**Inputs**\n\n{input_lines}\n\n**Return value**\n\n{spec.returns}"


def _format_learning_steps(spec, cat_info: dict, lang: str) -> str:
    hint = spec.hint.strip() if spec.hint else ""
    if lang == "de":
        steps = [
            "Lies zuerst den Rueckgabewert: Welche Form muss die Antwort haben, "
            "und muss sie eindeutig sein?",
            "Bestimme den Zustand, den du behalten musst. Bei dieser Kategorie ist "
            f"das meistens: {cat_info['concept']}",
            f"Wende das Standardmuster an: {cat_info['walkthrough']}",
        ]
        if hint:
            steps.append(f"Nutze diesen lokalen Hinweis beim Debuggen: {hint}")
        steps.append(
            "Pruefe deine Idee an einem kleinen Beispiel, bevor du Code schreibst. "
            "Wenn sich ein Zwischenergebnis nicht leicht erklaeren laesst, ist der "
            "Zustand wahrscheinlich noch nicht praezise genug."
        )
        return "\n".join(f"{i}. {step}" for i, step in enumerate(steps, start=1))

    steps = [
        "Start from the return value. Decide exactly what shape the answer must "
        "have and whether multiple valid answers are possible.",
        "Name the state you need to carry while scanning, recursing, or expanding "
        f"the search space. In this category, the core idea is: {cat_info['concept']}",
        f"Apply the reusable pattern: {cat_info['walkthrough']}",
    ]
    if hint:
        steps.append(f"Use this local debugging clue when you get stuck: {hint}")
    steps.append(
        "Trace one small example by hand before coding. If you cannot explain each "
        "state update in plain language, tighten the invariant before moving on."
    )
    return "\n".join(f"{i}. {step}" for i, step in enumerate(steps, start=1))


def _space_complexity_label(spec, cat_info: dict) -> str:
    category = spec.category.lower()
    if any(
        token in category
        for token in (
            "arrays",
            "stack",
            "heap",
            "trees",
            "graphs",
            "tries",
            "dp",
            "backtracking",
            "intervals",
        )
    ):
        return "O(N)"
    if any(
        token in cat_info["space_explain"].lower()
        for token in ("store", "stack", "heap", "grid", "array", "map", "set")
    ):
        return "O(N)"
    return "O(1)"


def generate_dynamic_reference(challenge_id: str, spec, lang: str) -> str:
    cat_info = NEETCODE_CATEGORY_INFO.get(spec.category, {
        "name": spec.category,
        "type": "Derived Challenge",
        "base_algo": "General Problem Solving",
        "concept": "Exploring subproblems or linear scans to solve queries.",
        "walkthrough": "Scan input elements and use temporary variables to track state.",
        "time_explain": "Traverses elements once.",
        "space_explain": "Uses constant variables.",
        "math_principles": "Mathematical optimization.",
        "math_equations": "",
        "pedagogic_insights": "Break down the inputs into simple steps."
    })

    difficulty_str = "Easy" if spec.difficulty <= 3 else "Medium" if spec.difficulty <= 7 else "Hard"

    if lang == "de":
        title_ref = "Referenz"
        cat_lbl = "Kategorie"
        diff_lbl = "Schwierigkeit"
        desc_lbl = "Problembeschreibung & Beispiele"
        algo_lbl = "Unterliegende Basisalgorithmen"
        concept_lbl = "Kernkonzept"
        complexity_lbl = "Komplexitaetsanalyse"
        time_lbl = "Zeitkomplexitaet"
        space_lbl = "Platzkomplexitaet"
        goal_lbl = "Ziel"
        contract_lbl = "Funktionsvertrag"
        examples_lbl = "Beispiele"
        why_lbl = "Warum diese Algorithmusfamilie passt"
        pattern_lbl = "Wiederverwendbares Muster"
    else:
        title_ref = "Reference"
        cat_lbl = "Category"
        diff_lbl = "Difficulty"
        desc_lbl = "Problem Description & Examples"
        algo_lbl = "Underlying Base Algorithm(s)"
        concept_lbl = "Core Concept"
        complexity_lbl = "Complexity Analysis"
        time_lbl = "Time Complexity"
        space_lbl = "Space Complexity"
        goal_lbl = "Goal"
        contract_lbl = "Function Contract"
        examples_lbl = "Examples"
        why_lbl = "Why this algorithm family fits"
        pattern_lbl = "Reusable pattern"

    is_base = any(x in spec.name.lower() for x in ["binary search", "bubble sort", "quick sort", "heap sort", "merge sort", "bfs", "dfs", "trie prefix tree", "lru cache", "union find"])
    algo_type = "Base Algorithm" if is_base else "Derived Challenge"

    time_comp = spec.required_complexity.value if hasattr(spec, "required_complexity") and hasattr(spec.required_complexity, "value") else "O(N)"
    space_comp = _space_complexity_label(spec, cat_info)
    description = _clean_problem_description(spec.description)
    contract = _format_parameter_contract(spec, lang)
    examples = _format_problem_examples(spec, lang)

    markdown = f"""# {title_ref}: {spec.name}

### **{cat_lbl}**: {cat_info['name']} | **{diff_lbl}**: {difficulty_str}

---

## {desc_lbl}
### {goal_lbl}
{description}

### {contract_lbl}
{contract}

### {examples_lbl}
{examples}

---

## {algo_lbl}
### {why_lbl}
This challenge is a **{algo_type}** built on **{cat_info['base_algo']}**.

- **{concept_lbl}**: {cat_info['concept']}
- **{pattern_lbl}**: Learn the category pattern, not just this one answer. The same idea should transfer to nearby NeetCode problems in this section.

---

## {complexity_lbl}
- **{time_lbl}**: `{time_comp}` — {cat_info['time_explain']}
- **{space_lbl}**: `{space_comp}` — {cat_info['space_explain']}
"""
    return markdown


def generate_dynamic_mathematical(challenge_id: str, spec, lang: str) -> str:
    cat_info = NEETCODE_CATEGORY_INFO.get(spec.category, {
        "name": spec.category,
        "math_principles": "Mathematical induction and state representations.",
        "math_equations": "$T(n) = O(n)$",
        "pedagogic_insights": "Trace small examples to understand patterns."
    })
    
    if lang == "de":
        title_lbl = "Mathematische Grundlagen"
        cat_lbl = "Kategorie"
        core_lbl = "Mathematischer Kern"
        eq_lbl = "Formeln & Gleichungen"
        insights_lbl = "Lernperspektive"
    else:
        title_lbl = "Mathematical Foundation"
        cat_lbl = "Category"
        core_lbl = "Mathematical Core"
        eq_lbl = "Recurrence & Equations"
        insights_lbl = "Learning Lens"
        
    markdown = f"""# {title_lbl}: {spec.name}

### **{cat_lbl}**: {cat_info['name']}

---

## {core_lbl}
To solve this challenge, we leverage the following mathematical principles:

{cat_info['math_principles']}

---

## {eq_lbl}
{cat_info['math_equations']}

---

## {insights_lbl}
{cat_info['pedagogic_insights']}
"""
    return markdown


router = APIRouter()


# --- Index entry -------------------------------------------------

class DocIndexEntry(BaseModel):
    id: str
    name: str
    category: str
    difficulty_existing: int
    difficulty_mine: int
    relevance_mine: int
    path: Optional[str]  # relative to DOCS_ROOT, or null if no doc
    has_doc: bool


# --- Helpers -----------------------------------------------------

def _slugify(name: str) -> str:
    """Match the filename convention used in docs/algorithms/*/.

    Examples: ``"Coin Change"`` -> ``"coin-change"``,
    ``"LCS"`` -> ``"lcs"``, ``"0/1 Knapsack"`` -> ``"01-knapsack"``.
    """
    s = name.lower()
    # Replace common separators with hyphens.
    for ch in " /(),:":
        s = s.replace(ch, "-")
    # Drop apostrophes (so "Levenshtein" doesn't have a stray `'`).
    s = s.replace("'", "")
    # Collapse multiple hyphens and strip leading/trailing.
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-").strip(".")


def _doc_family(category: str) -> str:
    """Return the source-family folder for a registry category."""
    if category.startswith("neetcode_"):
        return "neetcode"
    if category.startswith("leetcode_"):
        return "leetcode"
    return "geeksforgeeks"


def _doc_category_folder(category: str) -> str:
    """Return the category folder name inside the source-family folder."""
    for prefix in ("neetcode_", "leetcode_"):
        if category.startswith(prefix):
            return category.removeprefix(prefix)
    return category


def _category_dirs(category: str) -> list[Path]:
    """Map a category name to docs/algorithms/{family}/{category}/.

    The legacy flat path is checked as a fallback so older packaged docs keep
    resolving even if they have not been migrated yet.
    """
    return [
        DOCS_ROOT / "algorithms" / _doc_family(category) / _doc_category_folder(category),
        DOCS_ROOT / "algorithms" / _doc_family(category) / category,
        DOCS_ROOT / "algorithms" / category,
    ]


def _math_category_dirs(category: str) -> list[Path]:
    """Map a category name to docs/mathematical/{family}/{category}/."""
    return [
        DOCS_ROOT / "mathematical" / _doc_family(category) / _doc_category_folder(category),
        DOCS_ROOT / "mathematical" / _doc_family(category) / category,
        DOCS_ROOT / "mathematical" / category,
    ]


def _find_doc_path(challenge_id: str, name: str, category: str, lang: str = "en") -> Optional[Path]:
    """Return the absolute path of the doc, or None if it doesn't exist.

    Uses a prefix search on the challenge ID to resolve mismatches between
    registry names and disk filenames (e.g. 'graph_02_bfs.md' vs 'graph_02_breadth-first-search.md').
    """
    prefixes = [challenge_id]
    if category.startswith("leetcode_") and challenge_id.startswith("lc_"):
        prefixes.append(challenge_id.removeprefix("lc_"))

    for cat_dir in _category_dirs(category):
        if not cat_dir.is_dir():
            continue

        # Try finding files starting with challenge_id
        files = []
        for prefix in prefixes:
            files.extend(cat_dir.glob(f"{prefix}_*.md"))
        if not files:
            continue

        if lang == "de":
            de_files = [f for f in files if f.name.endswith("_de.md")]
            if de_files:
                return de_files[0]

        en_files = [f for f in files if not f.name.endswith("_de.md")]
        return en_files[0] if en_files else None

    return None


def _find_math_path(challenge_id: str, name: str, category: str, lang: str = "en") -> Optional[Path]:
    """Return the absolute path of the math doc, or None if it doesn't exist.
    
    Uses a prefix search on the challenge ID to resolve mismatches.
    """
    for cat_dir in _math_category_dirs(category):
        if not cat_dir.is_dir():
            continue

        files = list(cat_dir.glob(f"{challenge_id}_*.md"))
        if not files:
            continue

        if lang == "de":
            de_files = [f for f in files if f.name.endswith("_de.md")]
            if de_files:
                return de_files[0]

        en_files = [f for f in files if not f.name.endswith("_de.md")]
        return en_files[0] if en_files else None

    return None

# --- Endpoints ---------------------------------------------------

@router.get("/docs/index")
def docs_index() -> list[DocIndexEntry]:
    """List all challenges with their ratings and a has_doc flag."""
    out: list[DocIndexEntry] = []
    for cid, cls in sorted(CHALLENGE_REGISTRY.items()):
        spec = cls()._spec
        my_d, my_r = rate(spec.name, spec.category, spec.required_complexity.value, cid=cid)
        doc = _find_doc_path(cid, spec.name, spec.category)
        rel = None
        if doc is not None:
            try:
                rel = str(doc.relative_to(DOCS_ROOT)).replace("\\", "/")
            except ValueError:
                rel = None
        
        has_doc = doc is not None
        out.append(
            DocIndexEntry(
                id=cid,
                name=spec.name,
                category=spec.category,
                difficulty_existing=spec.difficulty,
                difficulty_mine=my_d,
                relevance_mine=my_r,
                path=rel,
                has_doc=has_doc,
            )
        )
    return out


@router.get("/docs/overview")
def docs_overview(lang: str = "en") -> Response:
    """Return the general overview doc (docs/README.md).

    Returns the file content with ``text/markdown`` so the
    client receives the raw markdown (no JSON wrapping or
    string escaping). FastAPI's default is to JSON-encode
    ``str`` returns, which would wrap the whole doc in
    quotes and escape newlines as ``\\n`` - not what we want
    for a markdown consumer.
    """
    readme_de = DOCS_ROOT / "README_de.md"
    readme_en = DOCS_ROOT / "README.md"
    readme = readme_de if lang == "de" and readme_de.is_file() else readme_en
    if not readme.is_file():
        raise HTTPException(status_code=404, detail="docs/README.md not found")
    return Response(
        content=readme.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/by-id/{challenge_id}")
def docs_by_id(challenge_id: str, lang: str = "en") -> Response:
    """Return the per-algorithm doc for a challenge (by challenge id).

    See :func:`docs_overview` for the media-type note.
    """
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = cls()._spec
    
    doc = _find_doc_path(challenge_id, spec.name, spec.category, lang)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"No doc yet for {challenge_id} ({spec.name}). "
                   f"Contribute at docs/algorithms/{_doc_family(spec.category)}/"
                   f"{spec.category}/{challenge_id}_*.md",
        )
    return Response(
        content=doc.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/math/by-id/{challenge_id}")
def math_by_id(challenge_id: str, lang: str = "en") -> Response:
    """Return the per-algorithm mathematical doc for a challenge (by challenge id)."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    spec = cls()._spec

    if challenge_id.startswith("nc_"):
        raise HTTPException(
            status_code=404,
            detail=f"NeetCode challenge '{challenge_id}' does not have a separate mathematical reference.",
        )

    doc = _find_math_path(challenge_id, spec.name, spec.category, lang)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"No mathematical doc yet for {challenge_id} ({spec.name}). "
                   f"Contribute at docs/mathematical/{_doc_family(spec.category)}/"
                   f"{spec.category}/{challenge_id}_*.md",
        )
    return Response(
        content=doc.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )


@router.get("/docs/{path:path}")
def docs_raw(path: str) -> Response:
    """Return the raw text of any file under DOCS_ROOT.

    Path-traversal safe: the resolved absolute path must remain
    inside DOCS_ROOT. The 403 is intentional - we don't want
    ``/api/docs/../server/app/main.py`` to leak the engine source.

    Sends the file with ``text/markdown`` so the client receives
    raw markdown (not JSON-wrapped).
    """
    if not DOCS_ROOT.is_dir():
        raise HTTPException(status_code=500, detail="DOCS_ROOT does not exist")
    target = (DOCS_ROOT / path).resolve()
    try:
        target.relative_to(DOCS_ROOT.resolve())
    except ValueError:
        raise HTTPException(status_code=403, detail="Path traversal denied")
    if not target.is_file():
        raise HTTPException(status_code=404, detail=f"Doc not found: {path}")
    return Response(
        content=target.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
    )
