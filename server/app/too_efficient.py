"""Detect "too efficient" solutions: hardcoded answers + suspiciously
low op counts.

The player can sometimes produce the correct output without doing
the algorithmic work:

  * **Hardcoded return**: ``def solve(data, n): return [0, 1, 2, 3]``
  * **Accessing private state**: ``return challenge._data`` (which
    bypasses the algorithm)
  * **Skipped work**: returns the expected output from a memoized
    dict, returns a precomputed constant, etc.

This module flags those cases so the engine can mark the run as
not correct. Two complementary checks:

  1. **AST scan** of the player source for the specific patterns
     above. Targeted so legitimate code isn't tripped (e.g.
     ``return arr[i]`` is fine; ``return arr`` is fine; only
     ``return <literal>`` / ``return challenge._*`` are flagged).
  2. **Op-count ratio vs the reference solution**. If the player's
     run is correct but uses ``< 30%`` of the ops the canonical
     optimal solution uses, the player is probably skipping work
     (or the optimal solution is wasteful — in which case we'd
     still want the run flagged for review).

The check is intentionally conservative: false positives cost
players a frustrating "wait, that didn't pass?" moment, so we'd
rather under-flag than over-flag. The 30% threshold is a starting
point and easy to tune later.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from engine.languages import SupportedLanguage, normalize_language
from server.app.source_ops import _statement_end, _strip_comments_and_strings


# Threshold for the op-count ratio check. 0.30 = "user did less
# than 30% of the reference's work". Tunable; lower = stricter
# (more false negatives), higher = looser (more false positives).
DEFAULT_RATIO_THRESHOLD = 0.30


class Reason(Enum):
    OK = "ok"
    HARDCODED = "hardcoded_return"     # `return <literal-list/dict/tuple/set>`
    PRIVATE_STATE = "private_state"    # `return challenge._<name>` or similar
    TOO_CHEAP = "too_cheap"            # op-count ratio below threshold


@dataclass
class CheckResult:
    """Outcome of :func:`check`. ``reason`` is ``Reason.OK`` when
    the source is clean. ``message`` is a short human-readable
    string for the UI; empty when ``reason`` is OK.
    """

    reason: Reason
    message: str = ""

    @property
    def flagged(self) -> bool:
        return self.reason is not Reason.OK


def check(
    user_source: str,
    user_ops: int,
    reference_ops: Optional[int] = None,
    ratio_threshold: float = DEFAULT_RATIO_THRESHOLD,
    language: str | None = "python",
) -> CheckResult:
    """Run the AST scan + op-count ratio check.

    Parameters
    ----------
    user_source:
        The full Python source the player submitted. Parsed with
        :func:`ast.parse`; syntax errors are caught and treated as
        "clean" (the engine's own syntax-error path will already
        have caught the problem before we get here).
    user_ops:
        The number of operations the player's run consumed.
    reference_ops:
        The number of operations the reference solution consumed
        on the same (n, seed). Optional: when ``None``, the ratio
        check is skipped (only the AST scan runs).
    ratio_threshold:
        ``user_ops / reference_ops`` below this is flagged.

    Returns
    -------
    :class:`CheckResult`
    """
    # --- 1. Static source scan ---------------------------------------
    try:
        language_id = normalize_language(language)
    except ValueError:
        language_id = "python"
    ast_result = _scan_source(user_source, language_id)
    if ast_result.flagged:
        return ast_result

    # --- 2. Op-count ratio -----------------------------------------
    if reference_ops is not None and reference_ops > 0 and user_ops > 0:
        ratio = user_ops / reference_ops
        if ratio < ratio_threshold:
            return CheckResult(
                Reason.TOO_CHEAP,
                message=(
                    f"Used {user_ops} ops vs the reference's {reference_ops} "
                    f"({ratio:.0%}). The solution may be skipping work or "
                    f"returning a precomputed answer. Re-run with care."
                ),
            )

    return CheckResult(Reason.OK)


# ---------------------------------------------------------------------------
# AST scanning helpers
# ---------------------------------------------------------------------------

# Names that, when accessed on a `challenge` instance, are private
# state set up by `setup_fn` and not part of the player's contract.
# Reading these is the canonical "cheat" (you have the answer in
# `challenge._data` etc).
_PRIVATE_STATE_ATTRS = {"_data", "_working_data", "_expected"}


def _scan_source(source: str, language: SupportedLanguage) -> CheckResult:
    if language == "python":
        try:
            tree = ast.parse(source)
        except SyntaxError:
            # The engine surfaces a syntax error before this point;
            # nothing to do here.
            return CheckResult(Reason.OK)
        return _scan_ast(tree)
    return _scan_c_family_source(source, language)


def _scan_ast(tree: ast.AST) -> CheckResult:
    """Walk every function in the source and look for flagged returns."""

    class _Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.flag: Optional[CheckResult] = None
            self.literal_returns = 0
            self.other_returns = 0

        def visit_Return(self, node: ast.Return) -> None:  # noqa: N802
            if self.flag is not None:
                return  # already flagged; keep walking for completeness
            value = node.value
            if value is None:
                self.other_returns += 1
                return

            if _is_private_state_access(value):
                self.flag = CheckResult(
                    Reason.PRIVATE_STATE,
                    message=(
                        "Solution reads the challenge's private state "
                        f"({ast.unparse(value)!r}). Use the function arguments."
                    ),
                )
                return
            if _is_literal_container(value):
                self.literal_returns += 1
                return
            self.other_returns += 1
            # Keep visiting in case the return is nested in a tuple
            # like `return (foo, challenge._data)`.
            self.generic_visit(node)

    v = _Visitor()
    v.visit(tree)
    if v.flag:
        return v.flag
    if v.literal_returns and not v.other_returns:
        return CheckResult(
            Reason.HARDCODED,
            message="Solution returns a hardcoded literal container. Compute the result from the inputs.",
        )
    return CheckResult(Reason.OK)


def _scan_c_family_source(source: str, language: SupportedLanguage) -> CheckResult:
    del language
    cleaned = _strip_comments_and_strings(source)
    literal_returns = 0
    other_returns = 0
    for expr in _c_family_return_expressions(cleaned):
        if _is_c_family_private_state_return(expr):
            return CheckResult(
                Reason.PRIVATE_STATE,
                message="Solution returns private challenge state. Use the function arguments.",
            )
        if _is_c_family_literal_container(expr):
            literal_returns += 1
        else:
            other_returns += 1
    if literal_returns and not other_returns:
        return CheckResult(
            Reason.HARDCODED,
            message="Solution returns a hardcoded literal container. Compute the result from the inputs.",
        )
    return CheckResult(Reason.OK)


def _c_family_return_expressions(source: str) -> list[str]:
    expressions: list[str] = []
    for match in re.finditer(r"\breturn\b", source):
        end = _statement_end(source, match.end())
        expr = source[match.end():end].strip()
        if expr.endswith(";"):
            expr = expr[:-1].strip()
        if expr:
            expressions.append(_strip_outer_parentheses(expr))
    return expressions


def _strip_outer_parentheses(expr: str) -> str:
    text = expr.strip()
    while text.startswith("(") and text.endswith(")"):
        close = _matching_paren(text, 0)
        if close != len(text) - 1:
            break
        text = text[1:-1].strip()
    return text


def _matching_paren(text: str, start: int) -> int:
    depth = 0
    for index, ch in enumerate(text[start:], start):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return index
    return -1


def _is_c_family_private_state_return(expr: str) -> bool:
    return bool(re.search(r"(?:^|[.\->])_(?:data|working_data|expected)\b", expr))


def _is_c_family_literal_container(expr: str) -> bool:
    text = _strip_outer_parentheses(expr)
    if text.startswith("[") and text.endswith("]"):
        close = _matching_bracket(text, 0, "[", "]")
        if close == len(text) - 1:
            return _contains_only_literal_atoms(text[1:-1])
    brace_match = _first_top_level_brace_initializer(text)
    if brace_match is not None:
        start, end = brace_match
        prefix = text[:start].strip()
        suffix = text[end + 1:].strip()
        if _literal_initializer_prefix(prefix) and re.fullmatch(r"[\s)]*", suffix):
            return _contains_only_literal_atoms(text[start + 1:end])

    call_match = re.fullmatch(
        r"(?:java\.util\.)?(?:Arrays\.asList|List\.of|Set\.of|Map\.of|Collections\.singleton|Collections\.singletonList|Collections\.singletonMap)\s*\((.*)\)"
        r"|(?:listOf|mutableListOf|setOf|mutableSetOf|mapOf|mutableMapOf)\s*\((.*)\)",
        text,
        flags=re.DOTALL,
    )
    if call_match:
        return _contains_only_literal_atoms(next(group for group in call_match.groups() if group is not None))
    if _is_empty_c_family_container(text):
        return True
    return False


def _is_empty_c_family_container(text: str) -> bool:
    container_names = (
        r"(?:std::)?(?:vector|array|list|deque|set|multiset|map|multimap|unordered_set|unordered_map)",
        r"(?:java\.util\.)?(?:ArrayList|LinkedList|HashSet|TreeSet|HashMap|TreeMap|PriorityQueue)",
        r"(?:System\.Collections\.Generic\.)?(?:List|HashSet|Dictionary|Queue|Stack|SortedSet|SortedDictionary|PriorityQueue)",
        r"(?:Array|Set|Map)",
    )
    container = "|".join(container_names)
    if re.fullmatch(rf"(?:new\s+)?(?:{container})\s*(?:<[^{{}};]*>)?\s*\(\s*\)", text):
        return True
    return bool(re.fullmatch(
        r"(?:java\.util\.)?Collections\.(?:emptyList|emptySet|emptyMap)\s*\(\s*\)"
        r"|(?:System\.)?Array\.Empty\s*<[^>]+>\s*\(\s*\)"
        r"|(?:emptyList|emptySet|emptyMap)\s*<[^>]*>\s*\(\s*\)",
        text,
    ))


def _matching_bracket(text: str, start: int, opener: str, closer: str) -> int:
    depth = 0
    for index, ch in enumerate(text[start:], start):
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return index
    return -1


def _first_top_level_brace_initializer(text: str) -> tuple[int, int] | None:
    paren_depth = 0
    bracket_depth = 0
    for index, ch in enumerate(text):
        if ch == "(":
            paren_depth += 1
        elif ch == ")":
            paren_depth = max(0, paren_depth - 1)
        elif ch == "[":
            bracket_depth += 1
        elif ch == "]":
            bracket_depth = max(0, bracket_depth - 1)
        elif ch == "{" and paren_depth <= 1 and bracket_depth == 0:
            close = _matching_brace(text, index)
            if close >= 0:
                return index, close
    return None


def _matching_brace(text: str, start: int) -> int:
    depth = 0
    for index, ch in enumerate(text[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return index
    return -1


def _literal_initializer_prefix(prefix: str) -> bool:
    if not prefix:
        return True
    cleaned = re.sub(r"<[^{};]*>", "", prefix)
    cleaned = re.sub(r"\[[^\]]*\]", "", cleaned)
    cleaned = cleaned.replace("::", "")
    return bool(re.fullmatch(r"(?:new\s+)?[A-Za-z_][A-Za-z0-9_.,\s()]*", cleaned))


def _contains_only_literal_atoms(contents: str) -> bool:
    text = contents.strip()
    if not text:
        return True
    without_numbers = re.sub(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?[fFdDlLuU]*", " ", text)
    without_punctuation = re.sub(r"[{}\[\](),:\s]", " ", without_numbers)
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\"\"|''|.", without_punctuation)
    allowed_words = {"true", "false", "null", "nullptr", "NaN", "Infinity"}
    for token in tokens:
        if not token.strip():
            continue
        if token in {'""', "''"}:
            continue
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token) and token in allowed_words:
            continue
        return False
    return True


def _is_literal_container(node: ast.AST) -> bool:
    """True iff ``node`` is a list / tuple / set / dict literal.

    Note: we do NOT flag ``return [x for x in arr]`` or
    ``return list(data)`` — those do real work. Only a literal
    of constants is flagged.
    """
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return all(_is_constant(el) for el in node.elts)
    if isinstance(node, ast.Dict):
        return all(
            _is_constant(k) and _is_constant(v)
            for k, v in zip(node.keys, node.values)
        )
    return False


def _is_constant(node: ast.AST) -> bool:
    """True iff ``node`` is a Python literal constant or a
    tuple of constants (the ``(a, b)`` form is a constant in
    Python's AST sense, represented as :class:`ast.Constant`)."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        return _is_constant(node.operand)
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return all(_is_constant(el) for el in node.elts)
    return False


def _is_private_state_access(node: ast.AST) -> bool:
    """True iff ``node`` is a ``challenge._<attr>`` or
    ``self._<attr>`` access, where ``_<attr>`` is in the
    known-private set."""
    if not isinstance(node, ast.Attribute):
        return False
    if node.attr not in _PRIVATE_STATE_ATTRS:
        return False
    # `challenge._data` → Attribute(value=Name(id='challenge'), attr='_data')
    if isinstance(node.value, ast.Name) and node.value.id in {"challenge", "self", "c"}:
        return True
    return False
