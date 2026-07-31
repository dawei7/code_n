## General

**Turn directed-looking rules into undirected inversion edges.** Consider indices $i<j$. If `nums[i] > nums[j]`, the left index can jump forward to the smaller value. From the right index, the same pair permits a backward jump to the larger value. Thus every inversion is traversable in both directions. No other pair permits either direction. Reachability is therefore connectivity in the undirected inversion graph.

**Recognize where no inversion crosses a boundary.** Split after position $i$. There is no edge between the left prefix and right suffix exactly when every left value is at most every right value, which is equivalent to

$$
\max(\texttt{nums[0..i]})\le\min(\texttt{nums[i+1..n-1]}).
$$

Such a boundary cannot be crossed by any jump sequence, so it separates reachable regions. Conversely, between two consecutive separating boundaries, the inversion graph cannot split into value-ordered parts again; any proposed split would itself supply another prefix-maximum/suffix-minimum boundary. Equal values may create separate vertices without an edge, but cutting between equal ordered regions is harmless because their reachable maxima are equal.

Compute every suffix minimum in a right-to-left pass. Then scan from left to right while tracking the current region's maximum. Whenever that maximum is at most the suffix minimum after the current position, close the region and write its maximum to all answer positions in it. Each position is written once across all regions. Close the final region at the end.

Every closed region is isolated from later positions and contains no remaining separating boundary. Its inversion-connected vertices can reach the region maximum, and no path can reach a value outside it. Assigning the region maximum therefore gives exactly the required answer for every start.

## Complexity detail

Let $n$ be the length of `nums`. Building suffix minima takes $O(n)$ time. The forward scan visits each index once, and the region-filling loops write each answer position exactly once in total, so they also take $O(n)$ time. The suffix array and output use $O(n)$ space; excluding the required output, auxiliary space is $O(n)$.

The benchmark defines its size as $n$ and uses descending arrays, whose inversion graph is one component. The accepted prefix/suffix method remains linear. A calibrated correct alternative recomputes the entire prefix maximum and suffix minimum at every possible boundary, producing quadratic growth while returning the same component maxima.

## Alternatives and edge cases

- **Build every inversion edge:** Union-find or graph traversal is direct and correct, but inspecting all pairs costs $O(n^2)$ time and explicit edges can also require $O(n^2)$ space.
- **Recompute both sides at every boundary:** This uses the same boundary condition without preprocessing, but repeated prefix and suffix scans cost $O(n^2)$ time.
- **Search separately from every start:** Repeating a graph search can take $O(n^3)$ time if neighbors are rediscovered by scanning the array.
- **Strictly increasing array:** It has no inversions, so each index reaches only its own value.
- **Strictly decreasing array:** Every pair is an inversion, all indices share one component, and every answer is the first and largest value.
- **Equal adjacent regions:** Equality creates no jump because both rules are strict; separating equal-valued regions still assigns the same correct maximum.
- **Single element:** With no possible jump, its own value is the answer.
- **Several components:** Each valid boundary is independent, and maxima need not be globally equal across the output.
