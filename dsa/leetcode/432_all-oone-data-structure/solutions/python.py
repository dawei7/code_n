"""Optimal app-local operation trace for LeetCode 432."""


def solve(operations: list[list[str]]) -> list[str]:
    head = {"count": 0, "keys": set(), "prev": None, "next": None}
    tail = {"count": 0, "keys": set(), "prev": head, "next": None}
    head["next"] = tail
    location = {}
    output: list[str] = []

    def insert_after(previous, count: int):
        following = previous["next"]
        bucket = {"count": count, "keys": set(), "prev": previous, "next": following}
        previous["next"] = bucket
        following["prev"] = bucket
        return bucket

    def remove_bucket(bucket) -> None:
        bucket["prev"]["next"] = bucket["next"]
        bucket["next"]["prev"] = bucket["prev"]

    for operation in operations:
        name = operation[0]
        if name == "inc":
            key = operation[1]
            current = location.get(key, head)
            destination = current["next"]
            target_count = current["count"] + 1
            if destination is tail or destination["count"] != target_count:
                destination = insert_after(current, target_count)
            destination["keys"].add(key)
            location[key] = destination
            if current is not head:
                current["keys"].remove(key)
                if not current["keys"]:
                    remove_bucket(current)
        elif name == "dec":
            key = operation[1]
            current = location[key]
            if current["count"] == 1:
                del location[key]
            else:
                destination = current["prev"]
                target_count = current["count"] - 1
                if destination is head or destination["count"] != target_count:
                    destination = insert_after(destination, target_count)
                destination["keys"].add(key)
                location[key] = destination
            current["keys"].remove(key)
            if not current["keys"]:
                remove_bucket(current)
        elif name == "getMaxKey":
            output.append("" if tail["prev"] is head else next(iter(tail["prev"]["keys"])))
        else:
            output.append("" if head["next"] is tail else next(iter(head["next"]["keys"])))

    return output
