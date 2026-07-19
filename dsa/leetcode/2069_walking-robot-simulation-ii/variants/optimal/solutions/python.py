class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4
        self.position = 0
        self.has_moved = False

    def step(self, num: int) -> None:
        self.position = (self.position + num) % self.perimeter
        self.has_moved = True

    def getPos(self) -> list[int]:
        horizontal = self.width - 1
        vertical = self.height - 1
        position = self.position

        if position <= horizontal:
            return [position, 0]
        if position <= horizontal + vertical:
            return [horizontal, position - horizontal]
        if position <= 2 * horizontal + vertical:
            return [2 * horizontal + vertical - position, vertical]
        return [0, self.perimeter - position]

    def getDir(self) -> str:
        horizontal = self.width - 1
        vertical = self.height - 1
        position = self.position

        if position == 0:
            return "South" if self.has_moved else "East"
        if position <= horizontal:
            return "East"
        if position <= horizontal + vertical:
            return "North"
        if position <= 2 * horizontal + vertical:
            return "West"
        return "South"


def solve(operations: list[str], arguments: list[list]) -> list:
    robot: Robot | None = None
    output = []

    for operation, args in zip(operations, arguments):
        if operation == "Robot":
            robot = Robot(args[0], args[1])
            output.append(None)
        elif operation == "step":
            assert robot is not None
            robot.step(args[0])
            output.append(None)
        elif operation == "getPos":
            assert robot is not None
            output.append(robot.getPos())
        elif operation == "getDir":
            assert robot is not None
            output.append(robot.getDir())
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
