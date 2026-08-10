## General

**Global swaps erase word ownership but preserve lengths and character counts.** Because characters may be swapped between any positions in any words, the original letters belonging to a particular word do not constrain the final arrangement. All characters form one global pool. What cannot change is each word's length and the total count of each letter.

To make a palindrome of length $L$, its mirrored positions require

$$
2\left\lfloor\frac{L}{2}\right\rfloor
$$

characters arranged as equal pairs. If $L$ is odd, the remaining center position can contain any single character. Thus equal-letter pairs are the scarce resource; centers do not need a mate.

**Compute the total supply of paired characters with a parity mask.** Variable `s` first accumulates the total number of characters across all words. Variable `mask` has one bit per lowercase letter. For each occurrence of letter $c$, the code toggles its bit:

`mask ^= 1 << (ord(c) - ord("a"))`.

After processing all characters, a bit is one exactly when that letter's total frequency is odd. Therefore `mask.bit_count()` is the number of letters with odd global counts.

For a letter with frequency $f$, exactly $f-(f\bmod2)=2\lfloor f/2\rfloor$ of its occurrences can be grouped into equal pairs. Summed across letters, the total number of characters available in paired form is

$$
\text{total characters}-\text{number of odd frequencies}.
$$

That is why the source executes `s -= mask.bit_count()`. After this line, `s` counts paired characters, not the number of pairs. It is always even.

For example, frequencies 5, 4, and 1 supply 4, 4, and 0 paired characters respectively, for a total of 8. The parity mask has two set bits, and total length 10 minus 2 also gives 8.

**Spend paired characters on the cheapest words first.** A word of length $L$ needs `L // 2 * 2` paired characters for its mirrored slots. Shorter words never require more paired characters than longer words. To maximize how many words can be made palindromic, the source sorts `words` by length and considers them from shortest to longest.

For each word, it subtracts its pair demand from `s`. If `s` remains nonnegative, enough equal-letter pairs exist and the word is counted. If `s` becomes negative, this word cannot be funded. Because every remaining word is at least as long and therefore has pair demand no smaller, none of them can be funded either, so the loop breaks.

**Why shortest-first is optimal.** Suppose a selection contains a longer word with pair demand $d_{\text{large}}$ but excludes a shorter word with demand $d_{\text{small}}\le d_{\text{large}}$. Exchanging the longer word for the shorter one cannot increase resource use and preserves the number of palindromes. Repeating such exchanges transforms an optimal selection into a prefix of the words sorted by length. Therefore taking the longest affordable prefix maximizes the count.

This is the same greedy principle as buying the greatest number of items under one budget when every item has equal value and nonnegative cost: choose the smallest costs first.

**Why pair supply is sufficient, not merely necessary.** Each unit of two paired characters comes from two equal letters, so it can fill one mirrored position pair in any chosen word. Global swaps allow those pairs to be placed wherever needed. After all mirrored positions of chosen words are filled, every chosen odd-length word needs one center.

Centers cause no additional pairing constraint: any remaining character can fill a center. Total word lengths and total characters are unchanged, and paired-character accounting reserves only the mirrored slots. Characters not used in selected palindromes can occupy unselected words, while unpaired occurrences and any unused paired occurrences supply centers as needed. Thus having enough paired characters exactly characterizes feasibility for the selected lengths.

**A concrete example.** For lengths 4, 2, and 2, each word demands 4, 2, and 2 paired characters. Suppose the global counts yield 8 paired characters. Sorting gives demands 2, 2, 4. The algorithm funds all three exactly.

If only 6 paired characters are available, it funds the two length-two words, leaving 2. The length-four word needs 4 and fails. Choosing the length-four word plus one length-two word would also give two palindromes, never three, confirming the greedy maximum.

For an odd word of length 3, demand is only 2; its center is free with respect to pair supply. Consequently length 3 and length 2 have the same pair cost. Sorting by raw length places length 2 first, but either order among equal-cost cases yields the same maximum count.

**The code does not construct the palindromes.** It counts whether the global multiset has enough pair resources for the selected lengths. The problem asks only for the maximum number, and arbitrary swaps guarantee a realizing arrangement. Tracking specific letters for specific mirrored positions would add unnecessary complexity.

**Input mutation.** `words.sort(key=len)` rearranges the caller's list into nondecreasing length order. The strings themselves are immutable and unchanged, but their list order is not preserved.

## Complexity detail

Let $W$ be the number of words and

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$

be the total character count. Scanning every character to build total length and parity mask takes $O(S)$ time. Sorting the $W$ word references by length takes $O(W\log W)$ time. The final affordability scan is $O(W)$. Total time is

$$
O(S+W\log W).
$$

The algorithm stores only integers `s`, `mask`, and `ans` beyond the input. However, Python's in-place Timsort may allocate $O(W)$ temporary references, so the exact implementation's auxiliary space is $O(W)$ in the worst case. The 26-bit parity mask is constant-sized. This agrees with the local manifest's linear-space allowance.

No frequency dictionary is needed: the parity mask supplies exactly the odd-count information required to calculate total paired characters.

## Alternatives and edge cases

- **Full 26-entry frequency array:** Summing `count // 2` over letters also computes the pair supply and is perfectly valid. The parity-mask identity obtains the same total with constant compact state.
- **Try to preserve each word's original letters:** That ignores the global-swap permission and can underestimate the answer. Character ownership is completely transferable.
- **Construct actual palindrome strings:** It is possible after selecting lengths, but unnecessary because only the maximum count is returned.
- **Sort by pair demand directly:** Using `2 * (len(w) // 2)` is conceptually exact. Sorting by length gives the same nondecreasing demand order; adjacent odd/even lengths can tie without harming greediness.
- **All words length one:** Every demand is zero, so every word can be a palindrome regardless of character counts.
- **No equal-letter pair at all:** `s` becomes zero. Only length-one words, whose demand is zero, can be counted.
- **Odd global frequencies:** Each contributes one unpaired occurrence; subtracting the parity-mask population leaves the largest even usable amount for mirrored positions.
- **Odd-length words:** Their center requires no equal partner, so only `len(w) // 2 * 2` characters are deducted.
- **Exact exhaustion:** If subtraction makes `s == 0`, the word is feasible and is counted. Failure occurs only when `s < 0`.
- **First unaffordable word:** All later words have at least as large a pair demand, so breaking is safe.
- **Repeated word lengths:** Their demands tie, and their relative order cannot change the maximum count.
- **Input mutation:** The method leaves `words` sorted by length, even though it does not change any string's characters.
