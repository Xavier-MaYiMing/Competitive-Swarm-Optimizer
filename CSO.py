#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 14:36
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : CSO.py
# @Statement : Competitive Swarm Optimizer (CSO)
# @Reference : Cheng R, Jin Y. A competitive swarm optimizer for large scale optimization[J]. IEEE Transactions on Cybernetics, 2014, 45(2): 191-204.
import numpy as np
import matplotlib.pyplot as plt


def cal_obj(x, opt):
    # CEC08 shifted sphere function, -100 <= x <= 100
    return sum((x - opt) * (x - opt))


def main(npop, iter, lb, ub, phi, opt):
    """
    The main function
    :param npop: population size
    :param iter: iteration number
    :param lb: lower bound
    :param ub: upper bound
    :param phi: a pre-defined parameter
    :param opt: the shifted value of sphere function
    :return:
    """
    # Step 1. Initialization
    dim = len(lb)  # dimension
    half_npop = int(npop / 2)
    pos = np.random.rand(npop, dim) * (ub - lb)  # population
    vel = np.zeros((npop, dim))  # velocity
    objs = np.array([cal_obj(pos[i], opt) for i in range(npop)])  # objectives
    gbest = min(objs)  # the global best
    iter_best = []  # the global best of each iteration
    ind = np.arange(npop)
    con_iter = 0  # the convergence iteration

    # Step 2. The main loop
    for t in range(iter):

        # Step 2.1. Random competitions
        np.random.shuffle(ind)
        pair1 = ind[: half_npop]
        pair2 = ind[half_npop:]
        center = np.ones((half_npop, dim)) * np.mean(pos, axis=0)
        flag = objs[pair1] < objs[pair2]
        winners = np.hstack((pair1[flag], pair2[~flag]))
        losers = np.hstack((pair1[~flag], pair2[flag]))

        # Step 2.2. Losers learn from winners
        vel[losers] = np.random.rand(half_npop, dim) * vel[losers] + np.random.rand(half_npop, dim) * (pos[winners] - pos[losers]) + phi * np.random.rand(half_npop, dim) * (center - pos[losers])
        pos[losers] += vel[losers]

        # Step 2.3. Evaluation
        for i in losers:
            pos[i] = np.min((pos[i], ub), axis=0)
            pos[i] = np.max((pos[i], lb), axis=0)
            objs[i] = cal_obj(pos[i], opt)
            if objs[i] < gbest:
                gbest = objs[i]
                con_iter = t + 1
        iter_best.append(gbest)

        if (t + 1) % 20 == 0:
            print('Iteration ' + str(t + 1) + ': gbest is ' + str(gbest))

    # Step 3. Sort the results
    x = np.arange(iter)
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('iteration number')
    plt.ylabel('gbest')
    plt.title('convergence curve')
    plt.savefig('convergence curve.png')
    plt.show()
    return {'gbest': gbest, 'convergence iteration': con_iter}


if __name__ == '__main__':
    t_npop = 500
    t_iter = 4000
    t_lb = np.array([-100] * 1000)
    t_ub = np.array([100] * 1000)
    t_phi = 0.15
    t_opt = np.random.uniform(-100, 100, 1000)
    print(main(t_npop, t_iter, t_lb, t_ub, t_phi, t_opt))
