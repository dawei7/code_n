class TextEditor:
    def __init__(self):
        self._left = []
        self._right = []

    def addText(self, text: str) -> None:
        self._left.extend(text)

    def deleteText(self, k: int) -> int:
        deleted = min(k, len(self._left))
        if deleted:
            del self._left[-deleted:]
        return deleted

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self._left))):
            self._right.append(self._left.pop())
        return "".join(self._left[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self._right))):
            self._left.append(self._right.pop())
        return "".join(self._left[-10:])


def solve(operations, arguments):
    editor = None
    output = []

    for operation, values in zip(operations, arguments):
        if operation == "TextEditor":
            editor = TextEditor()
            output.append(None)
        elif operation == "addText":
            output.append(editor.addText(*values))
        elif operation == "deleteText":
            output.append(editor.deleteText(*values))
        elif operation == "cursorLeft":
            output.append(editor.cursorLeft(*values))
        elif operation == "cursorRight":
            output.append(editor.cursorRight(*values))

    return output
