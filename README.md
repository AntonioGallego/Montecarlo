# Montecarlo
Antonio Gallego May 2021

Wonderful article on Montecarlo methods found in Hacker News

https://ggcarvalho.dev/posts/montecarlo/

The code was Go. As an exercise I went through it rewriting it in Python

https://en.wikipedia.org/wiki/Monte_Carlo_method

https://en.wikipedia.org/wiki/Monty_Hall_problem'


'''
$ python montecarlo.py
Pi's Montecarlo approach
After 100000 rounds Pi approaches 3.1406
Error 0.03%

Euler's number
After 100000 rounds e approaches 2.71504
Error 0.12%

Birthday's Paradox
After 1000 rounds probability of birthday collision for a group of size 23 approaches 0.504%
n	P(n)
1	0.00%
5	3.00%
10	10.40%
20	40.80%
23	50.70%
30	71.40%
40	88.20%
50	95.80%
60	98.90%
70	100.00%
75	100.00%
100	100.00%
366	100.00%

Monty Hall Problem
After 10000 games 'no-switch' success approaches 0.34%
After 10000 games 'switch' success approaches 0.66%

Montecarlo Integration
After 1000000 tests area is determined as 1.7699398187023536

Option Pricing Using the Black-Scholes Model, discretized version of the BSM model (Euler discretization)
Initial value: 100.0 Strike price: 105.0 Maturity: 1.0 Risk free short rate: 0.05 Volatility 0.2 Tests: 250000
European Option Value: 7.42013365
''''
