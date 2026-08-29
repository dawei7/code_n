## General

**Reduce the task to runs in the binary group array.** The validity condition depends only on `groups`. Words do not need to be compared; each selected word simply accompanies its group bit.

A maximal run is a longest consecutive region containing the same group value. For `[1,0,1,1]`, the runs are `[1]`, `[0]`, and `[1,1]`. Neighboring runs necessarily have different values because each run ends exactly when the bit changes.

**At most one index can be selected from a run.** Suppose two selected indices come from the same run. Because the selection is a subsequence, any selected indices between them must lie at positions between them in the original array. But every position between them belongs to the same maximal run and has the same group value. Eventually two consecutive selected entries would therefore have equal group values, violating alternation. So a valid subsequence contributes at most one word per run.

**One index from every run is achievable.** Choose any representative from the first run, then one from the second, and continue. Indices increase because runs occur left to right. Consecutive chosen groups differ because neighboring runs differ. This yields a valid subsequence whose length equals the number of runs.

The upper and lower bounds match: the optimum length is exactly the number of maximal runs.

**How the comprehension chooses representatives.** The source returns:

`[words[i] for i, x in enumerate(groups) if i == 0 or x != groups[i - 1]]`.

Index zero is always chosen because it starts the first run. For every later index `i`, the condition compares current group `x` with the preceding array entry. If they differ, `i` is the first position of a new run and its word is selected. If they are equal, `i` lies inside the current run and is skipped.

Thus the source chooses the leftmost word of every maximal run. The problem permits any longest answer, so choosing leftmost representatives is valid even when another answer could choose later words from some runs.

**Trace `words = ["e","a","b"]` and `groups = [0,0,1]`.** Index zero is included. Index one has the same group as index zero, so it is skipped. Index two changes from zero to one and is included. The result is `["e","b"]`. Choosing `"a"` instead of `"e"` would also be optimal, but the comprehension deterministically chooses the run start.

For `groups = [1,0,1,1]`, run starts are indices zero, one, and two. Index three repeats group one and is skipped. Corresponding words `["a","b","c"]` form the displayed answer.

**Why binary values make the greedy proof especially transparent.** With only zero and one, every run change automatically flips to the other value. The same run-representative argument actually works for any labels when the only requirement is adjacent inequality: maximal runs of equal labels still have unequal neighboring labels. The binary promise guarantees this interpretation with no additional constraints.

**Subsequence order is preserved.** The comprehension scans indices in ascending order and appends words immediately. It never sorts or rearranges them. Returning one word per run therefore respects the original word order.

**Words are distinct but the algorithm does not need that fact.** The validity rule references corresponding group entries, not equality of word text. Even if two words were equal, selecting their indices from alternating runs would satisfy this version's condition. Distinctness is part of the contract but not needed by the greedy mechanism.

## Complexity detail

Let $n$ be the number of words. `enumerate(groups)` visits every group once and each condition is constant time, so running time is $O(n)$. If there are $r$ runs, the returned list stores $r$ references and uses $O(r)$ output space, at most $O(n)$.

Apart from the required result list and comprehension iteration state, auxiliary space is $O(1)$. The manifest's $O(n)$ space includes the possible length-$n$ output.

## Alternatives and edge cases

- **Dynamic programming:** Longest-subsequence DP works but costs $O(n^2)$ time for a structure whose optimum is simply the number of runs.
- **Choose rightmost run representatives:** Also optimal, but the source chooses leftmost representatives by detecting run starts.
- **Single word:** Index zero is selected, giving the only possible and longest subsequence.
- **All groups equal:** There is one run, so exactly one word is returned.
- **Groups alternate everywhere:** Every index starts a new run and all words are returned.
- **Multiple valid answers:** Any representative per run works; the judge permits any optimum.
- **Word contents:** They are irrelevant in version I and are not compared.
- **Output order:** Run starts are encountered left to right, so the returned words remain a subsequence.
- **Do not select twice inside one run:** Two chosen indices from the same maximal run would have equal groups if no different-group choice lies between them. Keeping more than one cannot extend the alternating sequence beyond the one-representative-per-run bound.
