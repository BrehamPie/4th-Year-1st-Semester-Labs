import matplotlib.pyplot as plt
from collections import deque
import heapq as pq

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class KDTree():
    def get_distance(self,a, b):
        return (a[0]-b[0])**2+(a[1]-b[1])**2

    def __init__(self, points):
        def build(points, dimension=0):
            print(points, dimension)
            if(len(points) == 1):
                return Node(points[0])
            elif len(points) > 1:
                points.sort(key=lambda x: x[dimension])
                print(points)
                median = len(points) >> 1
                return Node(points[median], build(points[:median], dimension ^ 1), build(points[median+1:], dimension ^ 1))
        self.head = build(points)

    def bfs(self):
        q = deque()
        q.append((self.head, 0))
        while len(q):
            u = q.popleft()
            print(u[0].key, u[1])
            if u[0].left is not None:
                q.append((u[0].left, u[1]+1))
            if u[0].right is not None:
                q.append((u[0].right, u[1]+1))
    def dfs(self,root,point,dimension,heap,K):
       
        if root is not None:
            print(root.key)
            print(heap)
            radius = root.key[dimension]-point[dimension]
            actual_distance = self.get_distance(root.key,point)
            print("radius:"+str(radius))
            print("actual dis:"+str(actual_distance))
            if(len(heap)): print("heap:"+str(-heap[0][0]))
            if len(heap)<K:
                pq.heappush(heap, (-actual_distance,root.key))
            elif actual_distance < -heap[0][0]:
                pq.heappushpop(heap, (-actual_distance, root.key))
            dimension = (dimension+1)%2
            print("heap:"+str(heap)+str(heap[0][0]))
            for b in (radius<0,radius>=0)[:1+(radius**2< -heap[0][0])]:
                print("B is:"+str(b))
                print(root.left.key)
                if b is False:
                    self.dfs(root.left,point,dimension,heap,K)
                else:
                    self.dfs(root.right,point,dimension,heap,K)
        return heap
            


    def KNN(self,point,K):
        heap = []
        return self.dfs(self.head,point,0,heap,K)


my_points = [(72, 50), (66, 31), (64, 32), (66, 21), (40, 33), (74, 30), (50, 26), (0, 29), (70, 53), (96, 54), (92, 30), (74, 34), (80, 57), (60, 59), (72, 51), (0, 32), (84, 31), (74, 31), (30, 33), (70, 32), (88, 27), (84, 50), (90, 41), (80, 29), (94, 51),
             (70, 41), (76, 43), (66, 22), (82, 57), (92, 38), (75, 60), (76, 28), (58, 22), (92, 28), (78, 45), (60, 33), (76, 35), (76, 46), (68, 27), (72, 56), (64, 26), (84, 37), (92, 48), (110, 54), (64, 40), (66, 25), (56, 29), (70, 22), (66, 31), (0, 24)]
my_kd = KDTree(my_points)
my_kd.bfs()
print(my_kd.KNN((70,20),5))