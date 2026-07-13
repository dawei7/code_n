"""Utilities for the player's saved solution scripts."""

from __future__ import annotations

import os
import re
import threading
from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from typing import Optional

from .languages import SupportedLanguage, normalize_language
from .samples import sample_doc


# Backwards-compatible source-tree root for external template helpers. User
# data and solutions never live here.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass(frozen=True)
class SolutionPath:
    challenge_id: str
    path: str
    exists: bool


def ensure_solutions_dir() -> str:
    """Return the writable per-user LeetCode overlay root."""
    from server.app.config import USER_LEETCODE_ROOT

    USER_LEETCODE_ROOT.mkdir(parents=True, exist_ok=True)
    return str(USER_LEETCODE_ROOT)


def default_solution_path(challenge_id: str, language: str | None = "python") -> str:
    """Return the selected real version file, never an unversioned alias."""
    from server.app.user_solutions import active_solution_path

    return str(active_solution_path(challenge_id, language, create=True))


def resolve_solution_path(
    challenge_id: str,
    explicit_path: Optional[str] = None,
    language: str | None = "python",
) -> SolutionPath:
    path = explicit_path or default_solution_path(challenge_id, language)
    return SolutionPath(challenge_id=challenge_id, path=path, exists=os.path.exists(path))


def solution_hint(challenge_id: str, language: str | None = "python") -> str:
    path = default_solution_path(challenge_id, language)
    return (
        f"Create your solution at {path}. "
        f"Then run it from the cOde(n) app."
    )


def _build_templates() -> dict[str, dict]:
    """Build the per-challenge template metadata from the registry.

    Each registered :class:`~challenges.spec.AlgorithmSpec` exposes
    ``params``, ``inputs``, and ``returns``; the template generator
    in :func:`_solution_template` consumes those three keys.
    """
    from challenges.registry import get_challenge

    templates: dict[str, dict] = {}
    for challenge_id, _cls in _iter_registered_ids():
        challenge = get_challenge(challenge_id)
        if challenge is None:
            continue
        spec = getattr(challenge, "_spec", None)
        if spec is None:
            continue
        templates[spec.id] = {
            "params": list(spec.params),
            "inputs": dict(spec.inputs),
            "returns": spec.returns,
        }
    return templates


def _iter_registered_ids():
    """Yield ``(id, class)`` pairs in registry-insertion order."""
    from challenges.registry import CHALLENGE_REGISTRY
    for cid, cls in CHALLENGE_REGISTRY.items():
        yield cid, cls


class _LazyChallengeTemplates(Mapping[str, dict]):
    """Derive template metadata only when a template is first requested."""

    def __init__(self) -> None:
        self._data: dict[str, dict] | None = None
        self._lock = threading.Lock()

    @property
    def is_loaded(self) -> bool:
        return self._data is not None

    def load(self) -> dict[str, dict]:
        if self._data is None:
            with self._lock:
                if self._data is None:
                    self._data = _build_templates()
        return self._data

    def __getitem__(self, challenge_id: str) -> dict:
        return self.load()[challenge_id]

    def __iter__(self) -> Iterator[str]:
        return iter(self.load())

    def __len__(self) -> int:
        return len(self.load())


# Backwards-compatible public name. It still behaves like a read-only mapping,
# but importing this module no longer constructs the full challenge corpus.
_CHALLENGE_TEMPLATES: _LazyChallengeTemplates = _LazyChallengeTemplates()


_CPP_KEYWORDS = {
    "alignas",
    "alignof",
    "and",
    "and_eq",
    "asm",
    "auto",
    "bitand",
    "bitor",
    "bool",
    "break",
    "case",
    "catch",
    "char",
    "char8_t",
    "char16_t",
    "char32_t",
    "class",
    "compl",
    "concept",
    "const",
    "consteval",
    "constexpr",
    "constinit",
    "const_cast",
    "continue",
    "co_await",
    "co_return",
    "co_yield",
    "decltype",
    "default",
    "delete",
    "do",
    "double",
    "dynamic_cast",
    "else",
    "enum",
    "explicit",
    "export",
    "extern",
    "false",
    "float",
    "for",
    "friend",
    "goto",
    "if",
    "inline",
    "int",
    "long",
    "mutable",
    "namespace",
    "new",
    "noexcept",
    "not",
    "not_eq",
    "nullptr",
    "operator",
    "or",
    "or_eq",
    "private",
    "protected",
    "public",
    "register",
    "reinterpret_cast",
    "requires",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "static_assert",
    "static_cast",
    "struct",
    "switch",
    "template",
    "this",
    "thread_local",
    "throw",
    "true",
    "try",
    "typedef",
    "typeid",
    "typename",
    "union",
    "unsigned",
    "using",
    "virtual",
    "void",
    "volatile",
    "wchar_t",
    "while",
    "xor",
    "xor_eq",
}

_JAVA_KEYWORDS = {
    "abstract",
    "assert",
    "boolean",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "class",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extends",
    "final",
    "finally",
    "float",
    "for",
    "goto",
    "if",
    "implements",
    "import",
    "instanceof",
    "int",
    "interface",
    "long",
    "native",
    "new",
    "package",
    "private",
    "protected",
    "public",
    "return",
    "short",
    "static",
    "strictfp",
    "super",
    "switch",
    "synchronized",
    "this",
    "throw",
    "throws",
    "transient",
    "try",
    "void",
    "volatile",
    "while",
    "true",
    "false",
    "null",
    "var",
    "yield",
    "record",
    "sealed",
    "permits",
}

_CSHARP_KEYWORDS = {
    "abstract",
    "as",
    "base",
    "bool",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "checked",
    "class",
    "const",
    "continue",
    "decimal",
    "default",
    "delegate",
    "do",
    "double",
    "else",
    "enum",
    "event",
    "explicit",
    "extern",
    "false",
    "finally",
    "fixed",
    "float",
    "for",
    "foreach",
    "goto",
    "if",
    "implicit",
    "in",
    "int",
    "interface",
    "internal",
    "is",
    "lock",
    "long",
    "namespace",
    "new",
    "null",
    "object",
    "operator",
    "out",
    "override",
    "params",
    "private",
    "protected",
    "public",
    "readonly",
    "ref",
    "return",
    "sbyte",
    "sealed",
    "short",
    "sizeof",
    "stackalloc",
    "static",
    "string",
    "struct",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "uint",
    "ulong",
    "unchecked",
    "unsafe",
    "ushort",
    "using",
    "virtual",
    "void",
    "volatile",
    "while",
}

_JAVASCRIPT_KEYWORDS = {
    "await",
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "debugger",
    "default",
    "delete",
    "do",
    "else",
    "export",
    "extends",
    "false",
    "finally",
    "for",
    "function",
    "if",
    "import",
    "in",
    "instanceof",
    "let",
    "new",
    "null",
    "return",
    "super",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "undefined",
    "var",
    "void",
    "while",
    "with",
    "yield",
}

_GO_KEYWORDS = {
    "break",
    "case",
    "chan",
    "const",
    "continue",
    "default",
    "defer",
    "else",
    "fallthrough",
    "for",
    "func",
    "go",
    "goto",
    "if",
    "import",
    "interface",
    "map",
    "package",
    "range",
    "return",
    "select",
    "struct",
    "switch",
    "type",
    "var",
}

_KOTLIN_KEYWORDS = {
    "as",
    "break",
    "class",
    "continue",
    "do",
    "else",
    "false",
    "for",
    "fun",
    "if",
    "in",
    "interface",
    "is",
    "null",
    "object",
    "package",
    "return",
    "super",
    "this",
    "throw",
    "true",
    "try",
    "typealias",
    "typeof",
    "val",
    "var",
    "when",
    "while",
}


def _language_identifier(language: SupportedLanguage, name: str) -> str:
    cleaned = re.sub(r"\W", "_", name)
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"value_{cleaned}"
    if language == "cpp" and cleaned in _CPP_KEYWORDS:
        return f"{cleaned}_"
    if language == "java" and cleaned in _JAVA_KEYWORDS:
        return f"{cleaned}_"
    if language == "csharp" and cleaned in _CSHARP_KEYWORDS:
        return f"@{cleaned}"
    if language == "javascript" and cleaned in _JAVASCRIPT_KEYWORDS:
        return f"{cleaned}_"
    if language == "go" and cleaned in _GO_KEYWORDS:
        return f"{cleaned}_"
    if language == "kotlin" and cleaned in _KOTLIN_KEYWORDS:
        return f"{cleaned}_"
    return cleaned


def _clean_template_description(description: str) -> str:
    """Remove embedded markdown sections from imported challenge text."""
    text = description
    text = re.sub(
        r"\n+##\s+Example\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "").replace("**", "")
    return text.strip()


def _section_block(title: str, body: str) -> str:
    lines = [title, "-" * len(title)]
    if body:
        lines.extend(body.splitlines())
    return "\n".join(lines)


def _solution_header(challenge_id: str, description: str) -> str:
    clean_description = _clean_template_description(description)
    samples = sample_doc(challenge_id)
    blocks = [_section_block("Description", clean_description)]
    blocks.append(_section_block("Examples", samples or "No examples registered."))
    body = "\n\n".join(blocks).rstrip()
    return f'"""\n{body}\n"""\n\n'


def _comment_header(challenge_id: str, description: str, language: SupportedLanguage) -> str:
    clean_description = _clean_template_description(description)
    samples = sample_doc(challenge_id)
    blocks = [_section_block("Description", clean_description)]
    blocks.append(_section_block("Examples", samples or "No examples registered."))
    body = "\n\n".join(blocks).rstrip()
    if language in {"cpp", "java", "csharp", "javascript", "go", "kotlin"}:
        body = body.replace("*/", "* /")
        return f"/*\n{body}\n*/\n\n"
    return _solution_header(challenge_id, description)


def _type_text(text: str) -> str:
    return text.replace("`", "").replace("—", " ").replace("-", " ").lower()


def _name_hint(name: str, type_hint: str) -> str:
    hint = str(type_hint or name)
    return f"{name} {hint}" if name and name != hint else hint


def _has_word(text: str, *words: str) -> bool:
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in words)


def _starts_with_word(text: str, *words: str) -> bool:
    return any(re.match(rf"\s*{re.escape(word)}\b", text) for word in words)


_SCALAR_INT_START_WORDS = (
    "n",
    "m",
    "k",
    "q",
    "target",
    "capacity",
    "amount",
    "size",
    "length",
    "row",
    "col",
    "key",
    "val",
    "value",
    "index",
    "count",
    "src",
    "dest",
    "left",
    "right",
    "divisor",
    "dividend",
)


def _is_bool_hint(text: str) -> bool:
    return _starts_with_word(text, "bool", "boolean") or "true if" in text or "false if" in text


def _is_scalar_int_hint(text: str) -> bool:
    return (
        _starts_with_word(text, *_SCALAR_INT_START_WORDS)
        or bool(re.search(r"\b(?:int|integer|count|index|length)\b", text))
        or any(phrase in text for phrase in ("number of", "total number", "minimum number", "maximum number"))
    )


def _is_char_list_hint(text: str) -> bool:
    return (
        "list[char" in text
        or "list of char" in text
        or _starts_with_word(text, "chars", "characters")
        or ("list" in text and _has_word(text, "characters"))
    )


def _is_char_grid_hint(text: str) -> bool:
    return (
        "list[list[char" in text
        or (
            "board" in text
            and (
                "list[list[str" in text
                or "char" in text
                or "digit" in text
                or "sudoku" in text
                or "'.'" in text
            )
        )
    )


def _is_map_hint(text: str) -> bool:
    return bool(re.search(r"\b(?:dict|map|mapping)\b", text))


def _is_digit_mapping_list_hint(text: str) -> bool:
    return "mapping" in text and (
        "permutation" in text
        or "digit" in text
        or "length 10" in text
        or "length10" in text
    )


def _is_pair_list_hint(text: str) -> bool:
    return (
        "directed pairs" in text
        or "[old, new]" in text
        or "[old,new]" in text
        or "[u, v]" in text
        or "[u,v]" in text
    )


def _is_scalar_string_hint(text: str) -> bool:
    if "list[str" in text or "list of string" in text or "list of word" in text:
        return False
    return (
        "digit string" in text
        or ("integer digits" in text and "list" not in text)
        or "string of" in text
        or "peg name" in text
        or "first string" in text
        or "second string" in text
        or "word to " in text
        or "prefix to " in text
        or (_has_word(text, "str") and "list" not in text)
        or _starts_with_word(text, "str")
        or _starts_with_word(text, "string")
        or ("pattern" in text and "list" not in text and "length" not in text)
    )


def _is_scalar_double_hint(text: str) -> bool:
    return _starts_with_word(text, "eps") or "real number" in text or "float" in text or "double" in text


def _is_double_list_hint(text: str) -> bool:
    return ("list" in text or "array" in text) and (
        "probability" in text
        or "probabilities" in text
        or "item sizes" in text
        or "in (0, 1]" in text
        or _has_word(text, "probs")
        or "list[float" in text
        or "list[double" in text
        or "float" in text
        or "double" in text
    )


def _is_string_list_hint(text: str) -> bool:
    return (
        ("list[str" in text and "list[list[str" not in text)
        or "list of string" in text
        or "string tokens" in text
        or (_has_word(text, "tokens") and ("string" in text or "operands" in text or "operators" in text))
    )


def _is_string_matrix_hint(text: str) -> bool:
    return (
        "list[list[str" in text
        or "list of list of str" in text
        or _has_word(text, "accounts", "equations")
    )


def _is_mixed_string_table_hint(text: str) -> bool:
    return (
        "list of operation tuples" in text
        or "list of (cmd" in text
        or "op_name" in text
        or (
            "operations" in text
            and (
                "list[list" in text
                or "tuple" in text
                or "tuples" in text
                or "*args" in text
            )
        )
    )


def _is_double_matrix_hint(text: str) -> bool:
    return (
        "double matrix" in text
        or "float matrix" in text
        or "real-valued matrix" in text
        or (("list" in text or "matrix" in text) and "polygon vertices" in text)
        or ("list of m (x, y)" in text and ("polygon" in text or "vertices" in text))
    )


def _is_nested_coordinate_matrix_hint(text: str) -> bool:
    return bool(re.search(r"\(\(x\d*, y\d*\), \(x\d*, y\d*\)\)", text))


def _is_level_order_tree_list_hint(text: str) -> bool:
    return (
        bool(re.search(r"\broot\s+list\b", text))
        or "level order binary tree" in text
        or "level-order binary tree" in text
        or "level order tree" in text
        or "level-order tree" in text
        or "bst level-order" in text
        or "bst level order" in text
        or ("list" in text and "tree" in text and ("level" in text or "main tree" in text or "pattern tree" in text))
        or "linked list" in text
    )


def _is_int_table_hint(text: str) -> bool:
    return "list[list]" in text and "[[val" in text


def _is_explicit_int_list_hint(text: str) -> bool:
    return "list[int" in text and "list[list[int" not in text


def _is_long_scalar_hint(text: str) -> bool:
    return bool(re.search(r"\b(?:long\s+long|long\s+integer|long\s+int|int64|64\s+bit\s+(?:signed\s+)?(?:integer|int))\b", text))


def _is_long_list_hint(text: str) -> bool:
    return (
        "list[long" in text
        or "list of long" in text
        or "long array" in text
        or "array of long" in text
        or bool(re.search(r"\b(?:list|array)\s+of\s+64\s+bit\s+(?:signed\s+)?(?:integers|ints)\b", text))
    )


def _is_nullable_long_list_hint(text: str) -> bool:
    return (
        ("long?" in text or "nullable long" in text or "optional long" in text or "optional[long" in text)
        and ("list" in text or "array" in text)
    )


def _is_long_matrix_hint(text: str) -> bool:
    return (
        "list[list[long" in text
        or "list of lists of long" in text
        or "matrix of long" in text
        or "long matrix" in text
    )


def _is_dimension_array_hint(text: str) -> bool:
    return "list of length n+1" in text and "matrix i has shape" in text


def _return_kind(text: str) -> str | None:
    if _is_long_matrix_hint(text):
        return "matrix_long"
    if "list[list[str" in text or "list of list of str" in text:
        return "matrix_string"
    if "list[list[int" in text or "list[list]" in text:
        return "matrix_int"
    if "list[bool" in text:
        return "list_bool"
    if "list[str" in text:
        return "list_string"
    if "list[float" in text or "list[double" in text:
        return "list_double"
    if _is_nullable_long_list_hint(text):
        return "list_nullable_long"
    if _is_long_list_hint(text):
        return "list_long"
    if "list[int" in text:
        return "list_int"
    if "list of bool" in text or "list of boolean" in text:
        return "list_bool"
    if _is_bool_hint(text):
        return "bool"
    if "dict" in text or "mapping" in text or "map" in text:
        if "list" in text or "neighbors" in text:
            return "map_int_list_int"
        return "map_int_int"
    if (
        _starts_with_word(text, "string", "str")
        or "encoded string" in text
        or "longest common prefix" in text
    ):
        return "string"
    if "weighted search cost" in text:
        return "double"
    if _is_long_scalar_hint(text):
        return "long"
    scalar_int_phrases = (
        "the index",
        "first index",
        "the count",
        "the number",
        "number of",
        "total number",
        "minimum number",
        "maximum number",
        "maximum total profit",
        "maximum number of points",
        "maximum sum",
        "kth smallest element",
        "diameter in edges",
        "bitwise and",
    )
    if any(phrase in text for phrase in scalar_int_phrases):
        return "int"
    if "list of n medians" in text or "list of medians" in text:
        return "list_double"
    if (
        "list of lists" in text
        or "each group" in text
        or "each path is a list" in text
        or "each a sorted list" in text
        or "one inner list" in text
        or "list of sccs" in text
        or "list of paths" in text
        or "list of n! permutations" in text
        or "each a list" in text
        or "list of all valid combinations" in text
        or "list of valid combinations" in text
        or "suggestion lists" in text
        or "partitioned triplets" in text
        or "merged sparse vectors" in text
        or "children list" in text
        or "mst edges" in text
        or "edges (u" in text
        or "zero_loss_players" in text
        or "element is the [left, right]" in text
    ):
        if any(word in text for word in ("anagram", "suggestion", "creator_name", "video_id")):
            return "matrix_string"
        return "matrix_int"
    if (
        "list of string" in text
        or "list of n binary strings" in text
        or "binary strings" in text
        or "subsequences" in text
        or "folder paths" in text
        or "recipes" in text
        or "list of words" in text
    ):
        return "list_string"
    if (
        "sorted list" in text
        or "flat list" in text
        or "same list" in text
        or "a list of" in text
        or "the list of" in text
        or "the array after" in text
        or "the sorted list" in text
        or "permutation of" in text
        or "traversal" in text
        or "roundtrip" in text
    ):
        return "list_int"
    if "tree after" in text or "level-order" in text or "level order" in text:
        return "list_nullable_int"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_scalar_int_hint(text):
        return "int"
    return None


def _cpp_return_type(text: str) -> str | None:
    return {
        "bool": "bool",
        "int": "int",
        "long": "long long",
        "double": "double",
        "string": "string",
        "list_bool": "vector<bool>",
        "list_int": "vector<int>",
        "list_long": "vector<long long>",
        "list_nullable_long": "vector<optional<long long>>",
        "list_nullable_int": "vector<optional<int>>",
        "list_double": "vector<double>",
        "list_string": "vector<string>",
        "matrix_int": "vector<vector<int>>",
        "matrix_long": "vector<vector<long long>>",
        "matrix_string": "vector<vector<string>>",
        "map_int_int": "unordered_map<int, int>",
        "map_int_list_int": "unordered_map<int, vector<int>>",
    }.get(_return_kind(text))


def _java_return_type(text: str) -> str | None:
    return {
        "bool": "boolean",
        "int": "int",
        "long": "long",
        "double": "double",
        "string": "String",
        "list_bool": "List<Boolean>",
        "list_int": "List<Integer>",
        "list_long": "List<Long>",
        "list_nullable_long": "List<Long>",
        "list_nullable_int": "List<Integer>",
        "list_double": "List<Double>",
        "list_string": "List<String>",
        "matrix_int": "List<List<Integer>>",
        "matrix_long": "List<List<Long>>",
        "matrix_string": "List<List<String>>",
        "map_int_int": "Map<Integer, Integer>",
        "map_int_list_int": "Map<Integer, List<Integer>>",
    }.get(_return_kind(text))


def _csharp_return_type(text: str) -> str | None:
    return {
        "bool": "bool",
        "int": "int",
        "long": "long",
        "double": "double",
        "string": "string",
        "list_bool": "List<bool>",
        "list_int": "List<int>",
        "list_long": "List<long>",
        "list_nullable_long": "List<long?>",
        "list_nullable_int": "List<int?>",
        "list_double": "List<double>",
        "list_string": "List<string>",
        "matrix_int": "List<List<int>>",
        "matrix_long": "List<List<long>>",
        "matrix_string": "List<List<string>>",
        "map_int_int": "Dictionary<int, int>",
        "map_int_list_int": "Dictionary<int, List<int>>",
    }.get(_return_kind(text))


def _is_counted_matrix_hint(text: str) -> bool:
    is_numeric_tuple_list = (
        "operation" not in text
        and "op_name" not in text
        and "cmd" not in text
        and (
            "list of (" in text
            or "list of n (" in text
            or "list of m (" in text
            or "list of k (" in text
        )
    )
    return (
        bool(re.search(r"\bn\s*x\s*n\b", text))
        or is_numeric_tuple_list
        or "list of n lists" in text
        or "list of length n; children[" in text
        or ("children[" in text and ("[left, right]" in text or "list of" in text))
    )


def _is_generic_int_list_hint(text: str) -> bool:
    if not ("list" in text or "array" in text):
        return False
    if any(word in text for word in ("char", "string", "word", "probability", "float", "double", "bool")):
        return False
    if any(word in text for word in ("tuple", "operation", "matrix", "grid", "maze", "board", "dict", "map")):
        return False
    return (
        "list of n" in text
        or "list of k" in text
        or "list of available" in text
        or "list of length n" in text
        or "array of length" in text
        or "sorted array" in text
    )


def _cpp_type(type_hint: str, *, is_return: bool = False) -> str:
    text = _type_text(type_hint)
    if "void" in text or "in place" in text or (is_return and "none" in text):
        return "void" if is_return else "vector<int>"
    if is_return:
        return_type = _cpp_return_type(text)
        if return_type is not None:
            return return_type
    if _is_bool_hint(text):
        return "bool"
    if _is_digit_mapping_list_hint(text):
        return "vector<int>"
    if _is_pair_list_hint(text):
        return "vector<vector<int>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "unordered_map<int, vector<int>>"
        return "unordered_map<int, int>"
    if _is_scalar_string_hint(text):
        return "string"
    if _is_char_grid_hint(text):
        return "vector<vector<char>>"
    if _is_char_list_hint(text):
        return "vector<char>"
    if _is_mixed_string_table_hint(text):
        return "vector<vector<string>>"
    if _is_string_matrix_hint(text):
        return "vector<vector<string>>"
    if _is_string_list_hint(text):
        return "vector<string>"
    if _is_double_matrix_hint(text):
        return "vector<vector<double>>"
    if _is_double_list_hint(text):
        return "vector<double>"
    if _is_long_matrix_hint(text):
        return "vector<vector<long long>>"
    if _is_nullable_long_list_hint(text):
        return "vector<optional<long long>>"
    if _is_long_list_hint(text):
        return "vector<long long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "vector<vector<int>>"
    if _is_int_table_hint(text):
        return "vector<vector<int>>"
    if _is_level_order_tree_list_hint(text):
        return "vector<optional<int>>"
    if _is_counted_matrix_hint(text):
        return "vector<vector<int>>"
    if _is_explicit_int_list_hint(text):
        return "vector<int>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "vector<int>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "vector<vector<string>>"
    if "list[list[bool" in text:
        return "vector<vector<bool>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "vector<vector<int>>"
    if _has_word(text, "accounts", "equations"):
        return "vector<vector<string>>"
    if "list[str" in text or "list of string" in text:
        return "vector<string>"
    if "list[bool" in text:
        return "vector<bool>"
    if "list[float" in text or "list[double" in text:
        return "vector<double>"
    if "list[long" in text:
        return "vector<long long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "vector<int>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "vector<int>"
    if _is_level_order_tree_list_hint(text):
        return "vector<optional<int>>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "vector<string>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "string"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "vector<int>"
    if "bool" in text:
        return "bool"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "string"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _cpp_parameter_type(type_hint: str, returns_hint: str) -> str:
    cpp_type = _cpp_type(type_hint)
    if "in place" in _type_text(returns_hint) and cpp_type.startswith("vector<"):
        return f"{cpp_type}&"
    return cpp_type


def _java_type(type_hint: str, *, is_return: bool = False) -> str:
    text = _type_text(type_hint)
    if "void" in text or "in place" in text or (is_return and "none" in text):
        return "void" if is_return else "List<Integer>"
    if is_return:
        return_type = _java_return_type(text)
        if return_type is not None:
            return return_type
    if _is_bool_hint(text):
        return "boolean"
    if _is_digit_mapping_list_hint(text):
        return "List<Integer>"
    if _is_pair_list_hint(text):
        return "List<List<Integer>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "Map<Integer, List<Integer>>"
        return "Map<Integer, Integer>"
    if _is_scalar_string_hint(text):
        return "String"
    if _is_char_grid_hint(text):
        return "List<List<Character>>"
    if _is_char_list_hint(text):
        return "List<Character>"
    if _is_mixed_string_table_hint(text):
        return "List<List<String>>"
    if _is_string_matrix_hint(text):
        return "List<List<String>>"
    if _is_string_list_hint(text):
        return "List<String>"
    if _is_double_matrix_hint(text):
        return "List<List<Double>>"
    if _is_double_list_hint(text):
        return "List<Double>"
    if _is_long_matrix_hint(text):
        return "List<List<Long>>"
    if _is_nullable_long_list_hint(text):
        return "List<Long>"
    if _is_long_list_hint(text):
        return "List<Long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "List<List<Integer>>"
    if _is_int_table_hint(text):
        return "List<List<Integer>>"
    if _is_level_order_tree_list_hint(text):
        return "List<Integer>"
    if _is_counted_matrix_hint(text):
        return "List<List<Integer>>"
    if _is_explicit_int_list_hint(text):
        return "List<Integer>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "List<Integer>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "List<List<String>>"
    if "list[list[bool" in text:
        return "List<List<Boolean>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "List<List<Integer>>"
    if _has_word(text, "accounts", "equations"):
        return "List<List<String>>"
    if "list[str" in text or "list of string" in text:
        return "List<String>"
    if "list[bool" in text:
        return "List<Boolean>"
    if "list[float" in text or "list[double" in text:
        return "List<Double>"
    if "list[long" in text:
        return "List<Long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "List<Integer>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "List<Integer>"
    if _is_level_order_tree_list_hint(text):
        return "List<Integer>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "List<String>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "String"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "List<Integer>"
    if "bool" in text:
        return "boolean"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "String"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _csharp_type(type_hint: str, *, is_return: bool = False) -> str:
    text = _type_text(type_hint)
    if "void" in text or "in place" in text or (is_return and "none" in text):
        return "void" if is_return else "List<int>"
    if is_return:
        return_type = _csharp_return_type(text)
        if return_type is not None:
            return return_type
    if _is_bool_hint(text):
        return "bool"
    if _is_digit_mapping_list_hint(text):
        return "List<int>"
    if _is_pair_list_hint(text):
        return "List<List<int>>"
    if _is_map_hint(text):
        if "list" in text or "neighbors" in text:
            return "Dictionary<int, List<int>>"
        return "Dictionary<int, int>"
    if _is_scalar_string_hint(text):
        return "string"
    if _is_char_grid_hint(text):
        return "List<List<char>>"
    if _is_char_list_hint(text):
        return "List<char>"
    if _is_mixed_string_table_hint(text):
        return "List<List<string>>"
    if _is_string_matrix_hint(text):
        return "List<List<string>>"
    if _is_string_list_hint(text):
        return "List<string>"
    if _is_double_matrix_hint(text):
        return "List<List<double>>"
    if _is_double_list_hint(text):
        return "List<double>"
    if _is_long_matrix_hint(text):
        return "List<List<long>>"
    if _is_nullable_long_list_hint(text):
        return "List<long?>"
    if _is_long_list_hint(text):
        return "List<long>"
    if _is_nested_coordinate_matrix_hint(text):
        return "List<List<int>>"
    if _is_int_table_hint(text):
        return "List<List<int>>"
    if _is_level_order_tree_list_hint(text):
        return "List<int?>"
    if _is_counted_matrix_hint(text):
        return "List<List<int>>"
    if _is_explicit_int_list_hint(text):
        return "List<int>"
    if _is_dimension_array_hint(text) or _is_generic_int_list_hint(text):
        return "List<int>"
    if _is_scalar_double_hint(text):
        return "double"
    if _is_long_scalar_hint(text):
        return "long"
    if _starts_with_word(text, *_SCALAR_INT_START_WORDS):
        return "int"
    if "list[list[str" in text or "list of list of str" in text:
        return "List<List<string>>"
    if "list[list[bool" in text:
        return "List<List<bool>>"
    if "list[list[float" in text or "list[list[double" in text:
        return "List<List<double>>"
    if "list[list[long" in text:
        return "List<List<long>>"
    if (
        "list[list[int" in text
        or "list of lists of integers" in text
        or "list of (u, v" in text
        or "list-like of (u, v" in text
        or "list like of (u, v" in text
        or "list of (row" in text
        or "list of (x" in text
        or "list of n (" in text
        or "list of mst edges" in text
        or "edges (u" in text
        or "key points" in text
        or "vertices" in text
        or "list of tuples" in text
        or _is_pair_list_hint(text)
        or "each a list" in text
        or ("board" in text and "list of lists" in text)
        or "matrix" in text
        or "grid" in text
        or _has_word(text, "matrix", "grid", "mat", "edges", "intervals", "meetings", "points", "queries", "trust", "roads", "buildings")
    ):
        return "List<List<int>>"
    if _has_word(text, "accounts", "equations"):
        return "List<List<string>>"
    if "list[str" in text or "list of string" in text:
        return "List<string>"
    if "list[bool" in text:
        return "List<bool>"
    if "list[float" in text or "list[double" in text:
        return "List<double>"
    if "list[long" in text:
        return "List<long>"
    if "list[int" in text or ("list" in text and "int" in text) or "integer array" in text or "array of int" in text:
        return "List<int>"
    if "tuple" in text or "(row, column" in text or "(x, y" in text or "(u, v" in text:
        return "List<int>"
    if _is_level_order_tree_list_hint(text):
        return "List<int?>"
    if _has_word(text, "words", "strs", "dictionary", "word_dict", "worddict", "names", "tokens", "operations"):
        return "List<string>"
    if ("input value" in text or "todo" in text) and _has_word(text, "s", "t", "p", "word", "word1", "word2", "str1", "str2", "text", "pattern", "sentence", "license_plate", "date", "num1", "num2"):
        return "string"
    if _has_word(text, "nums", "nums1", "nums2", "arr", "arr1", "arr2", "list1", "list2", "data", "values", "weights", "prices", "costs", "deadline", "profit", "sizes", "freq", "heights", "temperatures", "digits", "ratings", "answers", "asteroids", "gas", "position", "speed", "piles", "stations"):
        return "List<int>"
    if "bool" in text:
        return "bool"
    if _is_scalar_int_hint(text):
        return "int"
    if "str" in text or "string" in text:
        return "string"
    if "float" in text or "double" in text:
        return "double"
    if _is_long_scalar_hint(text) or "long" in text:
        return "long"
    if "int" in text or "number" in text:
        return "int"
    return "int"


def _go_type(type_hint: str, *, is_return: bool = False) -> str:
    csharp_type = _csharp_type(type_hint, is_return=is_return)
    if csharp_type == "void":
        return ""
    return _go_type_from_csharp(csharp_type)


def _go_type_from_csharp(csharp_type: str) -> str:
    return {
        "bool": "bool",
        "int": "int",
        "long": "int64",
        "double": "float64",
        "string": "string",
        "List<bool>": "[]bool",
        "List<int>": "[]int",
        "List<long>": "[]int64",
        "List<long?>": "[]*int64",
        "List<int?>": "[]*int",
        "List<double>": "[]float64",
        "List<string>": "[]string",
        "List<char>": "[]rune",
        "List<List<bool>>": "[][]bool",
        "List<List<int>>": "[][]int",
        "List<List<long>>": "[][]int64",
        "List<List<double>>": "[][]float64",
        "List<List<string>>": "[][]string",
        "Dictionary<int, int>": "map[int]int",
        "Dictionary<int, List<int>>": "map[int][]int",
    }.get(csharp_type, "int")


def _kotlin_type(type_hint: str, *, is_return: bool = False) -> str:
    csharp_type = _csharp_type(type_hint, is_return=is_return)
    if csharp_type == "void":
        return "Unit"
    return _kotlin_type_from_csharp(csharp_type)


def _kotlin_type_from_csharp(csharp_type: str) -> str:
    return {
        "bool": "Boolean",
        "int": "Int",
        "long": "Long",
        "double": "Double",
        "string": "String",
        "List<bool>": "MutableList<Boolean>",
        "List<int>": "MutableList<Int>",
        "List<long>": "MutableList<Long>",
        "List<long?>": "MutableList<Long?>",
        "List<int?>": "MutableList<Int?>",
        "List<double>": "MutableList<Double>",
        "List<double?>": "MutableList<Double?>",
        "List<string>": "MutableList<String>",
        "List<char>": "MutableList<Char>",
        "List<List<bool>>": "MutableList<MutableList<Boolean>>",
        "List<List<int>>": "MutableList<MutableList<Int>>",
        "List<List<long>>": "MutableList<MutableList<Long>>",
        "List<List<double>>": "MutableList<MutableList<Double>>",
        "List<List<string>>": "MutableList<MutableList<String>>",
        "List<List<char>>": "MutableList<MutableList<Char>>",
        "Dictionary<int, int>": "MutableMap<Int, Int>",
        "Dictionary<int, List<int>>": "MutableMap<Int, MutableList<Int>>",
    }.get(csharp_type, "Int")


def _default_return(language: SupportedLanguage, return_type: str) -> str:
    if return_type == "void":
        return "return;"
    if language == "cpp":
        if return_type == "bool":
            return "return false;"
        if return_type in {"int", "long long"}:
            return "return 0;"
        if return_type == "double":
            return "return 0.0;"
        if return_type == "string":
            return 'return "";'
        return "return {};"
    if language == "java":
        if return_type == "boolean":
            return "return false;"
        if return_type in {"int", "long"}:
            return "return 0;"
        if return_type == "double":
            return "return 0.0;"
        if return_type == "String":
            return 'return "";'
        if return_type.startswith("Map<"):
            return "return new LinkedHashMap<>();"
        return "return new ArrayList<>();"
    if language == "csharp":
        if return_type == "bool":
            return "return false;"
        if return_type in {"int", "long"}:
            return "return 0;"
        if return_type == "double":
            return "return 0.0;"
        if return_type == "string":
            return 'return "";'
        return f"return new {return_type}();"
    if language == "javascript":
        return "return null;"
    if language == "go":
        if not return_type:
            return "return"
        if return_type == "bool":
            return "return false"
        if return_type in {"int", "int64"}:
            return "return 0"
        if return_type == "float64":
            return "return 0.0"
        if return_type == "string":
            return 'return ""'
        return "return nil"
    if language == "kotlin":
        if return_type == "Unit":
            return "return"
        if return_type == "Boolean":
            return "return false"
        if return_type == "Int":
            return "return 0"
        if return_type == "Long":
            return "return 0L"
        if return_type == "Double":
            return "return 0.0"
        if return_type == "String":
            return 'return ""'
        if return_type.startswith("MutableMap<"):
            return "return mutableMapOf()"
        return "return mutableListOf()"
    return "return None"


def _language_types(language: SupportedLanguage, info: dict) -> tuple[str, list[str]]:
    params = list(info["params"])
    inputs = dict(info.get("inputs") or {})
    returns = str(info.get("returns") or "")
    if language == "cpp":
        return_type = _cpp_type(returns, is_return=True)
        return return_type, [
            f"{_cpp_parameter_type(_name_hint(name, inputs.get(name, name)), returns)} {_language_identifier(language, name)}"
            for name in params
        ]
    if language == "java":
        return_type = _java_type(returns, is_return=True)
        return return_type, [
            f"{_java_type(_name_hint(name, inputs.get(name, name)))} {_language_identifier(language, name)}"
            for name in params
        ]
    if language == "csharp":
        return_type = _csharp_type(returns, is_return=True)
        return return_type, [
            f"{_csharp_type(_name_hint(name, inputs.get(name, name)))} {_language_identifier(language, name)}"
            for name in params
        ]
    if language == "javascript":
        return "unknown", [_language_identifier(language, name) for name in params]
    if language == "go":
        return_type = _go_type(returns, is_return=True)
        return return_type, [
            f"{_language_identifier(language, name)} {_go_type(_name_hint(name, inputs.get(name, name)))}"
            for name in params
        ]
    if language == "kotlin":
        return_type = _kotlin_type(returns, is_return=True)
        return return_type, [
            f"{_language_identifier(language, name)}: {_kotlin_type(_name_hint(name, inputs.get(name, name)))}"
            for name in params
        ]
    return "None", params


def _cpp_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "cpp")
    return_type, params = _language_types("cpp", info)
    return (
        header
        + "#include <bits/stdc++.h>\n"
        + "using namespace std;\n\n"
        + "class Solution {\n"
        + "public:\n"
        + f"    {return_type} solve({', '.join(params)}) {{\n"
        + "        // Write your code here.\n"
        + f"        {_default_return('cpp', return_type)}\n"
        + "    }\n"
        + "};\n"
    )


def _java_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "java")
    return_type, params = _language_types("java", info)
    return (
        header
        + "import java.util.*;\n\n"
        + "class Solution {\n"
        + f"    public {return_type} solve({', '.join(params)}) {{\n"
        + "        // Write your code here.\n"
        + f"        {_default_return('java', return_type)}\n"
        + "    }\n"
        + "}\n"
    )


def _csharp_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "csharp")
    return_type, params = _language_types("csharp", info)
    return (
        header
        + "using System;\n"
        + "using System.Collections.Generic;\n"
        + "using System.Linq;\n\n"
        + "public class Solution\n"
        + "{\n"
        + f"    public {return_type} Solve({', '.join(params)})\n"
        + "    {\n"
        + "        // Write your code here.\n"
        + f"        {_default_return('csharp', return_type)}\n"
        + "    }\n"
        + "}\n"
    )


def _javascript_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "javascript")
    _return_type, params = _language_types("javascript", info)
    return (
        header
        + "class Solution {\n"
        + f"    solve({', '.join(params)}) {{\n"
        + "        // Write your code here.\n"
        + f"        {_default_return('javascript', 'unknown')}\n"
        + "    }\n"
        + "}\n\n"
        + "module.exports = { Solution };\n"
    )


def _go_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "go")
    return_type, params = _language_types("go", info)
    return_annotation = f" {return_type}" if return_type else ""
    return (
        header
        + "package main\n\n"
        + f"func solve({', '.join(params)}){return_annotation} {{\n"
        + "    // Write your code here.\n"
        + f"    {_default_return('go', return_type)}\n"
        + "}\n"
    )


def _kotlin_template(challenge_id: str, description: str, info: dict) -> str:
    header = _comment_header(challenge_id, description, "kotlin")
    return_type, params = _language_types("kotlin", info)
    return (
        header
        + "class Solution {\n"
        + f"    fun solve({', '.join(params)}): {return_type} {{\n"
        + "        // Write your code here.\n"
        + f"        {_default_return('kotlin', return_type)}\n"
        + "    }\n"
        + "}\n"
    )


def _solution_template(
    challenge_id: str,
    heading: str,
    description: str,
    language: str | None = "python",
) -> str:
    """Build a starter file for the player.

    Every challenge now has a template with EXPLICIT parameter
    names (no more ``def solve(**kwargs):``). The data comes from
    the registered ``AlgorithmSpec`` while the docstring contains
    only the challenge description and examples.
    """
    language_id = normalize_language(language)
    header = _solution_header(challenge_id, description)

    if language_id == "sql":
        return (
            f"-- {heading}\n"
            "-- Tables are created from the JSON fixture before this query runs.\n"
            "SELECT *\nFROM your_table;\n"
        )
    if language_id == "bash":
        return (
            f"#!/usr/bin/env bash\n# {heading}\n"
            "set -euo pipefail\n\ncat\n"
        )

    info = _CHALLENGE_TEMPLATES.get(challenge_id)
    if info is None:
        # Unknown challenge - fall back to a generic stub. Shouldn't
        # happen in practice; registry.py enumerates the supported
        # IDs.
        return (
            header +
            'def solve():\n'
            '    # Write your code here.\n'
            '    return None\n'
        )

    if language_id == "cpp":
        return _cpp_template(challenge_id, description, info)
    if language_id == "java":
        return _java_template(challenge_id, description, info)
    if language_id == "csharp":
        return _csharp_template(challenge_id, description, info)
    if language_id == "javascript":
        return _javascript_template(challenge_id, description, info)
    if language_id == "go":
        return _go_template(challenge_id, description, info)
    if language_id == "kotlin":
        return _kotlin_template(challenge_id, description, info)

    params = info["params"]
    sig = "def solve(" + ", ".join(params) + "):"

    return (
        header +
        f'{sig}\n'
        f'    # Write your code here.\n'
        f'    return None\n'
    )


def create_solution_file(
    challenge_id: str,
    title: str = "",
    description: str = "",
    language: str | None = "python",
) -> str:
    """Create the saved solution script for a challenge if it does not exist."""
    language_id = normalize_language(language)
    heading = f"{challenge_id}: {title}" if title else challenge_id
    content = _solution_template(challenge_id, heading, description, language_id)
    from server.app.user_solutions import active_solution_path, ensure_solution_versions

    ensure_solution_versions(challenge_id, language_id, content)
    return str(active_solution_path(challenge_id, language_id))
