from queue import Queue

def bfs_cc(adj, vtx, color, s, visited):            # 하나의 color리스트를 이루는 요소찾기
    queue = Queue()                                 # 큐 객체 생성
    queue.put(vtx[s])                               # 처음정점 큐에 넣기
    visited[s] = True                               # s방문 표시
    color.append(vtx[s])                            # color에도 vtx[s]정점 색칠
    while queue.qsize() !=0:                        # 큐가 공백이 아닐때까지
        ver = queue.get()                           # 큐에서 하나빼고               
        s = vtx.index(ver)                          # s를 vtx[ver]의 값으로 바꾸고
        for i in range(len(vtx)):                   # 인접정점의 길이만큼 돌면서
            if adj[s][i] == 1 and visited[i] == False:  # 인접정점이고, 방문하지 않은 정점이라면
                queue.put(vtx[i])                   # 큐에 해당정점을 넣고
                visited[i] = True                   # 방문표시를 한다
            if vtx[i] not in color:                 # 해당정점이 color에 없으면
                color.append(vtx[i])                # color에 색칠
        
    return color                                    # color반환


def find_connected_component(adj, vtx):             # 부분그래프 찾기(colorList 구현)
    visited = [False]*(len(vtx))                    # visited방문 리스트 초기화
    colorList = []                                  # 각 부분그래프들을 저장할 colorList생성

    for v in range(len(vtx)):                       # 그래프안의 모든 정점들에 대해
        if visited[v] == False:                     # vtx가 방문한 정점이 아니라면
            color = bfs_cc(adj, vtx, [], v, visited)# v를 시작정점으로, 너비우선탐색으로 연결된 정점들을 다 찾은 결과 => color리스트로 저장(하나의 부분 그래프)
            colorList.append(color)                 # colorList에 하나의 부분그래프(color리스트)추가

    return len(colorList)                           # colorList의 길이반환(find_bridge함수에서 사용)
    
    
def find_bridges(adj,vtx):                          # 브리지 찾기 [연결삭제해보면서 브리지 판단]
    n = len(vtx)                                    # 길이(정점의 개수)
    count = 0
    for i in range(n):                              # 정점의 수(배열 한줄)만큼 돌면서
        for j in range(i+1, n):                     # i+1부터(=자기자신 다음 정점부터)시작해서 n까지 돌면서
            if adj[i][j] != 0:                      # 0아님=1=인접정점이면
                adj[i][j] = adj[i][j] = 0           # 이걸 0으로만들어서 = 연결삭제
                if find_connected_component(adj, vtx) > 1:              # 부분그래프의 요소가 1보다 작으면
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
