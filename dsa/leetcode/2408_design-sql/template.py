class SQL:
    pass

    def __init__(self, names: List[str], columns: List[int]):
        pass
        

    def ins(self, name: str, row: List[str]) -> bool:
        pass
        

    def rmv(self, name: str, rowId: int) -> None:
        pass
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        pass
        

    def exp(self, name: str) -> List[str]:
        pass
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)
