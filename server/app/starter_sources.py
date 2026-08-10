"""Compose instructional editor starters around canonical package templates."""

from __future__ import annotations

import html
import re
from functools import lru_cache

from challenges.spec import AlgorithmSpec
from engine.languages import SupportedLanguage, normalize_language
from server.app.challenge_packages import (
    leetcode_doc_markdown,
    leetcode_solution_variant_complexity,
)


_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
_NUMBERED_TITLE_RE = re.compile(r"^\d+\.\s+")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>]*>")
_FENCE_RE = re.compile(r"^\s*```[^`]*\s*$")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_EXAMPLE_MARKER_RE = re.compile(r"(?i)Example(?:s|\s+\d+)?\s*:\s*$")


def compose_documented_starter(
    spec: AlgorithmSpec,
    language: str,
    template_source: str,
) -> str:
    """Prepend learning context while leaving ``template_source`` unchanged.

    The package's ``template.*`` remains the exact canonical interface on disk.
    This function creates the writable editor starter shown to the learner.
    """

    language_id = normalize_language(language)
    description, examples = _canonical_learning_sections(spec.id)
    if not description:
        description = spec.description.strip()
    if not examples:
        examples = _sample_fallback(spec)

    time_complexity, space_complexity = leetcode_solution_variant_complexity(spec.id)
    if not time_complexity:
        time_complexity = str(spec.required_complexity.value)
    if not space_complexity:
        space_complexity = "Not specified"

    body = "\n\n".join((
        _section("Description", description or "No description is available."),
        _section("Examples", examples or "No source examples are provided."),
        _section(
            "Required Complexity",
            f"Time: {time_complexity}\nSpace: {space_complexity}",
        ),
    ))
    preamble = _comment_block(body, language_id)
    if language_id == "bash" and template_source.startswith("#!"):
        shebang, separator, remainder = template_source.partition("\n")
        if separator:
            return f"{shebang}\n\n{preamble}\n\n{remainder}"
    return f"{preamble}\n\n{template_source}"


@lru_cache(maxsize=4096)
def _canonical_learning_sections(challenge_id: str) -> tuple[str, str]:
    markdown = leetcode_doc_markdown(challenge_id) or ""
    description = _clean_reference_markdown(_named_section(markdown, "description"))
    examples = _clean_reference_markdown(_named_section(markdown, "examples"))
    if not examples:
        examples = _clean_reference_markdown(_embedded_examples(markdown))
        if examples:
            embedded_start = description.find(examples)
            if embedded_start >= 0:
                description = description[:embedded_start].strip()
    return description, examples


def _named_section(markdown: str, requested_title: str) -> str:
    lines = markdown.splitlines()
    start: int | None = None
    section_level = 0
    requested = requested_title.casefold()

    for index, line in enumerate(lines):
        match = _HEADING_RE.match(line.strip())
        if not match:
            continue
        title = _NUMBERED_TITLE_RE.sub("", match.group("title").strip()).casefold()
        if title == requested:
            start = index + 1
            section_level = len(match.group("marks"))
            break

    if start is None:
        return ""

    end = len(lines)
    for index in range(start, len(lines)):
        match = _HEADING_RE.match(lines[index].strip())
        if match and len(match.group("marks")) <= section_level:
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def _embedded_examples(markdown: str) -> str:
    lines = markdown.splitlines()
    start: int | None = None
    enclosing_level = 6

    for index, line in enumerate(lines):
        marker = _HTML_TAG_RE.sub("", line).replace("*", "").replace("`", "").strip()
        # Some imported reference files contain zero-width characters (or the
        # visible mojibake for them) immediately before ``Example``. Requiring
        # the marker to begin at column zero would hide otherwise valid source
        # examples from the starter.
        if _EXAMPLE_MARKER_RE.search(marker):
            start = index
            for previous in range(index - 1, -1, -1):
                heading = _HEADING_RE.match(lines[previous].strip())
                if heading:
                    enclosing_level = len(heading.group("marks"))
                    break
            break

    if start is None:
        return ""

    end = len(lines)
    for index in range(start + 1, len(lines)):
        heading = _HEADING_RE.match(lines[index].strip())
        if heading and len(heading.group("marks")) <= enclosing_level:
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def _clean_reference_markdown(markdown: str) -> str:
    if not markdown:
        return ""
    text = html.unescape(_HTML_COMMENT_RE.sub("", markdown))
    text = text.replace("\u200b", "").replace("\u00e2\u20ac\u2039", "")
    text = _IMAGE_RE.sub(lambda match: match.group(1).strip(), text)
    text = _LINK_RE.sub(lambda match: match.group(1).strip(), text)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = _HTML_TAG_RE.sub("", text)

    cleaned_lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if _FENCE_RE.match(line) or line.strip() == "---":
            continue
        heading = _HEADING_RE.match(line.strip())
        if heading:
            title = _NUMBERED_TITLE_RE.sub("", heading.group("title").strip())
            line = f"{title.rstrip(':')}:"
        line = re.sub(
            r"^-\s+\*\*(Input|Output|Explanation):\*\*\s*",
            r"\1: ",
            line,
            flags=re.IGNORECASE,
        )
        line = line.replace("***", "").replace("**", "").replace("`", "")
        line = _ITALIC_RE.sub(r"\1", line)
        line = re.sub(r"(?<=\w)\*(?=[\s,.;:!?)}\]]|$)", "", line)
        line = re.sub(r"(?<!\w)\*(?=\w)", "", line)
        cleaned_lines.append(line.rstrip())

    text = "\n".join(cleaned_lines).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def _sample_fallback(spec: AlgorithmSpec) -> str:
    lines: list[str] = []
    for index, sample in enumerate(spec.samples, start=1):
        if lines:
            lines.append("")
        lines.extend((
            f"Example {index}:",
            f"Input: {sample.input_repr}",
            f"Output: {sample.output_repr}",
        ))
    return "\n".join(lines)


def _section(title: str, body: str) -> str:
    return f"{title}\n{'-' * len(title)}\n{body.strip()}"


def _comment_block(body: str, language: SupportedLanguage) -> str:
    if language == "python":
        return "\n".join(f"# {line}" if line else "#" for line in body.splitlines())
    if language == "bash":
        return "\n".join(f"# {line}" if line else "#" for line in body.splitlines())

    escaped = body.replace("*/", "* /")
    return f"/*\n{escaped}\n*/"
