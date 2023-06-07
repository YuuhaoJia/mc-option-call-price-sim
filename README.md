# monte-carlo-price-sim
Estimates spot price of European call options using Monte Carlo simulation. Includes a built in Black-Scholes pricing function for use as a benchmark, and generates simulations with n number of scenarios for accuracy comparison

### Built using

* Python

### Key themes/tags

* Monte Carlo Simulation
* Derivatives pricing
  * Black-Scholes
* Probability (Bayesian Statistics)
  * Random variates
  * Uncertainty
  * Drift
 
# Demo

Note: Demo conducted using the option_1.py file. The option being simulated had the following characteristics:

* Stock spot price: 100
* Strike price : 100
* Risk free rate: 5%
* Volatility: 10%
* Time to maturity: 1 year

### Graph of simulation 1 (10 scenarios)

![image](https://user-images.githubusercontent.com/112993711/189773560-fb41f8a9-84ec-40a4-a01e-326060d64996.png)

### Graph of simulation 2 (50 scenarios)

![image](https://user-images.githubusercontent.com/112993711/189773648-30eeb413-b3a3-4731-b645-f96affbe2419.png)

### Graph of simulation 3 (100 scenarios)

![image](https://user-images.githubusercontent.com/112993711/189773742-50eaa6c1-15da-4d31-8080-8887be68ecf5.png)

### Graph of simulation 4 (500 scenarios)

![image](https://user-images.githubusercontent.com/112993711/189773988-2c0813a4-7105-44ee-b7b3-48ae9fd03505.png)

### Output of function showing increased accuracy (more proximity to Black-Scholes benchmark) with increased number of scenarios

![image](https://user-images.githubusercontent.com/112993711/189774164-a832455e-9333-4f9c-8f8c-7553fa4a8f89.png)

# Contact

Yuhao Jia - yuhaoj10@gmail.com

Bachelor of Computer Science (BCS) 2025 Candidate

University of Waterloo 
