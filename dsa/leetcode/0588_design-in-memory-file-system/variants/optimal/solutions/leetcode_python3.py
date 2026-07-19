class _Node:
    def __init__(self):
        self.children = {}
        self.content = None


class FileSystem:
    def __init__(self):
        self.root = _Node()

    def _parts(self, path):
        return [part for part in path.split("/") if part]

    def _walk(self, path, create=False):
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
        return "".join(node.content)

