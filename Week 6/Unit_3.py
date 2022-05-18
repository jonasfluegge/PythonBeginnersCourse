import random
import statistics as s

mu = 100
sigma = 10


def gaussian_distribution():
    random_numbers = [random.gauss(mu, sigma) for _ in range(1, 1001)]
    return random_numbers


print("Mean:", s.mean(gaussian_distribution()))
print("Standard Deviation:", s.stdev(gaussian_distribution()))
