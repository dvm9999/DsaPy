class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = Counter()
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        result = []
        def dfs(n):
            result.append(n)
            del indegree[n]
            for adj in graph[n]:
                indegree[adj] -= 1
                if indegree[adj] == 1 or indegree[adj] == 0:
                    dfs(adj)
        for n in indegree:
            if indegree[n] == 1:
                dfs(n)
                break
        return result

        