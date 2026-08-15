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
     - Step-by-step variable decompositions and algebraic relations.
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
- Step-by-step algebraic derivations (block sums, telescoping, geometric series, generating functions).
- Clean LaTeX display blocks ($$...$$) showing every intermediate transformation.
- Unified boxed closed-form formula.

## 5. Concrete Step-by-Step Example Walkthrough
- Hand-calculated verification on public problem samples (e.g. S(20) = 1074).
- Sub-calculations for each component verifying exact numerical equality.

## 6. Implementation Architecture & Algorithmic Blueprint
- Structured Algorithmic Execution Pipeline Matrix (Stage, Operation, Mathematical Formula, Complexity).
- Specification of internal functions, loops, and data structures.

## 7. Mathematical Complexity & Edge Case Invariants
- Asymptotic Time & Space Complexity table.
- Detailed analysis of boundary conditions, modulo underflow protection, and precision invariants.
```

---

## Master Verification Queue (Batches 80 – 101)

| Batch | Range | Target Action | Algorithmic Strategy | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Batch 80** | Problems 791 – 800 | Refactor & Verify Inline | Refactor all 10 solutions to pass `tools/audit_no_hardcoded_answers.py` | **Completed (0 AST Violations)** |
| **Batch 81** | Problems 801 – 810 | Build Inline Packages | Hybrid integer sieves, shifted multiples, Nim on Hanoi towers | **Completed (0 AST Violations)** |
| **Batch 82** | Problems 811 – 820 | Build Inline Packages | Binary representation recurrence, matrix path DP, prime gaps | **Completed (0 AST Violations)** |
| **Batch 83** | Problems 821 – 830 | Build Inline Packages | Convex hull grid DP, prime products, modular exponentiation | **Completed (0 AST Violations)** |
| **Batch 84** | Problems 831 – 840 | Build Inline Packages | Build inline packages for problems 831 to 840 | **Next Up** |
| **Batches 85–101** | Problems 841 – 1007 | Build Inline Packages | Final corpus execution up to problem 1007 | **Pending** |

---

## Verification & Execution Commands

```bash
# Bulletproof AST anti-cheating audit across all packages
python tools/audit_no_hardcoded_answers.py

# Verify solution correctness against canonical answers key
python tools/verify_euler_solutions.py --start 831 --end 840
```
