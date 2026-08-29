## General

**The goal is to assign digits to place values**

Once the digits are divided and ordered into two numbers, the sum is a weighted sum of those digits. A digit in a tens place contributes ten times its value, a digit in a hundreds place contributes one hundred times its value, and so on.

To minimize the total, smaller digits should receive larger place-value weights. The two numbers should also be as balanced in length as possible; otherwise one number creates an unnecessarily high place such as thousands while the other has unused lower places.

The solution obtains digits in ascending order and appends them alternately to two numbers. This simultaneously balances lengths and places the smallest digits earliest, where they become the most significant.

**Count digits without comparison sorting**

The code repeatedly extracts `num % 10`, increments that digit's Counter entry, divides `num` by ten, and increments `n`. This records the multiset of digits and their total count. Original digit order is irrelevant because any permutation is allowed.

Although the manifest says the digits are sorted, the exact implementation performs counting sort over the fixed alphabet $0$ through $9$. Pointer `j` starts at zero. Before choosing each next digit, the loop advances `j` until `cnt[j]` is positive, consumes one copy, and leaves `j` in place for possible duplicates.

Digits are therefore generated in nondecreasing order without building a sorted digit list.

**Why the two lengths must differ by at most one**

Consider the multiset of decimal place weights contributed by two result numbers. If their lengths differ by at least two, the longer number has a highest place whose weight is at least one hundred times a units place missing from the shorter side. Moving a leading digit from the longer number to extend the shorter one replaces a larger weight by a smaller weight and cannot increase the sum.

Thus an optimal layout distributes digit positions as evenly as possible. With an even number of digits, both numbers have equal length. With an odd number, one has exactly one extra digit.

Alternating assignments by `i & 1` guarantees precisely these lengths.

**Why ascending digits go into alternating positions**

For four digits, balanced two-digit numbers offer place weights

$$
10,10,1,1.
$$

The smallest two digits should take the two tens positions, and the largest two should take units positions. Alternating sorted digits does exactly that: the first digit starts number zero, the second starts number one, the third becomes number zero's units digit, and the fourth becomes number one's units digit.

For five digits, the balanced lengths are three and two, giving weights

$$
100,10,10,1,1
$$

after sorting from largest to smallest. Alternation assigns the smallest digit to the hundreds place of the longer number, the next two digits to tens places, and the final two to units places.

This is an instance of the rearrangement principle: pairing smaller digit values with larger positional weights minimizes their dot product.

**How appending constructs those places**

The statement

`ans[i & 1] = ans[i & 1] * 10 + j`

shifts the chosen result number left by one decimal place and inserts digit `j` as its new units digit. Earlier digits in that number become more significant. Since earlier assigned digits are never larger than later ones, each number's digits are nondecreasing from left to right, the best order for a fixed digit set.

The parity `i & 1` alternates zero, one, zero, one. The first result receives positions $0,2,4,\ldots$ from the sorted digit stream, while the second receives $1,3,5,\ldots$.

**Why zeros cause no problem**

Leading zeros are explicitly allowed. If a zero is one of the smallest digits, assigning it first gives it a large conceptual place weight but contributes nothing, which is ideal. Numerically, `0 * 10 + next_digit` naturally drops the leading zero without losing any required nonzero digit.

The digit counts, rather than the textual appearance of the final integers, preserve the fact that every original zero was assigned.

**Trace `num = 4325`**

The counts generate digits $2,3,4,5$:

- append $2$ to the first number, producing $2$;
- append $3$ to the second, producing $3$;
- append $4$ to the first, producing $24$;
- append $5$ to the second, producing $35$.

Their sum is $59$. Any arrangement that gives a larger digit one of the tens positions instead of $2$ or $3$ can be improved by swapping those digits.

**Why the construction is globally optimal**

Balanced lengths provide the smallest possible multiset of place weights. For that fixed multiset, assigning sorted digits oppositely to sorted weights is optimal: if a larger digit occupies a larger weight while a smaller digit occupies a smaller weight, swapping them changes the sum by

$$
(\textit{large}-\textit{small})(\textit{smallWeight}-\textit{largeWeight})\le0.
$$

Repeated swaps reach the alternating construction without increasing the sum. Therefore no different split can be smaller.

## Complexity detail

Let $d$ be the number of decimal digits. Extraction and construction each take $O(d)$ time. Scanning `j` across the ten digit values costs only $O(10)$. The exact code therefore runs in $O(d)$ time, stronger than the manifest's generic $O(d\log d)$ sorting bound.

The Counter has at most ten keys, and `ans` has two integers, so auxiliary space is $O(1)$ under the fixed decimal alphabet. The manifest's $O(d)$ bound would apply to an explicit sorted digit list, which this implementation does not allocate. Rebinding local `num` does not mutate caller state.

## Alternatives and edge cases

- **Sort a digit string:** Sorting then alternating is conceptually identical and costs $O(d\log d)$ time with $O(d)$ storage.
- **Try every split and permutation:** The possibilities grow factorially and ignore the place-value exchange structure.
- **Put all small digits in one number:** This unbalances lengths and creates larger high-place weights, usually increasing the sum.
- **Repeated digits:** Counter multiplicities ensure every occurrence is assigned exactly once.
- **Zeros:** Assigning them earliest is optimal, and permitted leading zeros need no special handling.
- **Even digit count:** Both result numbers receive the same number of digits.
- **Odd digit count:** The first result receives one extra digit, and the smallest digit occupies its extra highest place.
- **Two-digit input:** One digit goes to each one-digit result, so the answer is simply their sum.
- **Exact implementation:** It uses counting over ten digits, not comparison sorting as the manifest summary suggests.
