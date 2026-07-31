class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0
        self.last = 0

    def visit(self, url):
        self.current += 1
        if self.current == len(self.history):
            self.history.append(url)
        else:
            self.history[self.current] = url
        self.last = self.current

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(self.last, self.current + steps)
        return self.history[self.current]


def solve(homepage, operations):
    browser = BrowserHistory(homepage)
    output = []

    for name, arguments in operations:
        if name == "visit":
            browser.visit(arguments[0])
            output.append(None)
        elif name == "back":
            output.append(browser.back(arguments[0]))
        else:
            output.append(browser.forward(arguments[0]))

    return output
