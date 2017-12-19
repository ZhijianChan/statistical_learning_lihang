# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:51:55 2017

@author: Administrator
"""

import math

epsilon = 0.001


def gsfunc(y, mu, sigmaf):
    """Gaussian Distribution: (mu, sigma)
    """
    f1 = 1. / (math.pow(2 * math.pi, 0.5) * math.pow(sigmaf, 0.5))
    f2 = math.exp(- math.pow(y - mu, 2) / (2 * sigmaf))
    return f1 * max(f2, epsilon)


class GMM():
    def fit(self, data, K, max_iter = 10):
        self.K = K
        self.alpha = [1 / float(K)] * K
        self.mu = [0.] * K
        self.sigmaf = [1.] * K
        tot = len(data)
        
        for i in range(max_iter):
            print '\n[Epoch %d]' % i
            for k in range(K):
                # E-step
                gamma = [self.compute_gamma(y, k) for y in data]
                gamma_sum = sum(gamma)
                # M-step
                self.mu[k] = sum([gamma[j] * data[j] for j in range(tot)]) / gamma_sum
                self.sigmaf[k] = sum([gamma[j] * math.pow(data[j] - self.mu[k], 2)
                                      for j in range(tot)]) / gamma_sum
                self.alpha[k] = gamma_sum / tot
            print 'alpha:\t', self.alpha
            print 'mu:\t', self.mu
            print 'sigmaf:\t', self.sigmaf
    
    def predict(self, y):
        return sum([self.alpha[k] * gsfunc(y, self.mu[k], self.sigmaf[k])
                    for k in range(self.K)])
        
    def compute_gamma(self, y, k):
        prob_k = self.alpha[k] * gsfunc(y, self.mu[k], self.sigmaf[k])
        prob_all = sum([self.alpha[i] * gsfunc(y, self.mu[i], self.sigmaf[i])
                        for i in range(self.K)])
        return prob_k / prob_all

if __name__ == '__main__':
    gmm = GMM()
    data = [-67,-48,6,8,14,16,23,24,28,29,41,49,56,60,75]
    gmm.fit(data, 2)
    print '\nprob(12):', gmm.predict(12)