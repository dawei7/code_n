## General

**Make the best possible next character decisive**

Count the 26 letters and consider available letters from `z` downward. If the
largest remaining letter is not currently blocked, placing it next dominates
every choice of a smaller letter at the first differing position. Use as many
copies as possible, up to `repeatLimit`; shortening that run would expose a
smaller character earlier and could not improve the result.

**Break a full run with the best separator**

If copies of that largest letter remain after its allowed run, another copy
cannot be appended immediately. The only way to use it later is to insert a
smaller letter. Choose the largest available smaller letter and use exactly
one copy: a smaller separator would make the current prefix worse, while more
than one separator would delay the preferred large letter unnecessarily.

After the separator, the same largest letter is eligible again. When it is
exhausted, continue downward. If it is blocked and no smaller letter remains,
construction must stop; discarding its unusable copies is permitted.

At every position this rule chooses the largest character compatible with a
continuation. Any different valid string either makes the same choices or
first selects a smaller character, so it cannot be lexicographically larger.
The separator rule also preserves the possibility of using the maximum number
of preferred letters before moving permanently to lower ones.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting the input and materializing the
result take $O(n)$ time. The two descending indices traverse only the
26-letter alphabet between emissions, so their total overhead is linear in
the output length plus a constant alphabet scan. The pieces and returned
string occupy $O(n)$ space; the frequency table uses $O(1)$ space.

## Alternatives and edge cases

- **Maximum heap:** Repeatedly pop the largest letter and temporarily use the
  next one as a separator. This is also correct, but a fixed 26-entry count
  array is simpler and avoids heap operations.
- **Resort remaining characters after every choice:** Selecting greedily from
  a freshly sorted multiset is correct but can take $O(n^2\log n)$ time.
- If one letter is the only available character, at most `repeatLimit` copies
  can appear and all remaining copies must be discarded.
- A separator is used once even when many copies are available, because the
  larger blocked letter should resume immediately.
- When `repeatLimit` is at least every frequency, the result is simply all
  characters in descending order.
- The optimal result need not use all input characters.
