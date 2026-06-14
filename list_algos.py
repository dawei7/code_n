"""List all cOde(n) challenges with their existing metadata.

Output: one line per challenge: id, difficulty (1-10), category,
required complexity, name.
"""
from challenges.registry import CHALLENGE_REGISTRY

for cid, cls in sorted(CHALLENGE_REGISTRY.items()):
    spec = cls()._spec
    print(
        f"{cid:18s} | d={spec.difficulty} | "
        f"cat={spec.category:18s} | "
        f"{spec.required_complexity.value:12s} | "
        f"{spec.name}"
    )
