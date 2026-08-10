## General

**Represent balance with one number**

A substring is balanced when it contains the same number of `L` and `R` characters. Instead of maintaining two counts, the solution maintains their difference. The variable `l` increases by one for `L` and decreases by one for `R`. After reading a segment, `l == 0` exactly when the segment has equal counts.

At the beginning, `ans = l = 0` initializes both the number of completed balanced pieces and the running difference. The statement guarantees that every character is either `L` or `R`, so the code’s `else` branch can safely treat every non-`L` character as `R`.

**What the running balance means**

Because the balance is zero whenever a piece ends, it can be read in either of two equivalent ways:

- It is the difference between the total numbers of `L` and `R` in the prefix processed so far.
- After the latest cut, it is the difference inside the unfinished current piece.

When `l` returns to zero, all characters since the previous cut form a balanced substring. The solution immediately counts that substring by incrementing `ans`. It then continues scanning; no explicit reset is necessary because `l` is already zero.

For `s = "RLRRLLRLRL"`, the balance values are \(-1,0,-1,-2,-1,0,-1,0,-1,0\). Zeros appear after prefixes of lengths 2, 6, 8, and 10. Cutting at those positions gives `"RL"`, `"RRLL"`, `"RL"`, and `"RL"`, so the returned count is four.

**Why making the earliest possible cut is safe**

It might seem that an early balanced prefix should sometimes be merged with later characters to allow more pieces elsewhere. Merging cannot help the objective, which is to maximize the number of pieces. Once a prefix is balanced, taking it as its own piece leaves the remaining suffix balanced as well.

To see why, the entire input has equal total counts. Subtracting a prefix with equal counts leaves equal counts in the suffix. Thus an early cut never makes the remainder impossible to partition. Keeping that prefix attached to a later balanced portion can produce one larger balanced piece, but separating the two yields at least as many pieces.

There is also a clean upper-bound argument. In any valid split, each piece boundary occurs at the end of a globally balanced prefix. The first several balanced pieces together still contain equal total numbers of `L` and `R`, so the running prefix difference must be zero at every chosen boundary. Therefore, a valid split cannot contain more pieces than the number of zero-balance prefixes seen during the scan.

The algorithm cuts at every such zero prefix. Consecutive zero boundaries define substrings whose individual balance is zero minus zero, hence zero. It reaches the upper bound and is therefore optimal.

**Why this is a greedy algorithm**

At each position, the method permanently chooses a cut as soon as the current piece becomes balanced. The choice is greedy because it uses the earliest feasible ending, without looking ahead. Its correctness comes from the structure above: every possible piece ending must be one of the zero-balance positions, and selecting an earlier one cannot remove any later zero position.

Unlike some greedy problems, there is no need to compare alternative scores. Every zero crossing contributes one additional piece, and skipping it can never create two replacement boundaries where only one existed before.

**A more formal invariant**

After processing any prefix:

1. `ans` equals the number of zero-balance prefix endings encountered.
2. Cutting at those endings partitions the processed portion up to the latest ending into `ans` balanced substrings.
3. `l` is the balance of the characters after that latest ending.

The invariant is true before reading characters. Reading `L` or `R` updates the balance correctly. If it becomes nonzero, the unfinished piece remains open. If it becomes zero, the unfinished piece is balanced, incrementing `ans` makes the partition statement true, and the next unfinished piece begins from balance zero. At the end, the input guarantee makes the final balance zero, so every character belongs to a counted piece.

**Why only the count is stored**

The contract does not ask for the substrings or their boundary indices. The scan can therefore forget each completed piece immediately after counting it. The locations are implicit in moments when `l == 0`. Avoiding substring slicing is useful: slicing would allocate new strings even though their contents are not needed.

For `s = "LLLLRRRR"`, the balance rises from one through four and then falls back to zero only at the final character. There is exactly one feasible boundary and the algorithm returns one. This example shows that intermediate changes in direction do not matter; equality of the two counts is the only condition.

## Complexity detail

Let \(n=\lvert\texttt{s}\rvert\). The loop reads every character once and performs constant work, so time complexity is \(O(n)\). Any correct algorithm needs to inspect the input in the worst case because changing an unread character can alter where balance is reached, making this linear bound optimal.

Only `ans`, `l`, and the current character are stored. Their number does not depend on \(n\), so auxiliary space is \(O(1)\). The solution does not allocate substrings or modify `s`.

## Alternatives and edge cases

- **Two explicit counters:** Track counts of `L` and `R` separately and cut when they are equal. This remains \(O(n)\) time and \(O(1)\) space, but the signed difference expresses the condition with one state variable.
- **Stack simulation:** Push one symbol and cancel it with the other. It can detect balance but uses up to \(O(n)\) memory for information a single integer already captures.
- **Dynamic programming over cut positions:** Testing every balanced substring would be much more expensive. The zero-prefix characterization makes such optimization unnecessary.
- **One balanced piece only:** If the running difference returns to zero only at the final character, the maximum is one.
- **Alternating characters:** A string such as `"LRLRLR"` reaches zero every two characters, producing the maximum possible \(n/2\) pieces.
- **Input begins with either symbol:** The sign convention is arbitrary. Starting with `R` makes `l` negative, but only equality to zero matters.
- **Guaranteed final balance:** The problem promises that `s` itself is balanced, so the final character brings `l` to zero and all characters are included. Without that guarantee, the code would count balanced prefixes but leave an unbalanced suffix.
- **Even length:** Every balanced string has equal counts and therefore even length. The constraints need not state this separately because it follows from the guarantee.
- **Invalid characters:** The exact `else` branch treats anything other than `L` as `R`. This is correct only because the input alphabet is guaranteed to be exactly those two characters.
- **Returning boundaries:** If the task required the actual split, record the current index whenever `l` becomes zero. That would use \(O(ans)\) output space but would not change the greedy reasoning.
