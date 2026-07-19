## General
**Convert value choices into frequency choices**

Count the occurrences of every distinct value. Choosing a value removes exactly its frequency, so the identities of values no longer matter; only these counts affect how quickly the target of $n/2$ removed elements is reached.

Sort the frequencies descending and accumulate them until their sum is at least $n/2$. The number of consumed frequencies is the answer.

For any fixed number $q$ of selected values, the $q$ largest frequencies remove at least as many elements as any other $q$ frequencies: replacing a selected smaller frequency by an unselected larger one cannot reduce the total. Therefore, if the greedy prefix of length $q$ has not reached half, no set of $q$ values can succeed. The first greedy prefix that reaches the target is consequently minimal.

## Complexity detail
Hash counting takes expected $O(n)$ time. There are at most $n$ distinct frequencies to sort, costing $O(n\log n)$ time in the worst case. The counter and frequency list use $O(n)$ space.

## Alternatives and edge cases
- **Maximum heap:** Push all frequencies into a heap and repeatedly remove the largest; this can avoid fully sorting when the answer is small, while retaining $O(n\log n)$ worst-case time.
- **Counting frequencies of frequencies:** Because no frequency exceeds $n$, a bucket array can process counts descending in $O(n)$ time and $O(n)$ space.
- **Linear-search frequency table:** Avoiding a hash map by scanning prior distinct values for every element can take $O(n^2)$ time.
- **One distinct value:** Selecting it removes the complete array, so the answer is 1.
- **All values distinct:** Each choice removes one element, making the answer exactly $n/2$.
- **Tied frequencies:** Their order is irrelevant because they remove equal numbers of elements.
- **Overshooting half:** Removing more than $n/2$ elements is allowed.
