def solve(root: dict, k: int) -> str:
    node = root

    while node["val"] == "":
        left = node.get("left")
        if left is None:
            left_length = 0
        elif left["len"] > 0:
            left_length = left["len"]
        else:
            left_length = len(left["val"])

        if k <= left_length:
            node = left
        else:
            k -= left_length
            node = node.get("right")

    return node["val"][k - 1]
