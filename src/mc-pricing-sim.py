'''
Author: Yuhao Jia 
Created: 08/30/2022

coding: utf-8 
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class Option_Trade:
    def __init__(self, spot_price, strike_price, risk_free_rate, volatility, time_to_maturity):
        self.spot_price = spot_price
        self.strike_price = strike_price
        self.risk_free_rate = risk_free_rate
        self.volatility = volatility
        self.time_to_maturity = time_to_maturity

    def Black_Scholes(self):
        d_1 = (math.log(self.spot_price / self.strike_price) +
               (self.risk_free_rate + (self.volatility ** 2 / 2) * self.time_to_maturity)) / \
              self.volatility * math.sqrt(self.time_to_maturity)
        d_2 = d_1 - self.volatility * math.sqrt(self.time_to_maturity)
        call_price = self.spot_price * norm.cdf(d_1, 0, 1) - \
                     self.strike_price * math.exp(-self.risk_free_rate * self.time_to_maturity) * norm.cdf(d_2, 0, 1)
        return call_price

class Config:
    def __init__(self, n_scenarios, n_timesteps):
        self.n_scenarios = n_scenarios
        self.n_timesteps = n_timesteps

class gbm_model:
    def __init__(self, config):
        self.config = config

    def sim_risk_factor(self, Option_Trade):
        prices = []
        for x in range(self.config.n_scenarios):
            random_n = np.random.normal(0,1)
            drift = (Option_Trade.risk_free_rate - (Option_Trade.volatility ** 2) / 2)
            uncertainty = Option_Trade.volatility * random_n
            price = Option_Trade.spot_price * math.exp(drift + uncertainty)
            prices.append(price)
        return prices

class pay_off_pricer:
    def det_price(self, Option_Trade, pps):
        p = 0
        for i in range(len(pps)):
            price = pps[i]
            pay_off = price - Option_Trade.strike_price
            if pay_off > 0:
                p += pay_off
        discounted_price = (math.exp(- 1.0 * Option_Trade.risk_free_rate *
                                     Option_Trade.time_to_maturity) * p)
        return discounted_price / len(pps)

def splot(pps, Option_Trade):
    h = []
    z = []
    for x in pps:
        z.append(x)
        z.append(Option_Trade.spot_price)
        h.append(1)
        h.append(0)
        plt.plot(h, z)
    plt.xlabel('Timestep')
    plt.ylabel('Stock Value')
    plt.show()

class MonteCarloSim:
    def __init__(self, config, model):
        self.config= config
        self.model = model

    def sim(self, Option_Trade, pricer):
        pps = self.model.sim_risk_factor(Option_Trade)
        splot(pps, Option_Trade)
        price = pricer.det_price(Option_Trade, pps)
        return price
