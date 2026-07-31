## General

**Describe exactly what one swap can change inside a window**

Give each `'1'` value $+1$ and each `'0'` value $-1$. A substring's score is therefore its number of ones minus its number of zeros. Score $0$ means the substring is already balanced.

A swap changes a chosen substring's counts only when one swapped index lies inside the substring, the other lies outside it, and the two characters differ. Replacing an inside zero with an outside one raises the score by $2$; the opposite exchange lowers it by $2$. Consequently, a window can be balanced after at most one swap only if its original score is $-2$, $0$, or $2$.

Let $Z$ and $O$ be the total numbers of zeros and ones, and define

$$
K=2\min(Z,O).
$$

No balanced result can be longer than $K$, because it needs half of its positions from each character count. This same bound makes the score condition sufficient. For example, a length-$L$ window with score $2$ contains $(L-2)/2$ zeros. Since $L\le K\le2Z$, at least one of the string's zeros lies outside the window, and an inside one can be exchanged with it. The score-$-2$ case is symmetric, while score $0$ needs no swap. Thus a window is selectable exactly when its length is at most $K$ and its score belongs to $\{-2,0,2\}$.

**Turn the window test into three prefix-balance lookups**

Let $P_i$ be the score of the prefix ending just before index $i$, with $P_0=0$. A window from prefix index $l$ to prefix index $r$ has score $P_r-P_l$. At each right endpoint $r$, a qualifying left endpoint must therefore have prefix score $P_r$, $P_r-2$, or $P_r+2$.

Store the observed indices for every prefix score in increasing deques. Because the length cannot exceed $K$, discard indices smaller than $r-K$ from each of the three queried deques. The earliest remaining index produces the longest qualifying window ending at $r$. Append $r$ to the deque for $P_r$ and continue.

Every reported window obeys the proven length and score conditions, so it is balanced already or can be repaired by one available outside character. Conversely, every feasible optimal window has one of the three queried score differences and a left endpoint no earlier than $r-K$; its index remains in the corresponding deque when its right endpoint is processed. The scan therefore finds a window at least as long as every feasible candidate and returns the optimum.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Counting characters and scanning prefix endpoints take $O(N)$ time. Each prefix index is appended once and removed from its deque at most once; only three deques are queried per endpoint, so expiration remains linear rather than becoming a nested scan.

The prefix-score deques can collectively retain $O(N)$ indices. All other state is constant, giving $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every substring:** Incrementally counting each of the $O(N^2)$ windows gives a correct direct test but is too slow for $N=10^5$.
- **Sorted index lists plus binary search:** Store all positions of every prefix score and binary-search the first index at least $r-K$. This is simpler to reason about but takes $O(N\log N)$ time instead of exploiting monotonic endpoints.
- **Return only the global count bound:** The value $2\min(Z,O)$ is an upper bound, not always attainable; widely separated minority characters can leave every window of that length too imbalanced for one swap.
- **All characters equal:** Here $K=0$, every positive-length window lacks one character, and the correct answer is `0`.
- **Whole string already balanced:** Its score is zero and its length equals $K$, so the prefix pair $(0,N)$ returns the full length without using a swap.
- **At most one swap:** Score-zero windows must remain candidates because the operation is optional.
- **Window-boundary swap:** Swapping two characters both inside or both outside a chosen window cannot change its counts; only a crossing swap of unlike bits can repair score magnitude $2$.
