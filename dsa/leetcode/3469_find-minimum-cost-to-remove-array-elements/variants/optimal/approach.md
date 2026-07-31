## General

After removing two of the current first three elements, exactly one of those three survives. Every element after them remains untouched and in its original order. Thus, before each ordinary operation, the active prefix consists of one carried element from an earlier index followed by the next two unseen values.

Maintain `costs[carried]`, the minimum amount already paid when `nums[carried]` is that survivor and `next_index` is the first unseen index. Initially index 0 is carried at cost zero and the unseen suffix begins at index 1. Let the next two values be `second = nums[next_index]` and `third = nums[next_index + 1]`. The three legal choices are:

- keep the old carried value, paying `max(second, third)`;
- keep `second`, paying `max(nums[carried], third)`;
- keep `third`, paying `max(nums[carried], second)`.

For an old carried index, only the first choice can preserve that identity, so its next cost is updated directly. Either new value can be reached from every old state, so take the minimum transition cost over all carried indices for each of those two identities. These transitions cover every legal pair removal exactly once and retain only the cheapest history leading to the same survivor, which is sufficient because future costs depend only on its value and the untouched suffix.

Advance the unseen boundary by two after each stage. If no unseen value remains, remove the carried value by itself. If exactly one remains, remove it together with the carried value. Taking the least final cost over all possible survivors yields the global optimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. There are $O(n)$ stages, and a stage may contain $O(n)$ possible carried indices. Each transition scan is linear in the current state count, giving $O(n^2)$ time. Only the current and next maps are retained, each with $O(n)$ entries, so auxiliary space is $O(n)$. A full memo table over every stage and survivor would use $O(n^2)$ space without improving the time bound.

## Alternatives and edge cases

- **Literal recursive enumeration:** Exploring all three removal choices without merging equal states grows exponentially.
- **Memoization by survivor and suffix boundary:** This also takes $O(n^2)$ time but stores $O(n^2)$ states; the exact native attempt using that table exceeded LeetCode's memory limit.
- **Greedily remove the two largest or two smallest:** A locally cheap or expensive pair can leave a costly survivor for later, so neither rule guarantees the minimum total.
- **One or two elements:** No ordinary operation occurs; the required final cost is simply their maximum.
- **Exactly three elements:** One pair is removed first and the survivor is then removed alone, so all three possible survivors matter.
- **Even versus odd length:** The final operation contains two elements for even $n$ and one element for odd $n$.
- **Duplicate values:** States are keyed by survivor index because histories differ, even when several survivor values are equal.
