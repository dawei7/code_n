class SQL:
    def __init__(self, names: list[str], columns: list[int]) -> None:
        self.tables = {
            name: {
                "columns": column_count,
                "next_id": 1,
                "rows": {},
            }
            for name, column_count in zip(names, columns)
        }

    def ins(self, name: str, row: list[str]) -> bool:
        table = self.tables.get(name)
        if table is None or len(row) != table["columns"]:
            return False

        row_id = table["next_id"]
        table["next_id"] += 1
        table["rows"][row_id] = list(row)
        return True

    def rmv(self, name: str, row_id: int) -> None:
        table = self.tables.get(name)
        if table is not None:
            table["rows"].pop(row_id, None)

    def sel(self, name: str, row_id: int, column_id: int) -> str:
        table = self.tables.get(name)
        if table is None:
            return "<null>"

        row = table["rows"].get(row_id)
        if row is None or not 1 <= column_id <= table["columns"]:
            return "<null>"
        return row[column_id - 1]

    def exp(self, name: str) -> list[str]:
        table = self.tables.get(name)
        if table is None:
            return []
        return [
            f"{row_id}," + ",".join(row)
            for row_id, row in table["rows"].items()
        ]


def solve(operations: list[str], arguments: list[list]) -> list:
    database = None
    output = []

    for operation, values in zip(operations, arguments):
        if operation == "SQL":
            database = SQL(*values)
            output.append(None)
        elif operation == "ins":
            output.append(database.ins(*values))
        elif operation == "rmv":
            output.append(database.rmv(*values))
        elif operation == "sel":
            output.append(database.sel(*values))
        elif operation == "exp":
            output.append(database.exp(*values))

    return output
