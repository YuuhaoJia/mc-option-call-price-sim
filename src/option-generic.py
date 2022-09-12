'''
Author: Yuhao Jia 
Created: 08/30/2022
coding: utf-8 

Note: Instead of changing the value of each parameter (variable) the user
may find it easier to modify the function call(s) directly instead
'''
def option():
    n = #Indicate number of scenarios
    config = Config(n, 1)
    sp = #Stock spot price
    s = #Strike price
    rf = #Risk free rate
    v = #Volatility
    t = #Time to maturity
    Option = Option_Trade(sp, s, rf, v, t)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option)
    simulated_price = simulator.sim(Option, pricer)
    print('Option 1, 50 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option()
