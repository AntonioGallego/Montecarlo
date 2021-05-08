# Montecarlo
After reading this wonderful article on Monte Carlo methods found via Hacker News...

https://ggcarvalho.dev/posts/montecarlo/

... we'll use Monte Carlo methods and some Python code to estimate pi, e, some 'Birthday Paradox' chances, the outcome of the (in)famous Monty Hall, several definite integrals and an option price using the Black-Scholes Model.

Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. Invented by von Neumann, Ulam and Metropolis in the context Manhattan Project, this technique is used throughout areas such as physics, finance, engineering, project management, insurance, and transportation, where a numerical result is needed and the underlying theory is difficult and/or unavailable.

>To apply the Monte Carlo method, the analyst constructs a mathematical model that simulates a real system. A large number of random sampling of the model is applied yielding a large number of random samples of output results from the model. […] The method is based on running the model many times as in random sampling. For each sample, random variates are generated on each input variable; computations are run through the model yielding random outcomes on each output variable. Since each input is random, the outcomes are random. In the same way, they generated thousands of such samples and achieved thousands of outcomes for each output variable (N.T. Thomopoulos “Essentials of Monte Carlo Simulation: Statistical Methods for Building Simulation Models”)

>Monte Carlo methods are based on the analogy between probability and volume. The mathematics of measure formalizes the intuitive notion of probability, associating an event with a set of outcomes and defining the probability of the event to be its volume or measure relative to that of a universe of possible outcomes. Monte Carlo uses this identity in reverse, calculating the volume of a set by interpreting the volume as a probability. In the simplest case, this means sampling randomly from a universe of possible outcomes and taking the fraction of random draws that fall in a given set as an estimate of the set’s volume. The law of large numbers ensures that this estimate converges to the correct value as the number of draws increases. The central limit theorem provides information about the likely magnitude of the error in the estimate after a finite number of draws. (Paul Glasserman “Monte Carlo Methods in Financial Engineering - Stochastic Modelling and Applied Probability")

The article code was written in Go. As an exercise I went through it rewriting it in Python. Here's a typical run:

```
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
```
