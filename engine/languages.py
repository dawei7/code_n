"""Language metadata shared by the editor, API, and runner."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, get_args


SupportedLanguage = Literal["python", "cpp", "java", "csharp", "javascript", "go", "kotlin", "sql", "bash"]

# The application exposes only the language family used by each problem's
# verified LeetCode submission. The broader SupportedLanguage type remains for
# internal compatibility with legacy runners and personal solution files.
PrimaryLanguage = Literal["python", "javascript", "sql", "bash"]
PRIMARY_LANGUAGES: tuple[PrimaryLanguage, ...] = (
    "python",
    "javascript",
    "sql",
    "bash",
)


@dataclass(frozen=True)
class LanguageInfo:
    id: SupportedLanguage
    label: str
    monaco_language: str
    extension: str


SUPPORTED_LANGUAGES: dict[SupportedLanguage, LanguageInfo] = {
    "python": LanguageInfo("python", "Python", "python", "py"),
    "cpp": LanguageInfo("cpp", "C++", "cpp", "cpp"),
    "java": LanguageInfo("java", "Java", "java", "java"),
    "csharp": LanguageInfo("csharp", "C#", "csharp", "cs"),
    "javascript": LanguageInfo("javascript", "JavaScript", "javascript", "js"),
    "go": LanguageInfo("go", "Go", "go", "go"),
    "kotlin": LanguageInfo("kotlin", "Kotlin", "kotlin", "kt"),
    "sql": LanguageInfo("sql", "SQL", "sql", "sql"),
    "bash": LanguageInfo("bash", "Bash", "shell", "sh"),
}

FUNCTION_LANGUAGES: tuple[SupportedLanguage, ...] = ("python", "cpp", "java", "csharp", "javascript", "go", "kotlin")

LANGUAGE_ALIASES = {
    "py": "python",
    "python3": "python",
    "c++": "cpp",
    "cc": "cpp",
    "cxx": "cpp",
    "cs": "csharp",
    "c#": "csharp",
    "js": "javascript",
    "node": "javascript",
    "nodejs": "javascript",
    "golang": "go",
    "kt": "kotlin",
    "mysql": "sql",
    "sqlite": "sql",
    "sh": "bash",
    "shell": "bash",
}


def normalize_language(language: str | None) -> SupportedLanguage:
    """Return a canonical language id or raise ``ValueError``."""
    raw = (language or "python").strip().lower()
    canonical = LANGUAGE_ALIASES.get(raw, raw)
    if canonical in get_args(SupportedLanguage):
        return canonical  # type: ignore[return-value]
    valid = ", ".join(SUPPORTED_LANGUAGES)
    raise ValueError(f"Unsupported language '{language}'. Expected one of: {valid}")


def language_extension(language: str | None) -> str:
    return SUPPORTED_LANGUAGES[normalize_language(language)].extension


def app_solution_filename(language: str | None) -> str:
    """Return the canonical app-local reference filename for a language."""

    language_id = normalize_language(language)
    if language_id == "sql":
        return "leetcode_sqlite.sql"
    return f"leetcode.{SUPPORTED_LANGUAGES[language_id].extension}"


def leetcode_solution_filename(language: str | None) -> str:
    """Return the canonical source-native LeetCode filename for a language."""

    language_id = normalize_language(language)
    return f"leetcode.{SUPPORTED_LANGUAGES[language_id].extension}"


def candidate_solution_filename(language: str | None) -> str:
    """Return the inert app-contract review-candidate filename for a language."""

    language_id = normalize_language(language)
    return f"candidate.{SUPPORTED_LANGUAGES[language_id].extension}"
