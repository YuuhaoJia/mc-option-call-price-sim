'''
Author: Yuhao Jia 
Created: 08/30/2022

coding: utf-8 
'''
def option():
    n = #Indicate number of scenarios desired
    config = Config(n, 1) 
    sp = #Indicate stock spot price
    s = #Indicate strike price
    rf = #Indicated risk free rate
    v = #Indicate volatility
    t = #Indicate time to maturity
    Option_1 = Option_Trade(sp, s, rf, v, t)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option_1)
    simulated_price = simulator.sim(Option_1, pricer)
    print('Option 1, 50 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option()
