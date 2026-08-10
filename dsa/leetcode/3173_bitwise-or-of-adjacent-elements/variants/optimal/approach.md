## General

**One output corresponds to one adjacent pair**

For an input of length $n$, output position $i$ is defined by exactly two values:

$$
\texttt{answer}[i]=\texttt{nums}[i]\mathbin{\mathrm{OR}}\texttt{nums}[i+1].
$$

There are $n-1$ adjacent pairs, so the direct construction is both simplest and sufficient.

`pairwise(nums)` lazily produces `(nums[0],nums[1])`, then `(nums[1],nums[2])`, continuing in left-to-right order. The list comprehension applies `a | b` to each and stores the results in the same order.

**Meaning of bitwise OR**

At each binary bit position, the result bit is 1 if at least one of the two input bits is 1. For 8 (`1000`) and 4 (`0100`), OR is 12 (`1100`).

For 1 and 3, binary `01 | 11 = 11`, so the result is 3.

No carry occurs between bit positions; OR is not addition.

**Why overlapping pairs are intentional**

An interior element appears in two outputs: once with its left neighbor and once with its right neighbor. For `[a,b,c]`, results are `a|b` and `b|c`. This is required because both index pairs are adjacent.

`pairwise` retains exactly this overlap. Grouping into disjoint pairs such as $(0,1),(2,3)$ would omit required outputs.


Every pair emitted by `pairwise` contains elements at consecutive indices. Pair number $i$ is exactly `(nums[i], nums[i+1])`, so its computed OR equals required `answer[i]`.

Conversely, every valid output index from 0 through $n-2$ has one emitted pair. The list comprehension therefore creates exactly $n-1$ correct entries in required order.

**Examples**

For `[1,3,7,15]`, each next number already contains all bits of the previous, so OR results are 3, 7, and 15.

For `[5,4,9,11]`:

- $5|4=5$;
- $4|9=13$;
- $9|11=11$.

The result is `[5,13,11]`.

**Why no state is needed across pairs**

Each answer depends only on the original two adjacent inputs. An OR from one pair must not be fed into the next pair. Doing so would compute prefix OR values rather than adjacent OR values.

The source uses a newly created output list and never overwrites `nums`, so every pair reads original values.

**Bit-level trace**

For adjacent values 5 and 4, use four-bit forms `0101` and `0100`. Reading from right to left:

- bit 0 is 1 because 5 supplies it;
- bit 1 is 0 because neither supplies it;
- bit 2 is 1 because both supply it;
- bit 3 is 0.

The result is `0101`, still 5.

For 4 and 9, forms `0100` and `1001` combine to `1101`, or 13. This shows how OR preserves all set bits from both neighbors.

**Useful OR properties**

OR is commutative, so swapping the two values inside one pair would not change that output. It is also idempotent, giving `x | x = x`. These properties help verify individual results, but they do not permit reordering the array because which values are adjacent determines which pairs exist.

The result is always at least each nonnegative operand numerically because it contains every 1-bit from both. It can equal one operand when that operand's set bits are a superset of the other's.

**Output independence**

Although two consecutive outputs share one source value, neither output depends on the other. The list comprehension evaluates `a | b` from iterator values and appends the result; it does not carry accumulated bit state.

This independence also allows each pair to be computed conceptually in parallel, though the compact source processes them sequentially.

**Boundary length**

The contract guarantees $n\ge2$, so there is at least one pair. If a length-one list were supplied outside the contract, `pairwise` would emit nothing and the method would return an empty list, which is the natural $n-1$ result.

## Complexity detail

Let $n$ be input length.

`pairwise` emits $n-1$ pairs and each OR is constant time under bounded integers, so time is $O(n)$.

The returned list has $n-1$ integers and therefore uses $O(n)$ required output space. Excluding output, the pairwise iterator and comprehension loop use $O(1)$ auxiliary space.

The manifest's $O(n)$ space includes the returned array.

The input list is not modified.

Under the value bound 100, each integer has at most seven relevant bits. The usual model treats one OR as constant time; more generally, arbitrary-precision OR cost would depend on integer bit length.

## Alternatives and edge cases

- **Index loop:** Append `nums[i] | nums[i+1]` for `i` from 0 to $n-2$. It is equivalent and avoids requiring `pairwise`.
- **`zip(nums, nums[1:])`:** Concise, but `nums[1:]` allocates an extra $O(n)$ slice.
- **In-place overwrite:** It risks corrupting the next pair because interior original values are reused.
- **Prefix OR:** Incorrect; it accumulates earlier elements rather than using only adjacent pairs.
- **Two elements:** Exactly one OR value is returned.
- **Equal adjacent values:** `x | x = x`.
- **One value's bits contain the other's:** The OR equals the bitwise superset.
- **Zero neighbor:** `x | 0 = x`.
- **Interior element:** It correctly contributes to two neighboring results.
- **Order preservation:** Pairwise iteration produces outputs by increasing left index.
- **Nonnegative inputs:** Binary OR has the straightforward finite representation intended by the problem.
- **Output length:** Exactly one less than input length.
