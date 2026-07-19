## General
**Count ballots by candidate**

Join each `Vote.CandidateId` to the matching `Candidate.id`. Grouping the joined rows by candidate turns every ballot for one candidate into a single count.

**Rank the aggregate counts**

Order the candidate groups by descending `COUNT(*)`. Because the contract guarantees one candidate has strictly more votes than every other candidate, the first group is unambiguous; `LIMIT 1` returns only its name.

**Why the returned candidate is the winner**

The join associates every vote with exactly its chosen candidate, and grouping neither loses nor duplicates joined ballots. Each aggregate count therefore equals that candidate's true vote total. Descending order places the unique maximum first, so the selected row is precisely the winner.

## Complexity detail
With `V` votes and `C` candidates, the join and aggregation take $O(V + C)$ expected work with indexed or hashed identifiers. Ordering at most `C` aggregate rows takes $O(C \log C)$ time. The groups require $O(C)$ working space.

## Alternatives and edge cases
- **Aggregate votes before joining:** count `Vote` rows by `CandidateId`, select the largest count, then join that one identifier to `Candidate`; this has the same asymptotic bounds.
- **Window rank over counts:** `RANK()` can express maximum selection, but it is more machinery than needed when the winner is guaranteed unique.
- **Correlated count per candidate:** produces the right answer but may rescan the full vote table for every candidate and take $O(CV)$ time.
- **Candidate row order:** does not indicate popularity; only aggregated vote counts decide the result.
- **Candidates with no votes:** create no joined group and cannot be the winner while at least one ballot exists.
- **Unique winner guarantee:** means no tie-breaking rule should be invented.
- **Capitalized `Name` column:** preserve the requested output label exactly.
