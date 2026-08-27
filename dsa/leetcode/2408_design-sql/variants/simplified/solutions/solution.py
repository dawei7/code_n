from typing import List


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {} for name in names}
        self.cols = {name: col for name, col in zip(names, columns)}
        self.row_ids = {name: 1 for name in names}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables or len(row) != self.cols.get(name, -1):
            return False
        rid = self.row_ids[name]
        self.row_ids[name] += 1
        self.tables[name][rid] = list(row)
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables:
            self.tables[name].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name]:
            return "<null>"
        row = self.tables[name][rowId]
        if 1 <= columnId <= len(row):
            return row[columnId - 1]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        res = []
        for rid in sorted(self.tables[name].keys()):
            row = self.tables[name][rid]
            res.append(f"{rid}," + ",".join(row))
        return res

    def insertRow(self, name: str, row: List[str]) -> bool:
        return self.ins(name, row)

    def deleteRow(self, name: str, rowId: int) -> None:
        self.rmv(name, rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.sel(name, rowId, columnId)
