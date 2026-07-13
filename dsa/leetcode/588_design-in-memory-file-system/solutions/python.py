class _Node:
    def __init__(self) -> None:
        self.children: dict[str, _Node] = {}
        self.content: list[str] | None = None


class FileSystem:
    def __init__(self) -> None:
        self.root = _Node()

    @staticmethod
    def _parts(path: str) -> list[str]:
        return [part for part in path.split("/") if part]

    def _walk(self, path: str, *, create: bool = False) -> _Node:
        node = self.root
        for part in self._parts(path):
            if create:
                node = node.children.setdefault(part, _Node())
            else:
                node = node.children[part]
        return node

    def ls(self, path: str) -> list[str]:
        node = self._walk(path)
        if node.content is not None:
            return [self._parts(path)[-1]]
        return sorted(node.children)

    def mkdir(self, path: str) -> None:
        self._walk(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath, create=True)
        if node.content is None:
            node.content = []
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self._walk(filePath)
        return "".join(node.content or [])


def solve(operations: list[list]) -> list:
    file_system = FileSystem()
    results: list = []

    for operation in operations:
        name = operation[0]
        if name == "ls":
            results.append(file_system.ls(operation[1]))
        elif name == "mkdir":
            file_system.mkdir(operation[1])
        elif name == "addContentToFile":
            file_system.addContentToFile(operation[1], operation[2])
        elif name == "readContentFromFile":
            results.append(file_system.readContentFromFile(operation[1]))
        else:
            raise ValueError(f"Unsupported FileSystem operation: {name}")

    return results

