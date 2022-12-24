from sklearn.linear_model import LogisticRegression
n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
print(X)
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

