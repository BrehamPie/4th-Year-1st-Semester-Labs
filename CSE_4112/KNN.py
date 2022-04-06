from math import sqrt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#KNN class for 2D points.
class KNN_2D():
    def __init__(self):
        self.points=[]
    def add_point(self,point):
        self.points.append(point)
    def find_k_nearset_points(self,point,K):
        distance_list = []
        for old_point in self.points:
            distance_list.append( (sqrt (abs(old_point[0]-point[0])**2+abs(old_point[1]-point[1])**2), old_point))
        print(type (distance_list))
        distance_list.sort()
        return distance_list[:K]



#Using diabetes dataset and taking blood pressure and skin thickness
dataset = pd.read_csv('./diabetes.csv')
X = dataset.iloc[:50,[2,3]].values
my_knn = KNN_2D()
xs=[]
ys=[]
for point in X:
    my_knn.add_point((point[0],point[1]))
    xs.append(point[0])
    ys.append(point[1])
#input point
in_x = 70
in_y = 20
in_x,in_y =  map(int, input("Enter Point(x,y):").split())
K = int(input("How many Nearest Values:"))
ret = my_knn.find_k_nearset_points([in_x,in_y], K)
print(ret)
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(5)
plt.grid()
plt.scatter(xs,ys)
for point in ret:
    plt.scatter(point[1][0], point[1][1], c='#112112')
plt.scatter(in_x,in_y, c=  '#ff7f0e')
plt.xticks(np.arange(min(xs), max(xs)+1, 4.0))
plt.yticks(np.arange(min(ys), max(ys)+1, 4.0))

plt.show()


