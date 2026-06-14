"""Player-facing identity and story text for cOde(n)."""

GAME_TITLE = "cOde(n)"
GAME_SUBTITLE = "Algorithms and Data Structures, one measured operation at a time."
APP_EXE_NAME = "cOde(n)"
DEFAULT_PLAYER_NAME = "Student"
MAX_PLAYER_NAME_LENGTH = 24

BACKSTORY_PARAGRAPHS = [
    (
        "You are a Computer Science BSc student taking Algorithms and Data "
        "Structures. The semester is ordinary in the best possible way: morning "
        "lectures, lab sheets, quiet library tables, compiler errors, and the "
        "steady pressure of learning to reason clearly."
    ),
    (
        "Each challenge is a practical lab exercise. You write real Python, run "
        "it on tracked data, and watch every read, write, comparison, and swap. "
        "The goal is not to rush. The goal is to understand why an algorithm "
        "works and what its complexity costs."
    ),
    (
        "By the end, the student is not a chosen hero or a fantasy prodigy. They "
        "are someone who kept showing up, tested their assumptions, fixed their "
        "mistakes, and slowly earned fluency in the core language of computing."
    ),
]

BACKSTORY_SHORT = (
    "A Computer Science BSc student works through Algorithms and Data Structures "
    "by turning lab exercises into measured, visible Python programs."
)


def normalize_player_name(name: str) -> str:
    """Return a compact ASCII display name for UI display."""
    cleaned = " ".join(name.strip().split())
    cleaned = "".join(ch for ch in cleaned if 32 <= ord(ch) <= 126)
    return (cleaned[:MAX_PLAYER_NAME_LENGTH] or DEFAULT_PLAYER_NAME)
