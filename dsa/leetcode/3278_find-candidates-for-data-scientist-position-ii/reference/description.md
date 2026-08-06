## Description

The `Candidates` table records each candidate's proficiency from `1` through `5` in individual skills. Its `(candidate_id, skill)` pairs are unique. The `Projects` table similarly lists every skill required by a project and its importance from `1` through `5`; `(project_id, skill)` is its primary key.

A candidate is suitable for a project only when the candidate possesses every required skill. Score each suitable pair from a base of `100`: add `10` for every required skill whose proficiency exceeds its importance, subtract `5` when proficiency is lower, and make no change when they are equal.

For each project that has at least one suitable candidate, return only the candidate with the greatest score. Break a score tie in favor of the smaller `candidate_id`. Omit projects with no suitable candidate, and order the final rows by `project_id` ascending.
