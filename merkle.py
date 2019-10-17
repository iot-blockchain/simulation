import pickle
import random
import time
import matplotlib.pyplot as plt

import merkletools

mt = merkletools.MerkleTools()


def generate_tree(num):
    start = time.time_ns()
    for x in range(0, num * 10000):
        y = random.randint(0, 9) * x
        mt.add_leaf(str(y), True)
    mt.make_tree()
    end = time.time_ns()
    time_consumption = end - start
    return [num * 10000, time_consumption]


def begin_tests(env):
    print("current env: ", env)
    axis_x = []
    axis_y = []
    for i in range(1, 100):
        x, y = generate_tree(i)
        print(x, " leaves, time consumption: ", y, " ns")
        axis_x.append(x)
        axis_y.append(y)
    plt.plot(axis_x, axis_y)
    plt.xlabel('leaf nums')
    plt.ylabel('time consumption(ns)')
    plt.show()

    # 对象序列化
    f = open(env + '.dmp', 'wb')
    pickle.dump([axis_x, axis_y], f)


if __name__=='__main__':
    begin_tests("computer")
    f_computer = open('computer.dmp', 'rb')
    computer = pickle.load(f_computer)
    f_pi = open('pi.dmp', 'rb')
    pi = pickle.load(f_pi)

    plt.plot(computer[0], computer[1], color='green', label='computer')
    plt.plot(pi[0], pi[1], color='skyblue', label='raspberry pi')

    plt.xlabel('leaf nums')
    plt.ylabel('time consumption(ns)')
    plt.show()
