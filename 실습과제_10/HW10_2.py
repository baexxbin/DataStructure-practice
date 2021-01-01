# 너비우선 탐색
from queue import Queue                         # 큐모듈 import

def bfs(adj, vtx, s):
    visited = [False]*(len(vtx))                # visited 리스트 생성, 정점노드의 개수의 길이만큼
    queue = Queue()                             # 큐 객체 생성
    queue.put(vtx[s])                           # 처음정점 큐 추가
    visited[s] = True                           # 정점s를 방문표시
    while queue.qsize() !=0:                    # 큐가 공백이 아닐때까지
        ver = queue.get()                       # 큐에서 정점하나 빼냄(ver)
        print(ver, end=' ')                      # 빼낸 정점ver 방문했다고 출력
        s = vtx.index(ver)                      # s를 ver의 값으로 변환
        for i in range(len(vtx)):               # 인접정점의 길이만큼 돌면서(=해당정점의 배열한줄길이)
            if adj[s][i] == 1 and visited[i] == False:    # 인접정점을 찾고, 해당정점이 visited가 아닐때
                visited[i] = True                         # 방문했다고 표시
                queue.put(vtx[i])                         # 큐에 넣기


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

print('BFS : ', end="")
bfs(adjMat, vertex, 0)      # 처음 초기값으로 A=0을보냄
print()