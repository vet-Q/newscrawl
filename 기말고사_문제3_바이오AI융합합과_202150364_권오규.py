import numpy as np

class Values:

    def __init__(self):
        self.W1 = np.array([[0.10, 0.20], [0.30, 0.40]])
        self.W2 = np.array([[0.50], [0.60]])
        self.B1 = np.array([0.1, 0.2])
        self.B2 = np.array([0.3])

    def reset(self):
        self.W1 = np.array([[0.10, 0.20], [0.30, 0.40]])
        self.W2 = np.array([[0.50], [0.60]])
        self.B1 = np.array([0.1, 0.2])
        self.B2 = np.array([0.3])


class MLP(Values):

    def __init__(self):
        super().__init__()
        self.X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.T = np.array([[1], [0], [0], [1]])
        self.learning_rate = 0.2


    # define relu and relu derivative function (if x > 0: return 1 else 0)
    def relu(self,x,derivative=False):
        if derivative == True:
            der_val = np.array(x > 0)
            der_val = der_val.astype(int)
            return der_val
        return np.maximum(x,0)


    # define tanh function and derivative
    def tanh(self,x,derivative=False):
        if derivative == True:
            return 1 - x ** 2
        return np.tanh(x)


    # calculate forward pass
    def predict(self,x,func):
        layer0 = x  # 입력을 layer0에 대입한다.
        Z1 = np.dot(layer0, self.W1) + self.B1  # 행렬의 곱을 계산한다.
        layer1 = func(Z1)  # 활성화 함수를 적용한다.
        Z2 = np.dot(layer1, self.W2) + self.B2  # 행렬의 곱을 계산한다.
        layer2 = func(Z2)  # 활성화 함수를 적용한다.
        return layer0, layer1, layer2


    # calculate back propagation
    def fit(self, func):
        for i in range(90000):  # 9만번 반복한다.
            for x, y in zip(self.X, self.T):  # 학습 샘플을 하나씩 꺼낸다.
                x = np.reshape(x, (1, -1))  # 2차원 행렬로 만든다. ①
                y = np.reshape(y, (1, -1))  # 2차원 행렬로 만든다.

                layer0, layer1, layer2 = self.predict(x,func)  # 순방향 계산
                layer2_error = layer2 - y  # 오차 계산
                layer2_delta = layer2_error * func(layer2,derivative=True)  # 출력층의 델타 계산
                layer1_error = np.dot(layer2_delta, self.W2.T)  # 은닉층의 오차 계산
                layer1_delta = layer1_error * func(layer1,derivative=True)  # 은닉층의 델타 계산

                self.W2 += -self.learning_rate * np.dot(layer1.T, layer2_delta)
                self.W1 += -self.learning_rate * np.dot(layer0.T, layer1_delta)
                self.B2 += -self.learning_rate * np.sum(layer2_delta, axis=0)
                self.B1 += -self.learning_rate * np.sum(layer1_delta, axis=0)

    # Print MLP result
    def output(self, func):
        for x, y in zip(self.X, self.T):
            x = np.reshape(x, (1, -1))  # 하나의 샘플을 꺼내서 2차원 행렬로 만든다.
            layer0, layer1, layer2 = self.predict(x,func)
            print(x, y, layer2)  # 출력층의 값을 출력해본다.



if __name__ == "__main__":
    mlp = MLP()
    print('이번 결과는 tanh 적용시 결과입니다')
    mlp.fit(mlp.tanh)
    mlp.output(mlp.tanh)
    # print('전:',mlp.W1)
    # print('전:',mlp.W2)
    mlp.reset()
    print('-----------------------------------------------')
    print('이번 결과는 relu 적용시 결과입니다')
    # print('후:',mlp.W1)
    # print('후:',mlp.W2)
    mlp.fit(mlp.relu)
    mlp.output(mlp.relu)