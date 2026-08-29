## General

**Use each API answer to eliminate one person**

A celebrity must satisfy two conditions relative to every other person:

- the celebrity knows nobody else; and
- everybody else knows the celebrity.

Testing both conditions for every possible person would make $O(n^2)$ calls to `knows`. The key observation is that one call `knows(a, b)` always proves that at least one of `a` and `b` is not the celebrity.

If `knows(a, b)` is true, `a` cannot be the celebrity because `a` knows another person. If it is false, `b` cannot be the celebrity because at least one other person, namely `a`, does not know `b`. Regardless of the answer, one participant in the comparison is conclusively eliminated.

This lets the source reduce $n$ possibilities to one survivor using only $n-1$ questions.

**Maintain one surviving candidate**

The solution begins with `ans = 0`. It then compares the current candidate with each person `i` from 1 through `n - 1`.

If `knows(ans, i)` returns true, the current candidate has been caught knowing someone and is disqualified. Person `i` has not been disqualified by this particular fact, so the source replaces `ans` with `i`.

If `knows(ans, i)` returns false, person `i` is disqualified because `ans` does not know them. The current candidate has not been disproved by this fact, so `ans` remains unchanged.

It is important not to read too much into the survivor. In the true branch, knowing that the old candidate knows `i` does not prove that `i` is a celebrity; it merely leaves `i` as the only member of this pair still possible. Likewise, a false result does not prove `ans` is a celebrity. This phase eliminates candidates but does not verify all required relationships.

**Why no real celebrity is ever discarded**

After processing person `i`, `ans` is the only person among labels `0` through `i` who has not been ruled out by the questions asked so far.

The statement is true initially for person 0 alone. At the next comparison, exactly one of the old survivor and the new person is eliminated according to the API result, so one survivor remains for the enlarged prefix.

More strongly, if a real celebrity belongs to the processed prefix, that celebrity must be the survivor. Suppose the current candidate is the celebrity. They know nobody, so `knows(ans, i)` must be false and the algorithm keeps them. Suppose instead the newly considered person `i` is the celebrity. Everyone else knows them, so `knows(ans, i)` must be true and the algorithm changes the candidate to `i`. The update can never discard an actual celebrity.

After the loop, every person except `ans` has been disproved. Therefore, if a celebrity exists, it must be `ans`. This reduces verification to one person.

**Why elimination alone is insufficient**

If no celebrity exists, the pairwise process still leaves one survivor because each question eliminates only one of its two participants. That final person may fail a relationship that the elimination phase never asked about.

For example, the candidate might know an earlier person, or an earlier person might not know the candidate. Either fact violates the definition. The second pass is therefore mandatory; returning the survivor immediately would confuse “not yet disproved” with “proved.”

**Verify both directions against every other person**

For every label `i` other than `ans`, the source checks

```text
knows(ans, i) or not knows(i, ans)
```

If the first part is true, the candidate knows somebody and cannot be a celebrity. If the second part is true, person `i` does not know the candidate, so the candidate again fails. Either violation causes an immediate return of `-1`.

If the loop finishes, then for every other person `i`, both of the following hold:

$$
\neg\texttt{knows(ans, i)}
\qquad\text{and}\qquad
\texttt{knows(i, ans)}.
$$

Those are exactly the two celebrity conditions, so returning `ans` is correct.

The code skips `i == ans`. Whether a person knows themselves is irrelevant to the definition, which concerns the other $n-1$ people. The reference matrix happens to have ones on its diagonal, and querying that diagonal would falsely reject every candidate if treated as an outgoing relationship.

**Short-circuit evaluation saves unnecessary calls**

Python evaluates the `or` expression from left to right. If `knows(ans, i)` is true, the candidate is already disproved, so `not knows(i, ans)` is not evaluated. If the first call is false, the second direction must be queried.

This does not change the $O(n)$ bound, but it can reduce actual API calls when a non-celebrity candidate is rejected early. Because the API may be the expensive part of the problem, counting calls is more informative than counting ordinary arithmetic operations.

**Trace the first example**

For the matrix in which person 1 is the celebrity:

- Start with candidate 0. `knows(0, 1)` is true, so person 0 is eliminated and candidate becomes 1.
- Compare candidate 1 with person 2. `knows(1, 2)` is false, so person 2 is eliminated and candidate remains 1.
- Verification confirms that 1 does not know 0 or 2 and that both 0 and 2 know 1.

The method returns 1.

In an input with no celebrity, elimination still produces some `ans`. Verification eventually discovers either an outgoing relationship from `ans` or a missing incoming relationship and returns `-1`, as required.

**Why there cannot be two celebrities**

The definition itself makes a celebrity unique. If distinct people `a` and `b` were both celebrities, `a` would have to know `b` because everyone other than `b` knows `b`. But `a`, as a celebrity, must know nobody else. The requirements contradict each other. Thus successful verification of the survivor identifies the only possible celebrity.

## Complexity detail

The elimination pass performs exactly $n-1$ calls to `knows`. Verification considers $n-1$ other people and makes at most two calls for each. The worst-case total is

$$
(n-1)+2(n-1)=3n-3<3n.
$$

This directly satisfies the follow-up limit of at most $3n$ calls. With a genuine celebrity, both verification directions must be evaluated for every other person, so the source uses exactly $3n-3$ calls. With an invalid candidate, short-circuiting or early return may use fewer.

Assuming one API call takes $O(1)$ time, total time is $O(n)$. Linear time is asymptotically optimal: confirming a celebrity requires checking their relationship with every other person, because one unqueried person could be the counterexample that does not know the candidate or is known by the candidate.

The algorithm stores only the candidate, loop index, and a few temporary Boolean results. Auxiliary space is $O(1)$. It never materializes the inaccessible relationship matrix or caches API answers.

## Alternatives and edge cases

- **Verify every person independently:** Check both directions for each possible candidate. It is simple but makes $O(n^2)$ API calls in the worst case because the same relationships are queried repeatedly.
- **Stack elimination:** Put all people on a stack, pop two at a time, query one relationship, and push the only remaining possible candidate. This implements the same elimination proof with $O(n)$ calls but uses $O(n)$ stack space unnecessarily.
- **Cache API results:** Memoizing elimination calls can avoid repeating some questions during verification, at the cost of $O(n)$ stored results. The exact source already stays below `3n` calls with constant space.
- **Return the survivor without verification:** Incorrect when no celebrity exists. Elimination guarantees only that every other person was ruled out, not that the survivor satisfies all unqueried conditions.
- **Candidate knows someone:** One true outgoing query is enough to return `-1`; no incoming facts can repair that violation.
- **Someone does not know the candidate:** One false incoming query is likewise enough to return `-1`, even if the candidate knows nobody.
- **Self relationship:** The diagonal is skipped because knowing oneself neither qualifies nor disqualifies a celebrity under the definition.
- **Exactly one real celebrity:** The elimination pass is guaranteed to preserve that person, and complete verification returns their label.
- **No celebrity:** A survivor still emerges, but verification rejects it and returns `-1`.
- **Two people:** One elimination question leaves a candidate, and verification checks both required directions against the one other person.
- **API opacity:** The algorithm uses only `knows(a, b)` and never assumes direct access to `graph`. Reading or scanning the entire matrix would violate the interface contract.
- **Short-circuit order:** Querying the candidate's outgoing edge first allows immediate rejection without the incoming call. Reversing the checks remains correct but changes which failed cases save an API call.
