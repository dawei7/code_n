"""Language-aware static operation counting.

Python keeps the existing AST walker in :mod:`server.app.ast_ops`. For C++,
Java, C#, JavaScript, Go, and Kotlin this module provides a deterministic
structural counter: it strips comments/strings, counts common syntax operations, applies loop-body
multipliers, adds conservative recursion costs, and adds hidden costs for
standard-library algorithms such as sorts, scans, and binary searches.
"""

from __future__ import annotations

import math
import re

from engine.languages import SupportedLanguage, normalize_language
from server.app.ast_ops import count_ops as count_python_ops


def count_ops(source: str, n: int, language: str | None = "python") -> int:
    language_id = normalize_language(language)
    if language_id == "python":
        return count_python_ops(source, n)
    return _count_c_family_ops(source, n, language_id)


def _count_c_family_ops(source: str, n: int, language: SupportedLanguage) -> int:
    cleaned = _strip_comments_and_strings(source)
    return max(0, _count_block(cleaned, max(n, 1), language))


def _strip_comments_and_strings(source: str) -> str:
    out: list[str] = []
    i = 0
    length = len(source)
    while i < length:
        ch = source[i]
        nxt = source[i + 1] if i + 1 < length else ""
        raw_end = _cpp_raw_string_end(source, i)
        if raw_end is not None:
            _append_string_placeholder(out, source, i, raw_end)
            i = raw_end
            continue
        verbatim_end = _csharp_verbatim_string_end(source, i)
        if verbatim_end is not None:
            _append_string_placeholder(out, source, i, verbatim_end)
            i = verbatim_end
            continue
        quoted_raw_end = _triple_quote_string_end(source, i)
        if quoted_raw_end is not None:
            _append_string_placeholder(out, source, i, quoted_raw_end)
            i = quoted_raw_end
            continue
        if ch == "`":
            raw_end = _backtick_string_end(source, i)
            _append_string_placeholder(out, source, i, raw_end)
            i = raw_end
            continue
        if ch == "/" and nxt == "/":
            while i < length and source[i] != "\n":
                i += 1
            out.append("\n")
            continue
        if ch == "/" and nxt == "*":
            i += 2
            while i + 1 < length and not (source[i] == "*" and source[i + 1] == "/"):
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
            i += 2
            continue
        if ch in {'"', "'"}:
            quote = ch
            out.append('""' if quote == '"' else "''")
            i += 1
            while i < length:
                if source[i] == "\\":
                    i += 2
                    continue
                if source[i] == quote:
                    i += 1
                    break
                if source[i] == "\n":
                    out.append("\n")
                i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _append_string_placeholder(out: list[str], source: str, start: int, end: int) -> None:
    out.append('""')
    out.extend("\n" for ch in source[start:end] if ch == "\n")


def _cpp_raw_string_end(source: str, start: int) -> int | None:
    if start + 2 >= len(source) or source[start] != "R" or source[start + 1] != '"':
        return None
    open_paren = source.find("(", start + 2, min(len(source), start + 20))
    if open_paren < 0:
        return None
    delimiter = source[start + 2:open_paren]
    if len(delimiter) > 16 or any(ch.isspace() or ch in {'\\', '(', ')'} for ch in delimiter):
        return None
    close = source.find(f"){delimiter}\"", open_paren + 1)
    return len(source) if close < 0 else close + len(delimiter) + 2


def _csharp_verbatim_string_end(source: str, start: int) -> int | None:
    if source.startswith('$@"', start) or source.startswith('@$"', start):
        i = start + 3
    elif source.startswith('@"', start):
        i = start + 2
    else:
        return None

    while i < len(source):
        if source[i] == '"':
            if i + 1 < len(source) and source[i + 1] == '"':
                i += 2
                continue
            return i + 1
        i += 1
    return len(source)


def _triple_quote_string_end(source: str, start: int) -> int | None:
    if source[start:start + 3] != '"""':
        return None
    quote_count = 0
    while start + quote_count < len(source) and source[start + quote_count] == '"':
        quote_count += 1
    close = source.find('"' * quote_count, start + quote_count)
    return len(source) if close < 0 else close + quote_count


def _backtick_string_end(source: str, start: int) -> int:
    i = start + 1
    while i < len(source):
        if source[i] == "\\":
            i += 2
            continue
        if source[i] == "`":
            return i + 1
        i += 1
    return len(source)


def _count_block(source: str, n: int, language: SupportedLanguage) -> int:
    total = _count_flat_ops(source, n, language)
    for header_start, header_end, body_start, body_end in _loop_bodies(source):
        header = source[header_start:header_end]
        body = source[body_start:body_end]
        body_ops = _count_block(body, n, language)
        # The flat scan already counted the body once. Replace that one count
        # with the loop-weighted count.
        total += (_loop_iterations(header, n) - 1) * body_ops
    return total


def _loop_bodies(source: str) -> list[tuple[int, int, int, int]]:
    bodies: list[tuple[int, int, int, int]] = []
    covered_spans: list[tuple[int, int]] = []
    for do_start, header_start, header_end, body_start, body_end, span_end in _do_while_bodies(source):
        bodies.append((header_start, header_end, body_start, body_end))
        covered_spans.append((do_start, span_end))

    covered_until = -1
    for match in re.finditer(r"\b(?:for|while|foreach)\s*\(", source):
        if match.start() < covered_until or _inside_spans(match.start(), covered_spans):
            continue
        open_paren = source.find("(", match.start())
        close_paren = _matching(source, open_paren, "(", ")")
        if close_paren < 0:
            continue
        body_start = _skip_space(source, close_paren + 1)
        if body_start >= len(source):
            continue
        if source[body_start] == "{":
            close_brace = _matching(source, body_start, "{", "}")
            if close_brace < 0:
                continue
            bodies.append((match.start(), body_start, body_start + 1, close_brace))
            covered_until = close_brace + 1
            continue
        body_end = _statement_end(source, body_start)
        if body_end <= body_start:
            continue
        bodies.append((match.start(), body_start, body_start, body_end))
        covered_until = body_end

    for match in re.finditer(r"\bfor\b", source):
        if match.start() < covered_until or _inside_spans(match.start(), covered_spans):
            continue
        header_start = match.start()
        after_keyword = _skip_space(source, match.end())
        if after_keyword < len(source) and source[after_keyword] == "(":
            continue
        body_start = source.find("{", after_keyword)
        if body_start < 0:
            continue
        close_brace = _matching(source, body_start, "{", "}")
        if close_brace < 0:
            continue
        bodies.append((header_start, body_start, body_start + 1, close_brace))
        covered_until = close_brace + 1
    return bodies


def _do_while_bodies(source: str) -> list[tuple[int, int, int, int, int, int]]:
    bodies: list[tuple[int, int, int, int, int, int]] = []
    for match in re.finditer(r"\bdo\b", source):
        body_start = _skip_space(source, match.end())
        if body_start >= len(source):
            continue
        if source[body_start] == "{":
            close_brace = _matching(source, body_start, "{", "}")
            if close_brace < 0:
                continue
            body_range_start = body_start + 1
            body_range_end = close_brace
            after_body = close_brace + 1
        else:
            body_range_start = body_start
            body_range_end = _statement_end(source, body_start)
            after_body = body_range_end
        while_start = _skip_space(source, after_body)
        while_match = re.match(r"while\s*\(", source[while_start:])
        if while_match is None:
            continue
        header_start = while_start
        open_paren = source.find("(", header_start)
        close_paren = _matching(source, open_paren, "(", ")")
        if close_paren < 0:
            continue
        span_end = _statement_end(source, close_paren + 1)
        bodies.append((
            match.start(),
            header_start,
            close_paren + 1,
            body_range_start,
            body_range_end,
            span_end,
        ))
    return bodies


def _inside_spans(index: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)


def _skip_space(source: str, start: int) -> int:
    index = start
    while index < len(source) and source[index].isspace():
        index += 1
    return index


def _statement_end(source: str, start: int) -> int:
    control_end = _if_statement_end(source, start)
    if control_end is not None:
        return control_end

    paren_depth = 0
    bracket_depth = 0
    brace_depth = 0
    saw_brace = False
    for index in range(start, len(source)):
        ch = source[index]
        if ch == "(":
            paren_depth += 1
        elif ch == ")":
            paren_depth = max(0, paren_depth - 1)
        elif ch == "[":
            bracket_depth += 1
        elif ch == "]":
            bracket_depth = max(0, bracket_depth - 1)
        elif ch == "{":
            brace_depth += 1
            saw_brace = True
        elif ch == "}":
            if brace_depth > 0:
                brace_depth -= 1
                if saw_brace and brace_depth == 0 and paren_depth == 0 and bracket_depth == 0:
                    return index + 1
            elif paren_depth == 0 and bracket_depth == 0:
                return index
        elif ch == ";" and paren_depth == 0 and bracket_depth == 0 and brace_depth == 0:
            return index + 1
    return len(source)


def _if_statement_end(source: str, start: int) -> int | None:
    start = _skip_space(source, start)
    if not _keyword_at(source, start, "if"):
        return None
    open_paren = _skip_space(source, start + len("if"))
    if open_paren >= len(source) or source[open_paren] != "(":
        return None
    close_paren = _matching(source, open_paren, "(", ")")
    if close_paren < 0:
        return None

    then_start = _skip_space(source, close_paren + 1)
    if then_start >= len(source):
        return len(source)
    then_end = _statement_end(source, then_start)
    else_start = _skip_space(source, then_end)
    if _keyword_at(source, else_start, "else"):
        else_body_start = _skip_space(source, else_start + len("else"))
        if else_body_start >= len(source):
            return len(source)
        return _statement_end(source, else_body_start)
    return then_end


def _keyword_at(source: str, index: int, keyword: str) -> bool:
    if not source.startswith(keyword, index):
        return False
    before = source[index - 1] if index > 0 else ""
    after_index = index + len(keyword)
    after = source[after_index] if after_index < len(source) else ""
    return not (before.isalnum() or before == "_") and not (after.isalnum() or after == "_")


def _matching(source: str, start: int, open_char: str, close_char: str) -> int:
    depth = 0
    for index in range(start, len(source)):
        ch = source[index]
        if ch == open_char:
            depth += 1
        elif ch == close_char:
            depth -= 1
            if depth == 0:
                return index
    return -1


def _loop_iterations(header: str, n: int) -> int:
    text = re.sub(r"\s+", "", header)
    if "while(" in text or "foreach(" in text:
        return n
    if re.search(r"\bfor\s*\([^;:]+:", header):
        return n
    if re.search(r"[<>=!]n\b|\bn[<>=!]", text):
        return n
    if re.search(r"\.Length|\.length\(\)|\.size\(\)|Count\b", header):
        return n
    const_match = re.search(r"<\s*(\d+)", header)
    if const_match:
        try:
            return max(0, int(const_match.group(1)))
        except ValueError:
            return n
    return n


def _count_flat_ops(source: str, n: int, language: SupportedLanguage) -> int:
    code = _strip_generic_type_args(_without_declarations(source, language))
    total = 0
    total += len(re.findall(r"==|!=|<=|>=|&&|\|\|", code))
    total += len(re.findall(r"(?<![<>=!])<(?![<>=])|(?<![<>=!])>(?![<>=])", code))
    total += len(re.findall(r"\+\+|--|(?<![+\-])[-+*/%](?![+\-])", code))
    total += len(re.findall(r"(?<![=!<>])=(?!=)", code))
    total += len(re.findall(r"\[[^\]]*\]", code))
    total += len(re.findall(r"\.[A-Za-z_][A-Za-z0-9_]*", code))
    total += _count_calls(code)
    total += _count_library_costs(code, n, language)
    total += _count_recursive_costs(code, n, language)
    total += len(re.findall(r"\breturn\b|\bbreak\b|\bcontinue\b|\bprint(?:ln)?\b|\bConsole\.Write", code))
    total += _count_control_flow_ops(code)
    return total


def _count_control_flow_ops(code: str) -> int:
    total = 0
    total += len(re.findall(r"\bif\s*\(", code))
    total += len(re.findall(r"\bif\b(?!\s*\()", code))
    total += len(re.findall(r"\bfor\b(?!\s*\()", code))
    total += len(re.findall(r"\bswitch\s*\(", code))
    total += len(re.findall(r"\bcase\b|\bdefault\s*:", code))
    total += len(re.findall(r"(?<!\?)\?(?!\?)", code))
    return total


def _without_declarations(source: str, language: SupportedLanguage) -> str:
    lines = []
    declaration_words = (
        "#include",
        "using ",
        "import ",
        "package ",
        "class ",
        "public class",
        "namespace ",
    )
    for line in source.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(declaration_words) and "{" not in stripped:
            continue
        if language == "java" and re.match(r"(public\s+)?static\s+void\s+main\s*\(", stripped):
            continue
        if language == "csharp" and re.match(r"public\s+static\s+void\s+Main\s*\(", stripped):
            continue
        lines.append(line)
    return "\n".join(lines)


def _count_calls(code: str) -> int:
    call_count = 0
    ignored = {
        "if",
        "for",
        "while",
        "switch",
        "catch",
        "return",
        "sizeof",
        "typeof",
        "new",
        "Main",
        "main",
        "solve",
        "Solve",
    }
    for match in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", code):
        if match.group(1) not in ignored:
            call_count += 1
    return call_count


def _count_library_costs(code: str, n: int, language: SupportedLanguage) -> int:
    total = 0
    if language == "cpp":
        total += _n_log_n(n) * len(re.findall(r"\b(?:std::)?(?:sort|stable_sort)\s*\(", code))
        total += n * len(re.findall(r"\b(?:std::)?(?:partial_sort|nth_element)\s*\(", code))
        total += n * len(re.findall(
            r"\b(?:std::)?(?:find|count|accumulate|min_element|max_element|reverse|rotate|fill|copy)\s*\(",
            code,
        ))
        total += _log_n(n) * len(re.findall(
            r"\b(?:std::)?(?:binary_search|lower_bound|upper_bound|equal_range|push_heap|pop_heap)\s*\(",
            code,
        ))
        total += n * len(re.findall(r"\b(?:std::)?make_heap\s*\(", code))
        if re.search(r"\b(?:std::)?priority_queue\b", code):
            total += _log_n(n) * len(re.findall(r"\.(?:push|emplace|pop)\s*\(", code))
        if re.search(r"\b(?:std::)?(?:set|multiset|map|multimap)\b", code):
            total += _log_n(n) * len(re.findall(
                r"\.(?:insert|emplace|erase|find|lower_bound|upper_bound|equal_range)\s*\(",
                code,
            ))
        return total

    if language == "java":
        total += _n_log_n(n) * len(re.findall(r"\b(?:Arrays|Collections)\.sort\s*\(", code))
        total += _log_n(n) * len(re.findall(r"\b(?:Arrays|Collections)\.binarySearch\s*\(", code))
        total += n * len(re.findall(
            r"\b(?:Arrays|Collections)\.(?:fill|copyOf|copyOfRange|reverse|frequency|min|max)\s*\(",
            code,
        ))
        total += n * len(re.findall(r"\.(?:stream|filter|map|flatMap|collect|toArray|forEach)\s*\(", code))
        total += _n_log_n(n) * len(re.findall(r"\.sorted\s*\(", code))
        total += n * len(re.findall(
            r"\.(?:sum|count|max|min|reduce|anyMatch|allMatch|noneMatch|distinct)\s*\("
            r"|\bCollectors\.(?:groupingBy|toMap|toSet|toList)\s*\(",
            code,
        ))
        if re.search(r"\bPriorityQueue\b", code):
            total += _log_n(n) * len(re.findall(r"\.(?:offer|add|poll|remove)\s*\(", code))
        if re.search(r"\b(?:TreeSet|TreeMap)\b", code):
            total += _log_n(n) * len(re.findall(
                r"\.(?:add|put|remove|contains|containsKey|ceiling|floor|higher|lower|firstEntry|lastEntry|pollFirstEntry|pollLastEntry)\s*\(",
                code,
            ))
        return total

    if language == "csharp":
        total += _n_log_n(n) * len(re.findall(r"\bArray\.Sort\s*\(|\.Sort\s*\(", code))
        total += _log_n(n) * len(re.findall(r"\bArray\.BinarySearch\s*\(|\.BinarySearch\s*\(", code))
        total += n * len(re.findall(r"\bArray\.(?:Fill|Copy|Find|FindAll|Exists)\s*\(", code))
        total += _n_log_n(n) * len(re.findall(r"\.(?:OrderBy|OrderByDescending|ThenBy|ThenByDescending)\s*\(", code))
        total += n * len(re.findall(
            r"\.(?:Where|Select|SelectMany|ToArray|ToList|ToDictionary|ToLookup|ForEach|Sum|Count|Max|Min|Aggregate|Any|All|Distinct|GroupBy|Reverse)\s*\(",
            code,
        ))
        if re.search(r"\bPriorityQueue\b", code):
            total += _log_n(n) * len(re.findall(r"\.(?:Enqueue|Dequeue|EnqueueDequeue)\s*\(", code))
        if re.search(r"\b(?:SortedSet|SortedDictionary)\b", code):
            total += _log_n(n) * len(re.findall(
                r"\.(?:Add|Remove|Contains|ContainsKey|TryGetValue|GetValueOrDefault)\s*\(",
                code,
            ))
        return total

    if language == "javascript":
        total += _n_log_n(n) * len(re.findall(r"\.sort\s*\(", code))
        total += n * len(re.findall(
            r"\.(?:map|filter|flatMap|forEach|reduce|some|every|find|findIndex|includes|indexOf|lastIndexOf|reverse|fill|copyWithin)\s*\(",
            code,
        ))
        total += n * len(re.findall(r"\b(?:Array\.from|Object\.keys|Object\.values|Object\.entries)\s*\(", code))
        return total

    if language == "go":
        total += _n_log_n(n) * len(re.findall(
            r"\b(?:sort\.(?:Ints|Float64s|Strings|Slice|SliceStable)|slices\.Sort(?:Func|StableFunc)?)\s*\(",
            code,
        ))
        total += _log_n(n) * len(re.findall(r"\b(?:sort\.Search|slices\.BinarySearch(?:Func)?)\s*\(", code))
        total += n * len(re.findall(
            r"\b(?:copy|clear|append)\s*\(|\b(?:slices|maps)\.(?:Clone|Compact|DeleteFunc|Equal|Index|Contains|Max|Min|Reverse)\s*\(",
            code,
        ))
        if re.search(r"\bheap\.", code):
            total += _log_n(n) * len(re.findall(r"\bheap\.(?:Push|Pop|Remove|Fix)\s*\(", code))
        return total

    if language == "kotlin":
        total += _n_log_n(n) * len(re.findall(
            r"\.(?:sort|sortDescending|sortBy|sortByDescending|sorted|sortedDescending|sortedBy|sortedByDescending)\s*\(",
            code,
        ))
        total += _log_n(n) * len(re.findall(r"\.(?:binarySearch)\s*\(", code))
        total += n * len(re.findall(
            r"\.(?:map|mapNotNull|flatMap|filter|filterNot|forEach|reduce|fold|sum|count|max|min|maxOrNull|minOrNull|any|all|none|distinct|groupBy|associate|associateBy|toList|toSet|toMap|reversed)\s*\(",
            code,
        ))
        if re.search(r"\bPriorityQueue\b", code):
            total += _log_n(n) * len(re.findall(r"\.(?:add|offer|poll|remove)\s*\(", code))
        if re.search(r"\b(?:TreeSet|TreeMap)\b", code):
            total += _log_n(n) * len(re.findall(
                r"\.(?:add|put|remove|contains|containsKey|ceiling|floor|higher|lower|firstEntry|lastEntry|pollFirstEntry|pollLastEntry)\s*\(",
                code,
            ))
        return total

    return total


def _count_recursive_costs(code: str, n: int, language: SupportedLanguage) -> int:
    total = 0
    for name, body in _function_bodies(code):
        recursive_calls = len(re.findall(rf"\b{re.escape(name)}\s*\(", body))
        if recursive_calls == 0:
            continue
        # Exact recursion trees are undecidable from syntax alone. Model a
        # recursive helper as touching up to n subproblems/nodes, using the
        # body's visible work as the per-call cost. This keeps DFS/backtracking
        # and recursive solve() implementations from looking constant-time.
        body_cost = max(1, _count_block(body, n, language))
        total += recursive_calls * max(1, n - 1) * body_cost
    return total


def _function_bodies(code: str) -> list[tuple[str, str]]:
    functions: list[tuple[str, str]] = []
    ignored = {"if", "for", "while", "switch", "catch", "foreach", "return", "new"}
    pattern = re.compile(
        r"\b(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*"
        r"\([^;{}]*\)\s*"
        r"(?:const\s*)?"
        r"(?:->\s*[A-Za-z_][A-Za-z0-9_:<>,\s*&\[\]]+\s*)?"
        r"\{"
    )
    for match in pattern.finditer(code):
        name = match.group("name")
        if name in ignored:
            continue
        open_brace = match.end() - 1
        close_brace = _matching(code, open_brace, "{", "}")
        if close_brace < 0:
            continue
        functions.append((name, code[open_brace + 1:close_brace]))
    return functions


def _n_log_n(size: int) -> int:
    if size <= 1:
        return 1
    return max(1, math.ceil(size * math.log2(size)))


def _log_n(size: int) -> int:
    return max(1, math.ceil(math.log2(max(size, 2))))


def _strip_generic_type_args(code: str) -> str:
    generic_pattern = re.compile(
        r"\b([A-Za-z_][A-Za-z0-9_]*)\s*<\s*[A-Za-z_][A-Za-z0-9_<>,\s]*\s*>"
    )
    previous = None
    while previous != code:
        previous = code
        code = generic_pattern.sub(r"\1", code)
    return code
