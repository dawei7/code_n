## General

**Turn feedback vocabulary into constant-time score lookups**

Positive words are worth $+3$, negative words are worth $-1$, and every other word is worth zero.

The method converts `positive_feedback` to set `ps` and `negative_feedback` to set `ns`. Hash-set membership is expected $O(1)$, so each report word can be classified without scanning either vocabulary list.

The contract guarantees that no word belongs to both sets. The `if` followed by `elif` therefore has an unambiguous result:

- if `w in ps`, add three;
- else if `w in ns`, subtract one;
- otherwise, leave the score unchanged.

**Process reports with their student IDs**

`zip(student_id,report)` pairs corresponding entries. For each pair `(sid,r)`, local score `t` begins at zero.

`r.split()` separates the report at spaces. The input guarantees one space between consecutive lowercase words, so each resulting token is exactly one feedback word.

Every occurrence is scored. If a positive word appears twice, it contributes six total points; feedback is based on word occurrences, not merely the set of words used in the report.

After the complete report, `(t,sid)` is appended to `arr`.

Student IDs are unique, so every report corresponds to a distinct ranking entry.

**Why unknown words contribute zero**

Reports may contain ordinary words absent from both feedback lists, such as `"this"` or `"student"`. The source has no final `else` update, so these words leave `t` unchanged, exactly matching the scoring rules.

No stemming, punctuation removal, or case conversion is needed because the input already consists of lowercase words separated cleanly by spaces.

**Encode both ranking rules in one sort key**

Students rank by:

1. higher score first;
2. lower student ID first when scores tie.

Python sorts keys in ascending lexicographic order. The key

`(-x[0],x[1])`

negates the score, so a larger original score becomes a smaller negative number and appears earlier. The ID remains positive and unmodified, so smaller IDs appear first among equal negative scores.

For scores 5 and 2, keys begin with $-5$ and $-2$, placing score 5 first. For two score-5 students with IDs 10 and 3, keys are `(-5,10)` and `(-5,3)`, placing ID 3 first.

**Select exactly the top `k` IDs**

After sorting, `arr[:k]` contains the highest-ranked `k` entries. The list comprehension extracts tuple position one, the student ID:

`[v[1] for v in arr[:k]]`.

The score itself is not part of the requested output.

The constraint `1<=k<=n` ensures the slice contains exactly `k` entries.

**Trace the second sample**

Student 1's report `"this student is not studious"` contains:

- negative word `"not"` for $-1$;
- positive word `"studious"` for $+3$;
- three neutral words.

Its total is two.

Student 2's report contains positive word `"smart"` and receives three. Their ranking tuples are `(2,1)` and `(3,2)`. Sort keys `(-2,1)` and `(-3,2)` put student 2 first, producing `[2,1]`.

**Why the procedure is correct**

For each student, the inner loop visits every report word and adds exactly its defined contribution, so tuple `t` equals that student's true points.

The sort key orders any pair correctly: differing scores are placed in non-increasing score order, and equal scores are placed in increasing ID order. Thus the whole sorted array matches the complete ranking.

Taking its first `k` entries and returning their IDs yields exactly the requested top students.

**Input arrays remain unchanged**

The method creates sets and a separate ranking array. It does not modify the feedback lists, reports, or ID array. `arr.sort` mutates only the local tuple list.

## Complexity detail

Let $F$ be the total size of the two feedback vocabularies, measured by their words or total characters, and let $R$ be the total number of words or characters across all reports.

Building sets costs expected $O(F)$. Tokenizing and scoring reports costs expected $O(R)$. Sorting $n$ ranking tuples costs $O(n\log n)$. Total time is

$$
O(F+R+n\log n).
$$

The two sets use $O(F)$ storage, the ranking array uses $O(n)$, and splitting one report temporarily uses space proportional to that report. The returned list uses $O(k)$. Total auxiliary storage is $O(F+n+R_{\max})$, commonly summarized as $O(F+n)$ under bounded report length.

## Alternatives and edge cases

- **One weight dictionary:** Map positive words to 3 and negative words to $-1$, then use a default zero lookup.
- **Size-`k` heap:** It can avoid sorting all students when `k` is much smaller than `n`, but tie ordering must be encoded carefully.
- **Repeated feedback word:** Score every occurrence, not only the first.
- **Neutral word:** It contributes zero.
- **Equal scores:** Lower student ID ranks higher.
- **Negative total score:** It is valid and sorts below larger scores.
- **`k=n`:** Return every ID in full ranking order.
- **Unique IDs:** They eliminate a remaining sort tie.
- **Disjoint vocabularies:** The `if/elif` precedence never faces a contradictory word.
- **Report splitting:** The single-space guarantee makes tokens exact.
