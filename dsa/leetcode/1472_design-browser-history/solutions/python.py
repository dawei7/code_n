class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[: self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


def solve(homepage, operations):
    browser = BrowserHistory(str(homepage))
    output = []
    for raw_operation in operations:
        if not isinstance(raw_operation, list) or not raw_operation:
            continue
        name = str(raw_operation[0])
        args = raw_operation[1] if len(raw_operation) > 1 and isinstance(raw_operation[1], list) else []
        if name == "visit":
            url = str(args[0]) if args else ""
            browser.visit(url)
            output.append(None)
        elif name == "back":
            steps = int(args[0]) if args else 0
            output.append(browser.back(max(0, steps)))
        elif name == "forward":
            steps = int(args[0]) if args else 0
            output.append(browser.forward(max(0, steps)))
    return output
