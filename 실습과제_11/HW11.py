# <힙 이용 Kruskal MST 알고리즘 > p11.3
import heapq

parent = []                             # 각 노드의 부모노드 인덱스
set_size = 0                            # 전체 집합의 개수(노드들이 연결되면 하나의 집합됨)

# 각 집합 초기화
def init_set(nSets):                    # 정점의 개수를 매개변수로 받아옴 
    global set_size, parent             # 전역변수 set_size, parent 이용
    set_size = nSets                    # 처음 집합의 수는 정점의 수 만큼 있음
    for i in range(nSets):              # 모든 집합을 돌면서(모든 집합에 대해)
        parent.append(-1)               # 각각이 고유 집합(부모-1 = 자기가 루트노드)

# 정점 id가 속한 집합 찾기
def find(id):                           # 매개변수로 해당정점 id를 받아서
    while(parent[id] >= 0):             # id의 부모가 -1이 아닐때
        id = parent[id]                 # 부모노드는 id(대표)
    return id                           # id반환

# 두 집합 병합함수
def union(s1, s2):                      # 현재정점과 인접정점을 매개변수로 받아옴
    global set_size                     # 전역변수 set_size 전체집합 개수 사용
    parent[s1] = s2                     # 현재정점의 대표는 s2가됨 (=병합)
    set_size = set_size - 1             # 전체집합 개수 줄어듦

# Kruskal 알고리즘
def MSTKruskal(vertex, adj):            # 매개변수로 정점리스트, 인접행렬 받아옴
    vsize = len(vertex)                 # vise: 정점집합의 개수 = 정점의 개수 = 정점리스트의 길이
    init_set(vsize)                     # 각 정점 집합 초기화
    eList = []                          # 간선 리스트

    for i in range(vsize-1):
        for j in range(i+1, vsize):     # 그래프의 위 삼각형만큼 돌면서
            if adj[i][j] != None:       # 간선일 경우
                heapq.heappush(eList,(adj[i][j], i, j)) # eList를 힙으로 사용하며 튜플형태로 간선을 넣기, (튜플의 맨 처음요소를 기준으로 정렬)
    
    edgeAccepted = 0                    # MST간선으로 선택된 수
    while(edgeAccepted < vsize-1):      # 전체 간선을 넘지 않을때까지
        e = heapq.heappop(eList)        # 가장 작은 가중치를 가진 간선
        uset = find(e[1])               # 해당정점의 집합 대표찾기
        vset = find(e[2])               # 인접정점의 집합 대표찾기

        if uset != vset:                # 두 정점이 다른 집합의 원소일 경우
            print(f'간선추가: {vertex[e[1]], vertex[e[2]], e[0]}')  # 간선의 정보e[0]번째에 해당
            union(uset, vset)           # 두 집합을 합함
            edgeAccepted += 1           # MST간선 하나 추가

# ====================================================================
vertex = ['A',     'B',    'C',    'D',    'E',     'F',    'G']
weight = [[None,    29,     None,   None,   None,   10,    None],
          [29,      None,   16,     None,   None,   None,    15],
          [None,    16,     None,   12,     None,   None,  None],
          [None,    None,   12,     None,   22,     None,    18],
          [None,    None,   None,   22,     None,   27,      25],
          [10,      None,   None,   None,   27,     None,  None],
          [None,    15,     None,   18,     25,     None,  None]]

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)
