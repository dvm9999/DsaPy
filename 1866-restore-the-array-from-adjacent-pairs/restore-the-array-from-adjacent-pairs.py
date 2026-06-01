class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:        
        graph = defaultdict(list)
        res = []
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)        
        visited = set()
        def dfs(n):
            visited.add(n)
            res.append(n)
            for a in graph[n]:
                if a not in visited:
                    dfs(a)
        
        for v in graph:
            if len(graph[v]) == 1:
                dfs(v)
                break
        return res       