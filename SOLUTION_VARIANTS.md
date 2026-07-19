# Solution Variants

Every canonical LeetCode package uses the same branch topology. The Optimal
branch is always present in the manifest, even while its authored artifacts are
still incomplete. A later corpus pass may add a Simplified branch to selected
low-Elo Easy or straightforward Medium problems.

## Shared problem artifacts

Problem identity and semantics do not change with an implementation choice.
Keep these files once at the package root:

```text
metadata.json
doc.md
cases.json
benchmark.json
complexity_certificate.json
guided_example.md
assets/
```

The root document owns only the shared statement, function contract, and
examples. Required Complexity is branch-specific metadata and appears inside
the selected solution tab. The ordinary cases and legal benchmark remain
shared. Never loosen, enlarge, or otherwise recalibrate those workloads merely
to accommodate another branch.

## Separated solution artifacts

Every package uses this structure:

```text
solution_variants.json
variants/
  optimal/
    approach.md
    submission.json
    solutions/
      python.py
      leetcode_python3.py
  simplified/
    approach.md
    submission.json
    solutions/
      python.py
      leetcode_python3.py
```

Each branch owns everything that can differ with the algorithm:

- its derivation, correctness reasoning, complexity detail, alternatives, and
  edge cases in `approach.md`;
- its Required Complexity bounds in `solution_variants.json`;
- its app-local `solve(...)` implementation;
- its exact platform-native implementation;
- its own remote Accepted evidence.

Additional directories such as `variants/simplified/` or
`variants/naive/` are created only when those branches are intentionally
authored. A directory alone is not a published tab.

## Eligibility and publication policy

The Optimal branch is mandatory, listed first, and remains the default
reference and benchmark implementation. Its reference explanation and
app-local source may be displayed before remote submission evidence exists;
full package completion still requires the exact native Optimal source to be
Accepted.

A simplified branch is optional. It is eligible only when:

1. the difficulty is Easy or Medium;
2. an effective Elo exists, preferring `elo_rating` over
   `estimated_elo_rating`;
3. that Elo is at or below the manifest ceiling, currently `1500`;
4. it passes the unchanged shared correctness cases and legal benchmark; and
5. the exact native source receives an Accepted result from LeetCode.

Do not infer Simplified branches during the repository-structure migration.
Test and verify the complete Optimal corpus first. The later Simplified pass
will apply the Elo policy, unchanged shared judge, and remote verification
requirements. If LeetCode rejects a proposed Simplified source, remove that
branch and its manifest entry.

## Manifest contract

`metadata.json` points to the manifest and repeats the default:

```json
{
  "solution_variants": {
    "manifest": "solution_variants.json",
    "default": "optimal"
  }
}
```

The manifest records the challenge identity, default, and ordered branch
descriptors. Each descriptor owns a plain `O(...)` time bound and space bound;
qualifications such as expected hash-table behavior belong in `Complexity
detail`, not in the displayed bound. `engine/solution_variants.py` validates
the topology before the API exposes a branch. A Simplified, naive, or other
non-default branch remains hidden until its exact native source is verified.

Every `approach.md` contains exactly these level-two headings in order:

```text
## General
## Complexity detail
## Alternatives and edge cases
```

The final section remains a scannable bullet list. The UI renders the selected
manifest bounds as the familiar Required Complexity heading with exactly Time
and Space bullets, directly inside that branch's tab.
