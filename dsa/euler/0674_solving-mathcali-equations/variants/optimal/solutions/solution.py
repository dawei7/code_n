"""Project Euler Problem 674: Solving I-equations.

Find the sum of least simultaneous values of all I-expression pairs from I-expressions.txt,
given modulo 10^9 (last 9 digits).
"""

import os
import sys
from typing import Dict, List, Optional, Tuple, Union

_MOD = 1_000_000_000


class Var:
    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = sys.intern(name)


class INode:
    __slots__ = ("a", "b")

    def __init__(self, a: "Term", b: "Term") -> None:
        self.a = a
        self.b = b


Term = Union[Var, INode]


def parse_expr(s: str) -> Term:
    """Parse Expr := Var | I(Expr,Expr) where Var is one or more letters."""
    i = 0
    n = len(s)

    def parse() -> Term:
        nonlocal i
        if i >= n:
            raise ValueError("Unexpected end of input")

        if s[i] == "I":
            i += 2  # skip "I("
            left = parse()
            i += 1  # skip ","
            right = parse()
            i += 1  # skip ")"
            return INode(left, right)

        start = i
        while i < n and s[i].isalpha():
            i += 1
        return Var(s[start:i])

    term = parse()
    return term


def unify(t1: Term, t2: Term) -> Optional[Dict[str, Term]]:
    """First-order unification over free term magma with occurs check."""
    subs: Dict[str, Term] = {}
    occ_cache: Dict[Tuple[str, int], bool] = {}

    def deref(t: Term) -> Term:
        while isinstance(t, Var) and t.name in subs:
            nxt = subs[t.name]
            if isinstance(nxt, Var) and nxt.name in subs:
                subs[t.name] = subs[nxt.name]
            t = nxt
        return t

    def occurs(vname: str, t: Term) -> bool:
        t = deref(t)
        key = (vname, id(t))
        if key in occ_cache:
            return occ_cache[key]

        stack = [t]
        seen_nodes = set()
        while stack:
            cur = deref(stack.pop())
            if isinstance(cur, Var):
                if cur.name == vname:
                    occ_cache[key] = True
                    return True
            else:
                nid = id(cur)
                if nid in seen_nodes:
                    continue
                seen_nodes.add(nid)
                stack.append(cur.a)
                stack.append(cur.b)

        occ_cache[key] = False
        return False

    stack = [(t1, t2)]
    while stack:
        a, b = stack.pop()
        a = deref(a)
        b = deref(b)

        if a is b:
            continue
        if isinstance(a, Var) and isinstance(b, Var) and a.name == b.name:
            continue

        if isinstance(a, Var):
            if occurs(a.name, b):
                return None
            subs[a.name] = b
            continue

        if isinstance(b, Var):
            if occurs(b.name, a):
                return None
            subs[b.name] = a
            continue

        if isinstance(a, INode) and isinstance(b, INode):
            stack.append((a.a, b.a))
            stack.append((a.b, b.b))
            continue

        return None

    return subs


def eval_term(root: Term, subs: Dict[str, Term], mod: Optional[int]) -> int:
    """Evaluate root under substitution subs with all free variables set to 0."""
    memo: Dict[int, int] = {}

    def deref(t: Term) -> Term:
        while isinstance(t, Var) and t.name in subs:
            t = subs[t.name]
        return t

    sys.setrecursionlimit(1_000_000)

    def rec(t: Term) -> int:
        t = deref(t)
        if isinstance(t, Var):
            return 0
        tid = id(t)
        if tid in memo:
            return memo[tid]
        x = rec(t.a)
        y = rec(t.b)
        if mod is None:
            s = 1 + x + y
            v = s * s + y - x
        else:
            s = (1 + x + y) % mod
            v = (s * s + y - x) % mod
        memo[tid] = v
        return v

    return rec(root)


def _load_expressions() -> List[str]:
    cur = os.path.abspath(__file__)
    pkg_dir = cur
    while (
        os.path.basename(pkg_dir) != "0674_solving-mathcali-equations"
        and os.path.dirname(pkg_dir) != pkg_dir
    ):
        pkg_dir = os.path.dirname(pkg_dir)

    txt_path = os.path.join(pkg_dir, "I-expressions.txt")
    with open(txt_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def solve(raw_lines: Optional[List[str]] = None, mod: int = _MOD) -> int:
    """Find sum of least simultaneous values for all pairs of distinct I-expressions."""
    if raw_lines is None:
        raw_lines = _load_expressions()

    terms = [parse_expr(s) for s in raw_lines]
    n = len(terms)
    total = 0

    for i in range(n):
        ti = terms[i]
        for j in range(i + 1, n):
            sub = unify(ti, terms[j])
            if sub is not None:
                total = (total + eval_term(ti, sub, mod)) % mod

    return total


if __name__ == "__main__":
    print(solve())
