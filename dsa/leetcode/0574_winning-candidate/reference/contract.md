## Function Contract

**Inputs**

`Candidate(id, name)` identifies every candidate. `Vote(id, candidateId)` records one selected candidate per ballot through the foreign-key relationship `Vote.candidateId = Candidate.id`.

Let $V$ be the number of rows in `Vote` and $C$ the number of rows in `Candidate`.

**Return value**

Return a one-row table with a `name` column containing the unique candidate with the greatest vote count.
