from typing import List


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {
            name: {
                "columns": column_count,
                "next_id": 1,
                "rows": {},
            }
            for name, column_count in zip(names, columns)
        }

    def ins(self, name: str, row: List[str]) -> bool:
        table = self.tables.get(name)
        if table is None or len(row) != table["columns"]:
            return False

        row_id = table["next_id"]
        table["next_id"] += 1
        table["rows"][row_id] = list(row)
        return True

    def rmv(self, name: str, rowId: int) -> None:
        table = self.tables.get(name)
        if table is not None:
            table["rows"].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables.get(name)
        if table is None:
            return "<null>"

        row = table["rows"].get(rowId)
        if row is None or not 1 <= columnId <= table["columns"]:
            return "<null>"
        return row[columnId - 1]

    def exp(self, name: str) -> List[str]:
        table = self.tables.get(name)
        if table is None:
            return []
        return [f"{row_id}," + ",".join(row) for row_id, row in table["rows"].items()]
