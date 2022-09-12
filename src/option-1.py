'''
Author: Yuhao Jia 
Created: 08/30/2022

coding: utf-8 

The following are the parameters of Option 1:
Stock spot price: 100
Strike price : 100
Risk free rate: 3%
Volatility: 10%
Time to maturity: 1 year
'''
# Option 1 - 10 Scenarios

def option_1_10s():
    config = Config(10,1)
    Option_1 = Option_Trade(100, 100, 0.05, 0.20, 1)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option_1)
    simulated_price = simulator.sim(Option_1, pricer)
    print('Option 1, 10 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option_1_10s()

# Option 1 - 50 Scenarios

def option_1_50s():
    config = Config(50,1)
    Option_1 = Option_Trade(100, 100, 0.05, 0.20, 1)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option_1)
    simulated_price = simulator.sim(Option_1, pricer)
    print('Option 1, 50 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option_1_50s()

# Option 1 - 100 Scenarios

def option_1_100s():
    config = Config(100,1)
    Option_1 = Option_Trade(100, 100, 0.05, 0.20, 1)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option_1)
    simulated_price = simulator.sim(Option_1, pricer)
    print('Option 1, 100 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option_1_100s()

# Option 1 - 500 Scenarios

def option_1_500s():
    config = Config(500, 1)
    Option_1 = Option_Trade(100, 100, 0.05, 0.20, 1)
    model = gbm_model(config)
    pricer = pay_off_pricer()
    simulator = MonteCarloSim(config, model)

    black_scholes_price = Option_Trade.Black_Scholes(Option_1)
    simulated_price = simulator.sim(Option_1, pricer)
    print('Option 1, 500 Scenarios' + '\n'
          ' Black Scholes price:', black_scholes_price, '\n',
          'Simulated price:', simulated_price, '\n',
          'Absolute difference between results:', str(abs(black_scholes_price - simulated_price)), '\n')

option_1_500s()
