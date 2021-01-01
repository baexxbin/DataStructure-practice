# 파이썬의 queue 모듈의 Queue 클래스를 사용한다.
from queue import Queue

def bfs_cc(adj,vtx,color,s,visited):                # 너비 우선 탐색을 통한 부분 그래프 탐색
    queue = Queue(); queue.put(vtx[s]); visited[s] = True   # 첫 번재 정점을 큐에 넣고 해당 노드를 방문했다고 확인한다.
    color.append(vtx[s])                            # 방문했으므로 color에 append
    while queue.qsize() != 0:                                    # 공백이 아닐 때 까지
        vertex = queue.get()                    #   큐를 deque한다.
        s = vtx.index(vertex)                       #   출력한 정점의 인덱스를 확인하여 인접 정점 탐색을 위해 저장한다.
        for i in range(len(vtx)):                   #   모든 정점에 대하여
            if adj[s][i] == 1:                      #   인접 정점이라면
                if visited[i] == False:             #       방문 정점인지 확인하고
                    visited[i] = True               #           아니면 방문 표시를 한다.
                    queue.put(vtx[i])            #           해당 정점을 큐에 삽입
                if vtx[i] not in color:             #       color 리스트에 없다면 
                    color.append(vtx[i])            #           color 리스트에도 append
    return color                                    # color 반환


def find_connected_component(adj, vtx):             # 같은 color끼리 묶는 함수
    visited = [False] * len(vtx)                    # 방문 정점 초기화
    colorList = []                                  # 부분 그래프 리스트 초기화 

    for i in range(len(vtx)):                       # 모든 정점에 대하여
        if visited[i] == False:                     # 방문 정점이 아니라면
            color = bfs_cc(adj,vtx,[],i,visited)    # 새로운 부분 그래프 생성
            colorList.append(color)                 # color 리스트를 append
    return colorList                                # color List를 반환


def find_bridges(adj, vtx):                         # 브릿지를 찾는 함수
    n = len(vtx) ; count = 0                        # 정점의 갯수 설정 및 브릿지 갯수 초기화
    for i in range(n):                              
        for j in range(i+1, n):                     # 인접 행렬은 대각선을 기준으로 대칭이므로 한쪽 대각선만 검사한다.
            if adj[i][j] != 0:                      # 인접한 정점을
                adj[i][j] = 0                       # 인접하지 않게 바꾸고
                if len(find_connected_component(adj, vtx)) > 1 :    # 그에 대한 부분 그래프를 확인하여서 2개 이상 생성된다면
                    count += 1                                      # 브릿지의 갯수를 추가하고 출력한다.
                    print("Bridge%d: (%s,%s)"%(count,vtx[i],vtx[j]))
                adj[i][j] = 1                       # 검사가 끝나면 다시 인접한 정점으로 바꿔놓는다.



vertex =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat =[ [ 0,   1,   1,   0,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   1,   0,   0,   0 ],
          [ 0,   1,   1,   0,   0,   1,   0,   0 ],
          [ 0,   0,   1,   0,   0,   0,   1,   1 ],
          [ 0,   0,   0,   1,   0,   0,   0,   0 ],
          [ 0,   0,   0,   0,   1,   0,   0,   1 ],
          [ 0,   0,   0,   0,   1,   0,   1,   0 ] 
]
print('Find_Bridges : ')
find_bridges(adjMat, vertex)
print()