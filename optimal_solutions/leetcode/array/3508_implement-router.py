class TrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

class Router:
    def __init__(self):
        self.root = TrieNode()

    def add_route(self, pattern: str, handler: str):
        segments = pattern.strip('/').split('/')
        node = self.root
        for segment in segments:
            if segment not in node.children:
                node.children[segment] = TrieNode()
            node = node.children[segment]
        node.handler = handler

    def resolve(self, url: str) -> str:
        segments = url.strip('/').split('/')
        
        def find_best(node, index):
            if index == len(segments):
                return node.handler
            
            segment = segments[index]
            
            # Try exact match first
            if segment in node.children:
                res = find_best(node.children[segment], index + 1)
                if res: return res
            
            # Try wildcard match
            if '*' in node.children:
                res = find_best(node.children['*'], index + 1)
                if res: return res
                
            return None

        result = find_best(self.root, 0)
        return result if result else ""

def solve(operations, inputs):
    router = Router()
    results = []
    for op, args in zip(operations, inputs):
        if op == "add_route":
            router.add_route(args[0], args[1])
            results.append(None)
        elif op == "resolve":
            results.append(router.resolve(args[0]))
    return results
