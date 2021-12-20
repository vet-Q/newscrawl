import numpy as np

# define relu function
# define relu derivative function (if x > 0: return 1 else 0)
def relu(x):
    return np.maximum(x,0)

def relu_deriv(x):
    der_val = np.array(x > 0)
    der_val = der_val.astype(np.int)
    return der_val

# define tanh function
def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1 - x ** 2

# 입력유닛의 개수, 은닉유닛의 개수, 출력유닛의 개수
inputs, hiddens, outputs = 2, 2, 1
learning_rate = 0.2

# 훈련 샘플과 정답
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
T = np.array([[1], [0], [0], [1]])

def makevalues():
    W1 = np.array([[0.10, 0.20], [0.30, 0.40]])
    W2 = np.array([[0.50], [0.60]])
    B1 = np.array([0.1, 0.2])
    B2 = np.array([0.3])

    return W1,W2,B1,B2

# 순방향 전파 계산
def predict(x,func):
    layer0 = x  # 입력을 layer0에 대입한다.
    Z1 = np.dot(layer0, W1) + B1  # 행렬의 곱을 계산한다.
    layer1 = func(Z1)  # 활성화 함수를 적용한다.
    Z2 = np.dot(layer1, W2) + B2  # 행렬의 곱을 계산한다.
    layer2 = func(Z2)  # 활성화 함수를 적용한다.
    return layer0, layer1, layer2


# 역방향 전파 계산
def fit(func,derivFunc):
    for i in range(90000):  # 9만번 반복한다.
        for x, y in zip(X, T):  # 학습 샘플을 하나씩 꺼낸다.
            x = np.reshape(x, (1, -1))  # 2차원 행렬로 만든다. ①
            y = np.reshape(y, (1, -1))  # 2차원 행렬로 만든다.

            layer0, layer1, layer2 = predict(x,func)  # 순방향 계산
            layer2_error = layer2 - y  # 오차 계산
            layer2_delta = layer2_error * derivFunc(layer2)  # 출력층의 델타 계산
            layer1_error = np.dot(layer2_delta, W2.T)  # 은닉층의 오차 계산 ②
            layer1_delta = layer1_error * derivFunc(layer1)  # 은닉층의 델타 계산 ③

            W2 += -learning_rate * np.dot(layer1.T, layer2_delta)  # ④
            W1 += -learning_rate * np.dot(layer0.T, layer1_delta)  #
            B2 += -learning_rate * np.sum(layer2_delta, axis=0)  # ⑤
            B1 += -learning_rate * np.sum(layer1_delta, axis=0)  #


def output(a):
    for x, y in zip(X, T):
        a = a
        x = np.reshape(x, (1, -1))  # 하나의 샘플을 꺼내서 2차원 행렬로 만든다.
        layer0, layer1, layer2 = predict(x,a)
        print(x, y, layer2)  # 출력층의 값을 출력해본다.



if __name__ == "__main__":
    print('이번 결과는 tanh 적용시 결과입니다')
    fit(tanh,tanh_deriv)
    output(tanh)
    print('-----------------------------------------------')
    print('이번 결과는 relu 적용시 결과입니다')
    fit(relu, relu_deriv)
    output(relu)