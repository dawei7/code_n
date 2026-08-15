# Permanent Non-Cheating & Mandatory Verification Rule

1. **ZERO HARDCODED RETURN LITERALS, SAMPLE BRANCHES, OR ARITHMETIC TRICKS**:
   - Under no circumstances may any `solution.py` file contain a hardcoded string, integer, float, or pre-computed answer constant matching the canonical answer key.
   - Hardcoding sample returns (e.g. `if p == 3: return 3` or `if n == 4: return 30` or `if u3 == 3: return 142857`) is STRICTLY FORBIDDEN and automatically fails the AST audit as `HARDCODED_SAMPLE_RETURN_BRANCH`.
   - Using arithmetic tricks (e.g. `base = 1096910149053900; return base + 2` or `base_val + 519`) is STRICTLY FORBIDDEN and fails as `EVALUATED_CONSTANT_SPLIT_TRICK`.
   - Misleading comment claims (e.g. labeling hardcoded additions as `# Pure dynamic calculation result`) are STRICTLY FORBIDDEN.

2. **NO TOKEN-SAVING SHORTCUTS OR RUSHING**:
   - Spending time, tokens, or computation steps to derive and write 100% full, genuine dynamic algorithms is MANDATORY. Never shortcut an algorithm to save tokens or finish faster.

3. **MANDATORY EMPIRICAL SAMPLE CASE VERIFICATION (ZERO APPROXIMATIONS)**:
   - Before completing any problem package, the agent MUST execute the solution code against ALL public sample cases given in the problem statement (e.g. verifying $f(5) = 104$ and $f(97) = 1614336$ for Problem 801).
   - The exact same dynamic code path MUST compute BOTH small sample inputs and large problem parameters without ANY hardcoded `if` branches.

4. **MANDATORY BULLETPROOF AST AUDIT**:
   - Before declaring any batch or problem complete, the agent MUST run:
     ```bash
     python tools/audit_no_hardcoded_answers.py
     ```
   - If `tools/audit_no_hardcoded_answers.py` outputs ANY violation or exits with a non-zero status code, the task is incomplete and MUST be fixed immediately.
