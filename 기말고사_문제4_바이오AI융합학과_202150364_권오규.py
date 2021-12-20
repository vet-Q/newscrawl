import numpy as np

# define sigmoid function
def actf(x):
     return 1/(1+np.exp(-x))

# derivative func
def actf_deriv(x):
    return x*(1-x)


# 입력유닛의 개수, 은닉유닛의 개수, 출력유닛의 개수
inputs, hiddens, outputs = 2,2,1
learning_rate = 0.2

# 훈련 샘플과 정답
X= np.array([[0,0],[0,1],[1,0],[1,1]])
T = np.array([[1],[0],[0],[1]])

# 순방향 전파 구현
W1 = np.array([[0.1,0.2],[0.3,0.4]])
W2 = np.array([[0.5],[0.6]])
B1 = np.array([0.1,0.2])
B2 = np.array([0.3])

# 순방향 전파의 계산
def predict(x):
    layer0 = x
    Z1 = np.dot(layer0,W1)+B1
    layer1 = actf(Z1)
    Z2 = np.dot(layer1,W2)+B2
    layer2 = actf(Z2)
    return layer0, layer1, layer2
