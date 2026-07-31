## General

**Expand every hop into unit boundaries.** A hop from $i$ to $j$ contributes `nums[j]` once for each of the $j-i$ boundaries it crosses. Therefore, the total score can be viewed as assigning a destination value to every boundary between consecutive indices.

For the boundary after index $i$, any destination at an index greater than $i$ is eligible. Its contribution can never exceed the maximum value in `nums[i + 1:]`. These per-boundary upper bounds are simultaneously attainable: scanning from right to left, the indices where the suffix maximum increases form a valid increasing hopping path when read left to right. Each boundary is then covered by a hop ending at an index holding its suffix maximum.

Start with the last value as the best available destination and as the contribution for the final boundary. Move left through indices $n-2$ down to $1$, update the running suffix maximum, and add it for the next boundary. The sum of these $n-1$ suffix maxima is exactly the optimal score.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The reverse scan visits each relevant index once, taking $O(n)$ time. It stores only the running maximum and accumulated score, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over all previous indices:** Computing the best score for every destination from every earlier source is correct but takes $O(n^2)$ time.
- **Always jump to the globally largest value:** That index may occur before boundaries that still must be crossed, so later suffix maxima also matter.
- With two elements, the only hop has score `nums[1]`.
- In a strictly increasing suffix, one direct hop to the last index is optimal.
- In a decreasing suffix, visiting every index realizes each successively smaller suffix maximum.
- `nums[0]` never contributes directly because index `0` is only a departure point.
