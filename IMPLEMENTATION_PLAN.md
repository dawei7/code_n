# Master Implementation Plan: Project Euler 1007 Corpus Execution & Quality Audit

This document serves as the authoritative, repository-local standard for executing optimal Pure Python solutions and authoring deeply educational mathematical documentation across all 1,007 problem packages in `dsa/euler/`.

---

## User Review & Quality Invariants

> [!CAUTION]
> ### 1. Strict Anti-Cheating & Zero-Shortcut Protocol
> 1. **100% Inline Dynamic Calculation**: Every `solution.py` file MUST dynamically compute its return value using full, genuine mathematical algorithms (DP loops, sieves, recurrences, matrix exponentiation, or numerical iterations).
> 2. **Zero Hardcoded Constant Returns or Offset Tricks**: Hardcoding answer constants, short-circuiting, using conditional fallback branches (`if N > limit: return <constant>`), or using arithmetic offset tricks (`base = 1096910149053900; return base + 2`) is **STRICTLY FORBIDDEN**.
> 3. **Zero Hardcoded Sample Return Branches**: Conditional sample returns (`if p == 3: return 3` or `if n == 4: return 30`) automatically fail the AST audit as `HARDCODED_SAMPLE_RETURN_BRANCH`. The exact same dynamic code path MUST compute BOTH small sample inputs and large problem parameters.
> 4. **Mandatory AST Linter Pass**: Every solution must pass:
>    ```bash
>    python tools/audit_no_hardcoded_answers.py
>    ```
>    with **0 AST violations**.

---

## Standardized `solution.py` Code Architecture

Every `solution.py` must strictly adhere to the following clean structure:

1. **Top-Level `def solve(...) -> int | str:` Function**:
   - `def solve(...)` serves as the top-level entry point and directly returns the calculated answer.
   - **NO `if __name__ == "__main__":` boilerplate blocks**.
2. **Extensive Mathematical & Algorithmic Documentation**:
   - Each `solution.py` must feature an extensive top docstring detailing:
     - The underlying mathematical principles and theorems applied.
     - Step-by-Step variable decompositions and algebraic relations.
     - Asymptotic Time & Space Complexity analysis.
   - Clean, descriptive inline comments explaining each logical phase.
3. **Pure Python Standard Library**:
   - Zero external third-party packages or native binary dependencies.
4. **Memory Safety**:
   - Strict space efficiency ($\mathcal{O}(1)$, $\mathcal{O}(\log N)$, $\mathcal{O}(\sqrt{N})$, or rolling state DP) keeping RAM usage strictly under 100 MB.

---

## Standardized 7-Section Educational `approach.md` Schema

Every package's `variants/optimal/approach.md` must be a self-contained, highly educational document utilizing **pure Markdown tables and LaTeX math blocks ($...$ and $$...$$)** with zero Mermaid/graph dependencies:

```markdown
# [Problem Title] - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation
- Concise problem definition and parameter constraints.
- Clean LaTeX definitions of key sequences, sets, or probability spaces.

## 2. The Naive Approach & Fundamental Bottlenecks
- Exact naive brute-force algorithm (with code snippet).
- Quantitative complexity bottlenecks (operations count, CPU execution time, memory bounds).

## 3. Core Intuition & Mathematical Structure
- Intuitive breakthrough and conceptual decomposition.
- Mathematical Decomposition Table explaining each variable/component.
- Concrete Small-Value Verification Table tracing early terms.

## 4. Rigorous Mathematical Breakthrough & Derivations
- Step-by-Step algebraic derivations (block sums, telescoping, geometric series, generating functions).
- Clean LaTeX display blocks ($$...$$) showing every intermediate transformation.
- Unified boxed closed-form formula.

## 5. Concrete Step-by-Step Example Walkthrough
- Hand-calculated verification on public problem samples.
- Sub-calculations for each component verifying exact numerical equality.

## 6. Implementation Architecture & Algorithmic Blueprint
- Structured Algorithmic Execution Pipeline Matrix (Stage, Operation, Mathematical Formula, Complexity).
- Specification of internal functions, loops, and data structures.

## 7. Mathematical Complexity & Edge Case Invariants
- Asymptotic Time & Space Complexity table.
- Detailed analysis of boundary conditions, modulo underflow protection, and precision invariants.
```

---

## Master Verification Queue (Problems 1 – 1007 Fresh Start)

| Batch | Range | Target Action | Status |
| :--- | :--- | :--- | :--- |
| **Batch 1** | Problems 1 – 10 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 2** | Problems 11 – 20 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 3** | Problems 21 – 30 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 4** | Problems 31 – 40 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 5** | Problems 41 – 50 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 6** | Problems 51 – 60 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 7** | Problems 61 – 70 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 8** | Problems 71 – 80 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 9** | Problems 81 – 90 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 10** | Problems 91 – 100 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 11** | Problems 101 – 110 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 12** | Problems 111 – 120 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 13** | Problems 121 – 130 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 14** | Problems 131 – 140 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 15** | Problems 141 – 150 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 16** | Problems 151 – 160 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 17** | Problems 161 – 170 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 18** | Problems 171 – 180 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 19** | Problems 181 – 190 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 20** | Problems 191 – 200 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 21** | Problems 201 – 210 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 22** | Problems 211 – 220 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 23** | Problems 221 – 230 | Refactor to New Standard & Verify | **Completed (10/10 Passed, 0 AST Violations)** |
| **Batch 24** | Problems 231 – 240 | Refactor to New Standard & Verify | **In Progress (Starting at Problem 231)** |
| **Batches 25–101** | Problems 241 – 1007 | Refactor to New Standard & Verify | **Pending** |

---

## Verification & Execution Commands

```bash
# Bulletproof AST anti-cheating audit across all packages
python tools/audit_no_hardcoded_answers.py

# Verify solution correctness against canonical answers key
python tools/verify_euler_solutions.py --start 1 --end 230
```
