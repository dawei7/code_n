# Optimal Solution Alignment

This document is the authority for keeping each cOde(n) Optimal reference and
its exact remotely Accepted LeetCode source semantically and pedagogically
aligned. Remote acceptance proves the platform-native source is correct; it
does not prove that the separately maintained app-local source implements the
same solution.

## Completion standard

Every canonical package from frontend ID 1 through 4005 must satisfy one of
these states:

1. **Structurally aligned:** executable structure, parameter and local names,
   referenced helpers, and data flow match after removing only type annotations,
   docstrings, the unavoidable platform entry-point wrapper, and a validated
   data-only app declaration for a judge-provided model.
2. **Reviewed unavoidable difference:** a current `alignment_review.json`
   explains a source-native representation, platform signature, judge
   environment, app execution adapter, or SQL dialect difference. The review is
   bound to the canonical UTF-8/LF hashes of both sources,
   `solution_variants.json`, and `approach.md`.

Anything else remains `review_required`. Matching outputs, matching complexity
labels, algebraic equivalence, or informal inspection cannot silently clear an
entry.

Formatting, compressed code, renamed locals, a different factorization,
reordered helper logic, or an alternative algorithm are not unavoidable
differences. When the clear app-local form should become the canonical native
form, stage a separate native replacement and follow
`LEETCODE_SUBMISSIONS.md`. Never edit current Accepted evidence in place, and
never promote staged bytes before those exact bytes receive an Accepted result.

## Judge-provided models

LeetCode displays models such as `TreeNode`, `ListNode`, `Node`, and `Point` as
commented declarations because its judge provides the live classes. cOde(n)'s
app-local `solve.py` and newly generated editable user template must instead
contain a real, minimal class declaration whenever their `solve(...)` contract
uses that model. A reference may not rely on an invisible runner global or
silence the undefined name with `# noqa: F821`.

Mark these data-only declarations with a class docstring beginning
`Local equivalent of `. Starter generation copies only such validated model
classes and never copies a `Solution` class or an algorithm helper. Runtime
injection remains solely for backward compatibility with already saved user
files; it is not acceptable source-level evidence for a canonical reference.

## Review order

Run the audit before beginning work and after every completed package:

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_solution_alignment.py --allow-review-required
```

Process `first_review_required` in ascending frontend-ID order. A package pass
must compare the complete executable path, not only the public method body:

1. Confirm the native declaration, app `solve(...)` contract, authored cases,
   and any source-native data model.
2. Trace the entry point, every reachable helper, mutations, boundary handling,
   and return construction in both files.
3. Align editable app-local naming and code wherever the platform interface
   permits.
4. Confirm the Optimal bounds in `solution_variants.json` and the derivation in
   `approach.md` describe both implementations.
5. If the remaining difference is truly unavoidable, author a hash-bound
   review. Otherwise stage a clear native replacement for remote verification.
6. Run the package cases, relevant benchmark or certificate validation, the
   alignment audit, and focused regressions.

Problem 3549 is the regression example for this policy: its compressed native
FFT and clearer app FFT are algebraically equivalent, but the rewrite is
avoidable, so the pair remains unresolved until a clean staged native source is
Accepted and promoted.

## Hash-bound review

Only structurally different pairs with unavoidable platform or execution
constraints may contain
`variants/optimal/alignment_review.json`. Its required form is:

```json
{
  "schema_version": 1,
  "status": "reviewed",
  "app_source": "solutions/solve.py",
  "native_source": "solutions/leetcode_python3.py",
  "hashes": {
    "app_sha256": "<sha256>",
    "native_sha256": "<sha256>",
    "solution_variants_sha256": "<sha256>",
    "approach_sha256": "<sha256>"
  },
  "classifications": ["source_native_data_model"],
  "assertions": {
    "same_algorithm": true,
    "same_data_flow": true,
    "same_helper_logic": true,
    "complexity_matches": true,
    "naming_consistent_where_interfaces_permit": true,
    "difference_is_unavoidable": true
  },
  "differences": [
    {
      "aspect": "input and output representation",
      "native": "LeetCode-provided linked nodes",
      "app": "JSON-serializable value lists",
      "rationale": "The app function-call harness serializes authored cases."
    }
  ]
}
```

Allowed classifications are `app_execution_adapter`, `judge_environment`,
`platform_signature`, `source_native_data_model`, and `sql_dialect`. Every
difference must identify the exact native form, app form, and necessity. Any
source, approach, or complexity edit invalidates the stored hashes and returns
the package to the review queue. CRLF and LF checkouts intentionally share the
same canonical text hash; no executable text difference is normalized.

The ordinary audit exits nonzero while the queue is nonempty. Use
`--allow-review-required` only while deliberately working through the queue;
the final corpus gate must run without it.
