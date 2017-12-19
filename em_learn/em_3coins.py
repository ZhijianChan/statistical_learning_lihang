# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:34:29 2017

@author: Zhijian Chen
"""
import math


class EM():
        
    def fit(self, data, max_iter = 2):
        print data
        self.pi = 0.4
        self.p = 0.6
        self.q = 0.7
        tot = len(data)
        
        for i in range(max_iter):
            print '\n[Epoch %d]' % i
            # E-step
            mu = [self.compute_mu(y) for y in data]
            prob_b_sum = sum(mu)
            prob_c_sum = sum([1 - p for p in mu])
            # M-step
            self.p = sum([mu[j] * data[j] for j in range(tot)]) / prob_b_sum
            self.q = sum([(1 - mu[j]) * data[j] for j in range(tot)]) / prob_c_sum
            self.pi = prob_b_sum / tot
            print 'p:\t', self.p
            print 'q:\t', self.q
            print 'pi:\t', self.pi
    
    def compute_mu(self, y):
        prob_b = self.pi * math.pow(self.p, y) * math.pow(1 - self.p, 1 - y)
        prob_c = (1 - self.pi) * math.pow(self.q, y) * math.pow(1 - self.q, 1 - y)
        return prob_b / (prob_b + prob_c)
            

if __name__ == '__main__':
    data = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
    em = EM()
    em.fit(data)
