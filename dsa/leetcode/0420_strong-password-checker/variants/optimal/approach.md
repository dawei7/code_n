## General

**Three independent requirements can often share one edit**

A strong password must satisfy a length interval, contain all three required character types, and avoid runs of three equal characters. The challenge is not merely to count violations and add them: one insertion or replacement can repair several violations simultaneously. For example, replacing one character inside `"aaa"` with an uppercase letter can both break the repetition and add a missing uppercase type.

The solution first counts how many required types already appear. `countTypes` scans every character and sets one flag for lowercase letters, one for uppercase letters, and one for digits. The returned `types` is between zero and three, so `3 - types` is the number of missing categories. The `elif` chain is appropriate because one character belongs to at most one of these three categories; punctuation such as `'.'` and `'!'` sets none of them.

The optimal strategy then separates passwords into three length regimes. Insertions are forced when the string is shorter than six, replacements are sufficient when the length is already from six through twenty, and deletions are forced when it exceeds twenty. The relationship between edits and repeated runs differs in each regime.

**Case 1: fewer than six characters**

If `n < 6`, at least `6 - n` insertions are unavoidable because replacement and deletion cannot increase length. At least `3 - types` edits are also unavoidable because one edit can introduce at most one missing character category. This gives the lower bound

`max(6 - n, 3 - types)`.

The same number is sufficient. Mandatory insertions can be chosen from missing categories and placed inside repeated runs to break them. If more categories are missing than insertions are required, the remaining edits can be replacements that both add a category and break a repetition when needed. Because the original length is at most five, these strategically placed edits are enough to prevent any triple while reaching length six.

For `"a"`, the length deficit is five and two types are missing, so five insertions dominate. For `"aA1"`, the three types already exist but three characters must be inserted, so the answer is three. For `"aaaaa"`, one insertion is needed for length and two types are missing; two edits suffice, for example one insertion and one replacement placed to split the run.

This is why the short case does not separately scan repeated runs. Their repairs can be absorbed into the edits already counted by the larger of the two fundamental deficits.

**Count replacements required by a repeated run**

For passwords of valid or excessive length, the code scans maximal runs of identical characters. The sentinel `prev = '~'` is safe because the input alphabet does not contain `~`; the first real character therefore starts a new run with `cnt = 1`.

A run of length $L$ needs `L // 3` replacements if no deletions are applied. One replacement can be placed in every third position, splitting the run so that no segment retains three equal consecutive characters. Fewer replacements cannot work because the disjoint groups of positions `0..2`, `3..5`, and so on each need at least one changed character.

When a new character begins, `cnt // 3` for the completed run is added to `replace`, and `cnt` resets to one for the new run. The final run is added after the loop because no later character arrives to flush it.

**Case 2: length from six through twenty**

No insertion or deletion is required for length. Let `replace` be the sum of `L // 3` over all repeated runs, and let `missing = 3 - types`.

At least `replace` edits are necessary to destroy all triples, and at least `missing` edits are necessary to introduce absent categories. Replacements can serve both purposes: while changing every third character of a run, choose missing lowercase, uppercase, or digit characters as needed. If type repairs outnumber repetition repairs, additional replacements can be made at safe positions without creating a new triple.

Therefore the minimum is `max(replace, missing)`, not their sum. A password already satisfying both conditions returns zero.

**Case 3: more than twenty characters**

Let $D = n - 20$. Every valid result requires at least $D$ deletions. Since those deletions are mandatory, the best strategy spends them where they reduce the later replacement count most efficiently.

The effect depends on a run length modulo three. Initially a run of length $L$ costs `L // 3` replacements.

- If $L \bmod 3 = 0$, one deletion changes a length such as 3, 6, or 9 into 2, 5, or 8 and immediately reduces `L // 3` by one. This costs one deletion per saved replacement.
- If $L \bmod 3 = 1$, two deletions change a length such as 4, 7, or 10 into 2, 5, or 8 and reduce the replacement count by one. This costs two deletions per saving.
- If $L \bmod 3 = 2$, three deletions are needed before `L // 3` drops. This costs three deletions per saving.

These efficiencies prove the greedy priority: spend deletions on remainder-zero runs first, then remainder-one runs, then use groups of three anywhere repetitions remain.

**How the exact long-password bookkeeping works**

`remove` starts as the deletion budget `n - 20`. While each run is flushed, the code handles the most efficient opportunities.

For a run with `cnt % 3 == 0`, if a deletion remains, it immediately decrements `remove` and temporarily decrements `replace`. The subsequent `replace += cnt // 3` then records one fewer replacement than the undeleted run required. This arithmetic represents applying one deletion without constructing a modified string.

For a run with `cnt % 3 == 1`, the code increments `remove2`. This records one opportunity where two future deletions can save one replacement. It does not spend those deletions yet because the number of such opportunities may exceed the remaining budget.

Remainder-two runs need no special counter: after all cheaper opportunities are handled, any three deletions can reduce one still-required replacement, whether applied to an original remainder-two run or to a run whose earlier reduction changed its remainder.

After all runs are counted, `use2 = min(replace, remove2, remove // 2)` determines how many two-deletion opportunities can actually be used. It subtracts one replacement and two deletions for each. Then `use3 = min(replace, remove // 3)` spends groups of three remaining deletions to remove further replacement needs.

Any deletion budget left after that cannot reduce `replace`; it is still performed somewhere to reach length twenty, but it is charged only in the unavoidable $D$ deletion total.

**Combine deletions with the remaining repairs**

The final result is

`n - 20 + max(replace, 3 - types)`.

The first term counts every mandatory deletion. After those conceptual deletions, `replace` is the minimum number of edits still needed to break repeated runs. As in the medium case, those replacements can simultaneously introduce missing character types, so the remaining cost is the maximum of the two deficits.

Deletions can be selected without losing the sole representative of a required type: a password longer than twenty retains twenty characters, and run-focused deletions can preserve up to three category witnesses. Thus using the original `types` count does not force an overlooked category repair.

**Why the greedy deletion order is optimal**

Every mandatory deletion costs one step regardless of where it is used. Its only possible extra benefit is lowering the number of future replacements. A remainder-zero run yields that benefit after one deletion, a remainder-one run after two, and all other remaining opportunities after three. Spending a deletion on a more expensive opportunity while a cheaper one remains can never save more replacements; exchanging those deletions toward the cheaper run is at least as good. Repeating this exchange argument produces exactly the priority used by the code.

The algorithm therefore meets all lower bounds: unavoidable length edits, unavoidable type edits, and the minimized repetition edits after optimally assigning deletions. Its returned count is achievable and no smaller count can satisfy every rule.

## Complexity detail

Let $n$ be the password length. `countTypes` scans the string once. The applicable run-counting branch scans it once more, performing constant work per character. Total time is $O(n)$.

Only a fixed collection of counters, flags, and the previous character are stored. Runs are processed as they end rather than saved in a list, so auxiliary space is $O(1)$.

The constraint caps $n$ at 50, but the analysis remains linear for a generalized input length.

## Alternatives and edge cases

- **Breadth-first search over edited strings:** It could find a minimum in principle, but the branching factor over insertions, deletions, positions, and characters makes the state space enormous.
- **Add all violation counts:** Summing length deficit, missing types, and repetition replacements overcounts because one replacement or insertion can repair a repetition and a missing category together.
- **Replace every third repeated character before deleting:** For strings longer than twenty, this wastes mandatory deletions. Deleting from carefully chosen runs can eliminate some replacements for free beyond the deletion cost.
- **Delete from longest runs only:** Length alone does not determine immediate efficiency. A length-six run needs one deletion to save a replacement, while a length-five run needs three; modulo three controls the priority.
- **Already strong password:** Length is valid, `replace` and missing types are both zero, so the method returns zero.
- **Only punctuation:** `types` remains zero. Punctuation still contributes to length and repeated runs, but it satisfies no category.
- **Repeated punctuation:** The equality scan treats `'.'` or `'!'` exactly like repeated letters, correctly enforcing the no-three-identical rule.
- **Run ending at the last character:** The explicit post-loop flush is necessary; otherwise its replacements and deletion opportunities would be omitted.
- **Exactly length six or twenty:** These belong to the middle regime; no length edit is required.
- **Exactly length twenty-one:** One deletion is mandatory and is preferentially assigned to a remainder-zero run if one exists.
- **Several missing types inside repeated runs:** Replacement characters can be chosen from different missing categories, allowing repair costs to overlap.
