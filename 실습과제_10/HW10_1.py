# 깊이우선 탐색
def dfs_recur(adj, vtx, visited, id):   # vtx(id): 정점 / adj(id): 정점의 인접정점들
    if vtx[id] not in visited:          # vtx(id)가 방문하지 않은 정점이면
        visited.append(vtx[id])         # vtx(id)를 방문노드 집합에 추가
        print(vtx[id], end=' ')         # vtx(id)를 방문했다고 출력
        nbr = []
        for i in range(len(adj[id])):   # vtx(id)의 인접정점의 길이만큼 돌면서 (=해당 정점의 배열한줄의 길이)
            if adj[id][i] == 1 and adj[id][i] not in visited:   # adj[id][i]가 인접정점이고, visited가 아니라면
                # nbr.append(adj[id][i])                        # 인접정점배열에 저장
                nbr.append(i)                                   # 인접정점배열에 인접정점을 나타내는 i를 저장
        for v in nbr:                                           # 인접정점배열을 돌면서
            dfs_recur(adj, vtx, visited, v)                     # v에 대해 함수 순환호출


def dfs(adj, vtx, s):               # 깊이우선 탐색
    n = len(vtx)                    # 길이(정점노드들의 개수)
    # visited = [False]*n           # 초기엔 다 방문안함
    visited = []*n
    dfs_recur(adj, vtx, visited, s) # s:현재정점


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

print('DFS : ', end="")
dfs(adjMat, vertex, 0)
print()