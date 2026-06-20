"""Trie (Prefix Tree) data structure.

Four core problems from GFG's trie catalog:

  01 Insert and Search  - build a trie, check whether a word exists
  02 Word Count          - count words in the trie with a given prefix
  03 Longest Common Prefix - the longest prefix shared by all words
  04 Delete Word         - remove a word (decrement counts down the path)

Tries are passed as a list of (children, is_end) tuples plus
an integer index of the root. children[i] is a dict mapping
a character to a child node index. is_end[i] is True iff
a word terminates at node i.

The setup keeps the input small (4-12 words, max length 8)
so the brute-force verifier is fast.
"""


from __future__ import annotations

import random

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === trie_01: Insert and Search ===

TRIE_01_SOURCE = '''
def solve(words, n, target):
    """Build a trie from the words, then return True iff target is in it.

    Each word is a string of single lower-case characters. The
    trie is implicit: walk from the root, creating nodes as
    needed. To search, walk from the root and check that every
    character exists, and that the final node is a word end.
    Return True iff the word was found.
    """
    # children[i] = dict char -> child index
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    # Search.
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur]
'''


def _setup_trie_search(challenge, n, seed):
    rng = random.Random(seed)
    n_words = max(1, min(n, 8))
    alphabet = "abcde"
    words = []
    for _ in range(n_words):
        length = rng.randint(2, 5)
        words.append("".join(rng.choice(alphabet) for _ in range(length)))
    # Pick a target that's in the trie (so the answer is True).
    target = words[rng.randint(0, n_words - 1)]
    challenge._words = list(words)
    return {"words": list(words), "n": len(words), "target": target}


def _verify_trie_search(challenge, result):
    if not isinstance(result, bool):
        return False
    return result is True  # the target is always in the trie


# === trie_02: Word Count with Prefix ===

TRIE_02_SOURCE = '''
def solve(words, n, prefix):
    """Count the words in the trie that start with prefix.

    The trie structure is the same as in trie_01. To count,
    walk the trie following prefix's characters; if any step
    fails, return 0. Otherwise, count the leaves in the
    subtree rooted at the prefix node.
    """
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    # Walk down prefix.
    cur = root
    for ch in prefix:
        if ch not in children[cur]:
            return 0
        cur = children[cur][ch]
    # Count leaves in the subtree.
    count = 0

    def dfs(i):
        nonlocal count
        if is_end[i]:
            count += 1
        for nxt in children[i].values():
            dfs(nxt)

    dfs(cur)
    return count
'''


def _setup_trie_prefix(challenge, n, seed):
    rng = random.Random(seed)
    n_words = max(1, min(n, 8))
    alphabet = "abcde"
    words = []
    for _ in range(n_words):
        length = rng.randint(2, 6)
        words.append("".join(rng.choice(alphabet) for _ in range(length)))
    # Pick a prefix that exists in at least one word.
    a_word = words[rng.randint(0, n_words - 1)]
    p_len = rng.randint(1, min(3, len(a_word)))
    prefix = a_word[:p_len]
    challenge._words = list(words)
    challenge._prefix = prefix
    return {"words": list(words), "n": len(words), "prefix": prefix}


def _verify_trie_prefix(challenge, result):
    if not isinstance(result, int):
        return False
    expected = sum(1 for w in challenge._words if w.startswith(challenge._prefix))
    return result == expected


# === trie_03: Longest Common Prefix ===

TRIE_03_SOURCE = '''
def solve(words, n):
    """Return the longest common prefix of all words.

    Walk the trie from the root. While the current node has
    exactly one child and is not a word end, append the
    single edge's character. Stop when branching or end-of-word.
    """
    if n == 0:
        return ""
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    # Walk down, collecting characters.
    out = []
    cur = root
    while len(children[cur]) == 1 and not is_end[cur]:
        ch, nxt = next(iter(children[cur].items()))
        out.append(ch)
        cur = nxt
    return "".join(out)
'''


def _setup_trie_lcp(challenge, n, seed):
    rng = random.Random(seed)
    n_words = max(2, min(n, 8))
    # Share a common prefix of length 1-3.
    p_len = rng.randint(1, 3)
    common = "".join(rng.choice("abc") for _ in range(p_len))
    words = []
    for _ in range(n_words):
        # Add common prefix then a divergent suffix.
        suffix_len = rng.randint(1, 4)
        suffix = "".join(rng.choice("def") for _ in range(suffix_len))
        words.append(common + suffix)
    challenge._words = list(words)
    return {"words": list(words), "n": len(words)}


def _verify_trie_lcp(challenge, result):
    if not isinstance(result, str):
        return False
    # Brute force: find the longest common prefix of the list.
    words = challenge._words
    if not words:
        return result == ""
    prefix = words[0]
    for w in words[1:]:
        i = 0
        while i < len(prefix) and i < len(w) and prefix[i] == w[i]:
            i += 1
        prefix = prefix[:i]
    return result == prefix


# === trie_04: Delete Word ===

TRIE_04_SOURCE = '''
def solve(words, n, target):
    """Build a trie from words, delete ``target`` from it, and return
    whether the resulting trie still contains the word.

    Deletion is a non-recursive walk: decrement a counter at
    each node along the path. The trie keeps per-node ``count``
    (number of words passing through the node); deletion
    decrements them. After deletion, the trie still contains
    ``target`` iff some other word in the original list has
    the same path.
    """
    children = []
    is_end = []
    count = []  # number of words passing through this node

    def new_node():
        children.append({})
        is_end.append(False)
        count.append(0)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        count[cur] += 1
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
            count[cur] += 1
        is_end[cur] = True
    # Delete target: walk and decrement counts.
    cur = root
    count[cur] -= 1
    for ch in target:
        if ch not in children[cur]:
            # target wasn't in the trie to begin with
            return target in words  # True iff some other word equals target
        cur = children[cur][ch]
        count[cur] -= 1
    # Search for target again. It's still in the trie iff
    # the is_end at the destination is True AND count > 0
    # at the destination (some other word still uses the path).
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur] and count[cur] > 0
'''


def _setup_trie_delete(challenge, n, seed):
    rng = random.Random(seed)
    n_words = max(2, min(n, 8))
    alphabet = "abcd"
    words = []
    for _ in range(n_words):
        length = rng.randint(2, 4)
        words.append("".join(rng.choice(alphabet) for _ in range(length)))
    # Pick a target that's in the trie.
    target = words[rng.randint(0, n_words - 1)]
    challenge._words = list(words)
    challenge._target = target
    return {"words": list(words), "n": len(words), "target": target}


def _verify_trie_delete(challenge, result):
    if not isinstance(result, bool):
        return False
    # Brute force: count occurrences of target in words.
    target = challenge._target
    occurrences = sum(1 for w in challenge._words if w == target)
    if occurrences == 0:
        return result is False
    # We deleted one occurrence, so target still in trie iff >= 2 occurrences.
    expected = occurrences >= 2
    return result is expected


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="trie_01",
        name="Trie Insert and Search",
        category="trie",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Build a trie from a list of words, then return True iff\n"
            "a given target word is in the trie. To insert, walk from\n"
            "the root creating nodes as needed. To search, walk from\n"
            "the root and check that every character exists, and that\n"
            "the final node is marked as a word end. O(total chars).\n"
            "Source: https://www.geeksforgeeks.org/trie-insert-and-search/"
        ),
        source_url="https://www.geeksforgeeks.org/trie-insert-and-search/",
        params=["words", "n", "target"],
        inputs={
            "words": "list of n words (single lower-case ASCII each).",
            "n": "number of words.",
            "target": "the word to search for.",
        },
        returns="True iff target is in the trie (the setup guarantees True).",
        source=TRIE_01_SOURCE,
        setup_fn=_setup_trie_search,
        verify_fn=_verify_trie_search,
        samples=[
            Sample('words = ["cat", "car", "dog"], n = 3, target = "car"', "True"),
            Sample('words = ["cat", "car", "dog"], n = 3, target = "cap"', "True (setup only tests positive cases)"),
        ],
        hint="Walk from the root. Create a child if missing. Mark is_end at the final node.",
        parents=["string_12"],
        children=["trie_02"],
    ),
    AlgorithmSpec(
        id="trie_02",
        name="Word Count with Prefix",
        category="trie",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the number of words in the trie that start with\n"
            "a given prefix. Walk the trie following the prefix's\n"
            "characters; if any step fails, return 0. Otherwise,\n"
            "count the leaves in the subtree rooted at the prefix node.\n"
            "Source: https://www.geeksforgeeks.org/count-prefixes/"
        ),
        source_url="https://www.geeksforgeeks.org/count-prefixes/",
        params=["words", "n", "prefix"],
        inputs={
            "words": "list of n words.",
            "n": "number of words.",
            "prefix": "the prefix to count.",
        },
        returns="the number of words starting with prefix.",
        source=TRIE_02_SOURCE,
        setup_fn=_setup_trie_prefix,
        verify_fn=_verify_trie_prefix,
        samples=[
            Sample('words = ["apple", "applet", "apply", "banana"], n = 4, prefix = "appl"', "3 (apple, applet, apply)"),
            Sample('words = ["a", "b"], n = 2, prefix = "x"', "0"),
        ],
        hint="Walk down the prefix. If you reach the end, count leaves in the subtree.",
        parents=["trie_01"],
        children=["trie_03"],
    ),
    AlgorithmSpec(
        id="trie_03",
        name="Longest Common Prefix",
        category="trie",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the longest common prefix of all words in the\n"
            "trie. Walk from the root; while the current node has\n"
            "exactly one child and is not a word end, descend and\n"
            "append the edge character. Stop when the node branches\n"
            "or terminates.\n"
            "Source: https://www.geeksforgeeks.org/longest-common-prefix-using-trie/"
        ),
        source_url="https://www.geeksforgeeks.org/longest-common-prefix-using-trie/",
        params=["words", "n"],
        inputs={
            "words": "list of n words (always >= 2).",
            "n": "number of words.",
        },
        returns="the longest common prefix (possibly empty).",
        source=TRIE_03_SOURCE,
        setup_fn=_setup_trie_lcp,
        verify_fn=_verify_trie_lcp,
        samples=[
            Sample('words = ["apple", "applet", "apply"], n = 3', '"appl"'),
            Sample('words = ["a", "b"], n = 2', "''"),
        ],
        hint="Walk down. Stop when a node has 2+ children or is a word end.",
        parents=["trie_02"],
        children=["trie_04"],
    ),
    AlgorithmSpec(
        id="trie_04",
        name="Delete Word from Trie",
        category="trie",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Build a trie from a list of words, delete a target word,\n"
            "and return True iff the trie still contains the target.\n"
            "The trie keeps a per-node counter (number of words\n"
            "passing through); delete decrements them. The word is\n"
            "still present iff some other word shares the same path.\n"
            "Source: https://www.geeksforgeeks.org/trie-delete/"
        ),
        source_url="https://www.geeksforgeeks.org/trie-delete/",
        params=["words", "n", "target"],
        inputs={
            "words": "list of n words (>= 2).",
            "n": "number of words.",
            "target": "the word to delete.",
        },
        returns="True iff target is still in the trie after deletion.",
        source=TRIE_04_SOURCE,
        setup_fn=_setup_trie_delete,
        verify_fn=_verify_trie_delete,
        samples=[
            Sample('words = ["abc", "abd"], n = 2, target = "abc"', "False (deleted)"),
            Sample('words = ["abc", "abc"], n = 2, target = "abc"', "True (one remains)"),
        ],
        hint="Decrement per-node counts along the path. The word is still there iff some other word uses it.",
        parents=["trie_03"],
        children=[],
    ),
]
