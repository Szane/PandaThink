#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np


class KMArithmetic:
    'KM算法工具类'
    INF = 0xffffff
    MAX = 10000
    lx = np.zeros(MAX)
    ly = np.zeros(MAX)
    match = np.zeros(MAX)
    visX = np.zeros(MAX)
    visY = np.zeros(MAX)
    slack = np.zeros(MAX)

    def __initvertex(self, nx, ny, weight):
        for i in range(nx):
            self.lx[i] = -self.INF
            for j in range(ny):
                self.ly[j] = 0
                if self.lx[i] < weight[i][j]:
                    self.lx[i] = weight[i][j]
        for k in range(self.MAX):
            self.match[k] = -1

    def __path(self, u, ny, weight):
        u = int(u)
        self.visX[u] = 1
        for v in range(ny):
            if self.visY[v]:
                continue
            t = self.lx[u] + self.ly[v] - weight[u][v]
            if t == 0:
                self.visY[v] = 1
                if self.match[v] == -1 or self.__path(self.match[v], ny, weight):
                    self.match[v] = u
                    return True
            elif self.slack[v] > t:
                self.slack[v] = t
        return False

    def bestmatch(self, nx, ny, w):
        weight = np.array(w)
        self.__initvertex(nx, ny, weight)
        for u in range(nx):
            for i in range(ny):
                self.slack[i] = self.INF
            while 1:
                for i in range(nx):
                    self.visX[i] = 0
                for i in range(ny):
                    self.visY[i] = 0
                if self.__path(u, ny, weight):
                    break
                dx = self.INF
                for i in range(ny):
                    if (not self.visY[i]) and dx > self.slack[i]:
                        dx = self.slack[i]
                for i in range(nx):
                    if self.visX[i]:
                        self.lx[i] -= dx
                for i in range(ny):
                    if self.visY[i]:
                        self.ly[i] += dx
                    else:
                        self.slack[i] -= dx
        result_sum = 0
        for i in range(ny):
            if self.match[i] > -1:
                result_sum += weight[int(self.match[i])][i]
                print(self.match[i], i)
        return result_sum

    def getmatch(self):
        return self.match
