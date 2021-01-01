import collections

def bfs_cc(adj, vtx, s, color, visited):            # 하나의 color리스트를 이루는 요소찾기
    visited.append(vtx[s])
    queue = collections.deque(vtx[s])
    while queue:
        ver = queue.popleft()
        visited.append(ver)
        color.append(ver)
        nbr= []
        for i in range(len(vtx)):
            if adj[s][i] == 1 and vtx[i] not in visited:
                nbr.append(i)
        for s in nbr:
            visited.append(vtx[s])
            queue.append(vtx[s])
            

    return color


def find_connected_component(adj, vtx, i):             # 부분그래프 찾기(colorList 구현)
    visited = []
    colorList = []

    for v in adj[i]:        # adj의 i줄을 돌면서
        if vtx[v] not in visited:
            color = bfs_cc(adj, vtx, i, [], visited)
            colorList.append(color)
    
    print(f'그래프 연결성분 개수: {len(colorList)}')
    print(colorList)                                # 부분그래프들 출력
    return len(colorList)

def find_bridges(adj,vtx):                          # 브리지 찾기 [연결삭제해보면서 브리지 판단]
    n = len(vtx)                                    # 길이(정점의 개수)
    count = 0

    for i in range(n):                              # 정점의 수(배열 한줄)만큼 돌면서
        # print(vtx[i])
        for j in range(i+1, n):                     # i+1부터(=자기자신 다음 정점부터)시작해서 n까지 돌면서
            if adj[i][j] != 0:                      # 0아님=1=인접노드이면
                adj[i][j] = adj[i][j] = 0           # 이걸 0으로만들어서 = 연결삭제
                print('hi')
                # print(find_connected_component(adj, i))
                if find_connected_component(adj, vtx, i) < 1:              # 부분그래프의 요소가 1보다 작으면
                    count += 1                                          # 브리지++
                    print("Bridge%d: (%s,%s)" %(count, vtx[i], vtx[j])) # 브리지 출력
                adj[i][j] = adj[i][j] = 1                               # 다시 원상태 복구
    return count


vertex = ['A', 'B', 'C', 'D', 'E', 'F']
adjMat = [[0, 1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 1],
          [1, 1, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]]

print('find_bridges: ')
find_bridges(adjMat, vertex)
print()