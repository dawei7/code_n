"""Challenge tree - defines learning paths and category grouping.

The tree is a DAG (Directed Acyclic Graph) where nodes are challenges
and edges describe suggested learning flow. Challenges remain open so
learners can choose the order that fits their needs.
"""

import json
import os
from dataclasses import dataclass, field
from typing import Optional

from .branding import GAME_TITLE


@dataclass
class TreeNode:
    challenge_id: str
    name: str
    category: str
    children: list[str] = field(default_factory=list)
    parents: list[str] = field(default_factory=list)


# The challenge tree definition
# Format: (id, name, category, [prerequisite_ids])
CHALLENGE_TREE = {
    # === ROOT ===
    "intro_01": TreeNode("intro_01", "Hello Grid", "intro", children=["sort_01", "search_01", "graph_01", "dp_01"]),

    # === SORTING PATH ===
    "sort_01": TreeNode("sort_01", "Bubble Sort", "sorting", children=["sort_02"], parents=["intro_01"]),
    "sort_02": TreeNode("sort_02", "Selection Sort", "sorting", children=["sort_03"], parents=["sort_01"]),
    "sort_03": TreeNode("sort_03", "Insertion Sort", "sorting", children=["sort_04", "sort_05"], parents=["sort_02"]),
    "sort_04": TreeNode("sort_04", "Merge Sort", "sorting", children=["sort_06"], parents=["sort_03"]),
    "sort_05": TreeNode("sort_05", "Quick Sort", "sorting", children=["sort_06"], parents=["sort_03"]),
    "sort_06": TreeNode("sort_06", "Heap Sort", "sorting", children=["sort_07"], parents=["sort_04", "sort_05"]),
    "sort_07": TreeNode("sort_07", "Counting Sort", "sorting", children=[], parents=["sort_06"]),

    # === SEARCHING PATH ===
    "search_01": TreeNode("search_01", "Linear Search", "searching", children=["search_02"], parents=["intro_01"]),
    "search_02": TreeNode("search_02", "Binary Search", "searching", children=["search_03", "search_04"], parents=["search_01"]),
    "search_03": TreeNode("search_03", "BFS Grid", "searching", children=["search_05"], parents=["search_02"]),
    "search_04": TreeNode("search_04", "DFS Grid", "searching", children=["search_05"], parents=["search_02"]),
    "search_05": TreeNode("search_05", "A* Pathfinding", "searching", children=[], parents=["search_03", "search_04"]),

    # === GRAPH PATH ===
    "graph_01": TreeNode("graph_01", "Graph Representation", "graphs", children=["graph_02", "graph_03"], parents=["intro_01"]),
    "graph_02": TreeNode("graph_02", "BFS Traversal", "graphs", children=["graph_04"], parents=["graph_01"]),
    "graph_03": TreeNode("graph_03", "DFS Traversal", "graphs", children=["graph_04"], parents=["graph_01"]),
    "graph_04": TreeNode("graph_04", "Dijkstra", "graphs", children=["graph_05"], parents=["graph_02", "graph_03"]),
    "graph_05": TreeNode("graph_05", "Bellman-Ford", "graphs", children=["graph_06"], parents=["graph_04"]),
    "graph_06": TreeNode("graph_06", "Minimum Spanning Tree", "graphs", children=[], parents=["graph_05"]),

    # === DYNAMIC PROGRAMMING PATH ===
    "dp_01": TreeNode("dp_01", "Fibonacci", "dynamic", children=["dp_02"], parents=["intro_01"]),
    "dp_02": TreeNode("dp_02", "Climbing Stairs", "dynamic", children=["dp_03", "dp_04"], parents=["dp_01"]),
    "dp_03": TreeNode("dp_03", "Knapsack", "dynamic", children=["dp_05"], parents=["dp_02"]),
    "dp_04": TreeNode("dp_04", "Longest Common Subsequence", "dynamic", children=["dp_05"], parents=["dp_02"]),
    "dp_05": TreeNode("dp_05", "Matrix Chain Multiplication", "dynamic", children=[], parents=["dp_03", "dp_04"]),
}


class ChallengeTree:
    """Manages the challenge tree and suggested learning flow."""

    def __init__(self):
        self.nodes = CHALLENGE_TREE

    def get_node(self, challenge_id: str) -> Optional[TreeNode]:
        return self.nodes.get(challenge_id)

    def get_roots(self) -> list[TreeNode]:
        """Get challenges with no prerequisites."""
        return [node for node in self.nodes.values() if not node.parents]

    def get_children(self, challenge_id: str) -> list[TreeNode]:
        node = self.nodes.get(challenge_id)
        if not node:
            return []
        return [self.nodes[cid] for cid in node.children if cid in self.nodes]

    def get_parents(self, challenge_id: str) -> list[TreeNode]:
        node = self.nodes.get(challenge_id)
        if not node:
            return []
        return [self.nodes[pid] for pid in node.parents if pid in self.nodes]

    def is_unlocked(self, challenge_id: str, completed: set[str] | None = None) -> bool:
        """Check if a challenge is open to the learner."""
        return challenge_id in self.nodes

    def get_available(self, completed: set[str]) -> list[TreeNode]:
        """Get all challenges that are open but not currently done."""
        available = []
        for cid, node in self.nodes.items():
            if cid not in completed and self.is_unlocked(cid, completed):
                available.append(node)
        return available

    def get_category_nodes(self, category: str) -> list[TreeNode]:
        return [n for n in self.nodes.values() if n.category == category]

    def render_tree(self, progress) -> str:
        """Render the tree as a text-based visual."""
        lines = []
        lines.append(f"\033[1m=== {GAME_TITLE} Challenge Tree ===\033[0m\n")

        categories = ["intro", "sorting", "searching", "graphs", "dynamic"]
        category_names = {
            "intro": "Introduction",
            "sorting": "Sorting",
            "searching": "Searching",
            "graphs": "Graphs",
            "dynamic": "Dynamic Programming",
        }

        for cat in categories:
            nodes = self.get_category_nodes(cat)
            if not nodes:
                continue
            lines.append(f"\033[1m{category_names.get(cat, cat)}\033[0m")

            for node in nodes:
                status_value = progress.status_for(node.challenge_id)
                if status_value == "done":
                    status = "\033[92mOK\033[0m"
                elif status_value == "failed":
                    status = "\033[91mFAIL\033[0m"
                else:
                    status = "\033[93mOPEN\033[0m"

                indent = "  "
                deps = ""
                if node.children:
                    deps = f" -> [{', '.join(node.children)}]"
                lines.append(f"{indent}{status} {node.challenge_id}: {node.name}{deps}")

            lines.append("")

        return "\n".join(lines)
