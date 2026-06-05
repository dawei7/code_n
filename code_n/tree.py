"""Challenge tree - defines learning paths and category grouping.

The tree is a DAG (Directed Acyclic Graph) where nodes are challenges
and edges describe suggested learning flow. Challenges remain open so
learners can choose the order that fits their needs.

Sourced from the :class:`~challenges.spec.AlgorithmSpec` registered
for each challenge - the spec carries its own ``parents``/``children``
edges. Adding a new challenge is a one-file change.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .branding import GAME_TITLE


# Canonical display order for categories. New categories added by
# future sessions should append here. Derived dynamically from the
# registry in :func:`_category_order` but pinned so the navigator
# renders in a predictable order regardless of insertion order.
CATEGORIES: list[str] = ["intro", "sorting", "searching", "graphs", "dynamic"]

CATEGORY_NAMES: dict[str, str] = {
    "intro": "Introduction",
    "sorting": "Sorting",
    "searching": "Searching",
    "graphs": "Graphs",
    "dynamic": "Dynamic Programming",
}


@dataclass
class TreeNode:
    challenge_id: str
    name: str
    category: str
    children: list[str] = field(default_factory=list)
    parents: list[str] = field(default_factory=list)


def _build_tree() -> dict[str, TreeNode]:
    """Build the challenge tree from the registry.

    Each :class:`AlgorithmSpec` carries ``parents`` and ``children``
    lists. We turn each into a :class:`TreeNode`. The category field
    on the spec drives grouping; the name and id are taken directly.
    """
    from challenges.registry import CHALLENGE_REGISTRY

    nodes: dict[str, TreeNode] = {}
    # First pass: create every node.
    for cid, cls in CHALLENGE_REGISTRY.items():
        # Pull the spec from a fresh instance so we don't have to
        # introspect the factory class.
        instance = cls()
        spec = getattr(instance, "_spec", None)
        if spec is None:
            # Shouldn't happen - every challenge in the registry is
            # built by make_challenge() which always sets _spec.
            continue
        nodes[cid] = TreeNode(
            challenge_id=spec.id,
            name=spec.name,
            category=spec.category,
            children=list(spec.children),
            parents=list(spec.parents),
        )
    return nodes


CHALLENGE_TREE: dict[str, TreeNode] = _build_tree()


def _category_order() -> list[str]:
    """Return the display order of categories that have at least one node."""
    seen: list[str] = []
    for cat in CATEGORIES:
        if any(node.category == cat for node in CHALLENGE_TREE.values()):
            if cat not in seen:
                seen.append(cat)
    # Any category present in the tree but missing from CATEGORIES
    # gets appended in the order it appears, so adding a new
    # category to a spec never silently hides it.
    for node in CHALLENGE_TREE.values():
        if node.category not in seen:
            seen.append(node.category)
    return seen


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

        for cat in _category_order():
            nodes = self.get_category_nodes(cat)
            if not nodes:
                continue
            lines.append(f"\033[1m{CATEGORY_NAMES.get(cat, cat)}\033[0m")

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
