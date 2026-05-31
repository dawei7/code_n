"""Small input/output examples for challenge instructions."""

from __future__ import annotations


SAMPLES: dict[str, list[tuple[str, str]]] = {
    "intro_01": [
        ("data = [4, 9, 2]", "9"),
        ("data = [7]", "7"),
        ("data = [1, 5, 5, 3]", "5"),
    ],
    "search_01": [
        ("data = [8, 3, 5], target = 3", "1"),
        ("data = [4, 6, 9], target = 7", "-1"),
        ("data = [2, 2, 5], target = 2", "0 or 1"),
    ],
    "search_02": [
        ("data = [2, 4, 7, 9], target = 7", "2"),
        ("data = [1, 5, 8, 12], target = 3", "-1"),
        ("data = [10, 20, 30], target = 10", "0"),
    ],
    "search_03": [
        ("grid = [[0, 0, 0]], start = (0, 0), goal = (0, 2)", "2"),
        ("grid = [[0, 0]], start = (0, 0), goal = (0, 1)", "1"),
        ("grid = [[0, 1, 0], [0, 0, 0], [1, 1, 0]], start = (0, 0), goal = (0, 2)", "4"),
    ],
    "search_04": [
        ("grid = [[0, 0], [0, 0]], start = (0, 0)", "4"),
        ("grid = [[0, 1], [1, 0]], start = (0, 0)", "1"),
        ("grid = [[0, 0, 1]], start = (0, 0)", "2"),
    ],
    "graph_01": [
        ("num_nodes = 3, edges = [(0, 1), (1, 2)]", "{0: [1], 1: [0, 2], 2: [1]}"),
        ("num_nodes = 2, edges = []", "{0: [], 1: []}"),
        ("num_nodes = 3, edges = [(0, 2)]", "{0: [2], 1: [], 2: [0]}"),
    ],
    "graph_04": [
        ("0 --5--> 1", "distance to 1 is 5"),
        ("0 --2--> 1 --3--> 2", "distance to 2 is 5"),
        ("unreachable node", "distance stays infinite / absent"),
    ],
    "dp_01": [
        ("n = 0", "0"),
        ("n = 5", "5"),
        ("n = 8", "21"),
    ],
    "dp_02": [
        ("n = 1", "1"),
        ("n = 3", "3"),
        ("n = 5", "8"),
    ],
    "dp_03": [
        ("weights = [2, 3], values = [4, 5], capacity = 3", "5"),
        ("weights = [1, 2], values = [2, 4], capacity = 3", "6"),
        ("capacity = 0", "0"),
    ],
    "dp_04": [
        ('seq_a = "ABC", seq_b = "AC"', "2"),
        ('seq_a = "ABC", seq_b = "DEF"', "0"),
        ('seq_a = "AAB", seq_b = "AB"', "2"),
    ],
}

SORTING_SAMPLES = [
    ("data = [3, 1, 2]", "[1, 2, 3]"),
    ("data = [5, 5, 2, 9]", "[2, 5, 5, 9]"),
    ("data = [8, 4, 7, 1, 3]", "[1, 3, 4, 7, 8]"),
]


def samples_for(challenge_id: str) -> list[tuple[str, str]]:
    if challenge_id.startswith("sort_"):
        return SORTING_SAMPLES
    return SAMPLES.get(challenge_id, [])


def sample_lines(challenge_id: str) -> list[str]:
    lines: list[str] = []
    for index, (sample_input, sample_output) in enumerate(samples_for(challenge_id), start=1):
        lines.append(f"Sample {index} input:  {sample_input}")
        lines.append(f"Sample {index} output: {sample_output}")
        if index < 3:
            lines.append("")
    return lines


def sample_doc(challenge_id: str, indent: str = "") -> str:
    lines = sample_lines(challenge_id)
    if not lines:
        return ""
    return "Samples:\n" + "\n".join(f"{indent}{line}" if line else "" for line in lines) + "\n\n"
