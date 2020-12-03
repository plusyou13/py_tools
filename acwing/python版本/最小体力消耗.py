from collections import deque
from typing import List
import heapq
'''
1631. 最小体力消耗路径
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
请你返回从左上角走到右下角的最小 体力消耗值 。
'''
class Solution:

    # 代码很简洁，一看就明白了。
    # 和一般的BFS不同的是, 使用优先队列代替普通队列，每次从队列中先出路径最小的节点。如果某次出队是终点，那么必是最小路径所达的终点
    # 理解：假如说你比较皮，不是一条路走到底，而是每次给相连的最小消耗的区域涂色，就很好理解了。跟迪杰斯特拉算法很类似。
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        # m为行，n为列
        m, n = len(heights), len(heights[0])
        visit = set()
        nodes = [(0, 0, 0)]  # dis, i, j
        while nodes:
            dis, i, j = heapq.heappop(nodes)
            if i == m - 1 and j == n - 1:
                return dis
            if (i, j) in visit:  # 跳过已经遍历过的点
                continue
            visit.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visit:
                    heapq.heappush(nodes, (max(dis, abs(heights[x][y] - heights[i][j])), x, y))



    # 二分法＋bfs
    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        mat = [[0]*n for _ in range(m)]

        l, r = 0, 999999
        while l < r:
            mid = (l + r)//2
            mat = [[0]*n for _ in range(m)]
            mat[0][0] = 1
            queue = deque([(0, 0)])
            while queue:
                i, j = queue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0<=x<m and 0<=y<n and mat[x][y]==0 and abs(heights[i][j] - heights[x][y]) <= mid:
                        queue.append((x, y))
                        mat[x][y] = 1
            if mat[-1][-1] == 1:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    s=Solution()
    a=s.minimumEffortPath2([[1,2,2],[3,8,2],[5,3,5]])
    print(a)