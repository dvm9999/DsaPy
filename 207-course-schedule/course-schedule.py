class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = defaultdict(list)
        indegree = [0] * numCourses
        for p in prerequisites:
            preq[p[1]].append(p[0])
            indegree[p[0]] += 1
        queue = deque()
        for i, d in enumerate(indegree):
            if not d:
                queue.append(i)
        while queue:
            cc = queue.popleft()
            numCourses -= 1
            for d in preq[cc]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    queue.append(d)
        return numCourses == 0
