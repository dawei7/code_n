"""Optimal app-local solution for LeetCode 1166."""


class FileSystem:
    def __init__(self):
        self.paths: dict[str, int] = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        parent = path[: path.rfind("/")]
        if parent and parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


def solve(operations: list[list]) -> list:
    file_system = FileSystem()
    output = []
    for method, arguments in operations:
        if method == "createPath":
            output.append(file_system.createPath(*arguments))
        elif method == "get":
            output.append(file_system.get(*arguments))
        else:
            raise ValueError(f"unknown operation: {method}")
    return output
