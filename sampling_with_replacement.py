import random
import matplotlib.pyplot as plt

random.seed(2)

# Generation of a population
population_size = 1000
population = []
for i in range(population_size):
    height = random.uniform(150, 205)
    population.append(height)

# population parameters
mean_height = sum(population)/population_size


def calculate_variance(population, mean, denominator):
    sum_squared_deviations = 0
    for value in population:
        sum_squared_deviations = sum_squared_deviations + ((value - mean) ** 2)
    return sum_squared_deviations/denominator

variance_height = calculate_variance(population, mean_height, population_size)

sample_size = 2

def generate_sample(population, n):
    sm = []
    for i in range(n):
        position = random.randint(0, len(population) - 1)
        value = population[position]
        sm.append(value)
    return sm

trials = 100000
sample_mean_list = []
sample_variance_list = []

for i in range(trials):
    sample = generate_sample(population, sample_size)

    #deigmatikos mesos
    sample_mean = sum(sample)/sample_size

    #deigmatikh diakymansh
    sample_variance = calculate_variance(sample, sample_mean, sample_size - 1)

    sample_mean_list.append(sample_mean)
    sample_variance_list.append(sample_variance)


mean_of_sample_means = sum(sample_mean_list)/trials
print ('Mean of means = ' + str(mean_of_sample_means))
print ('Mean of Population = ' + str(mean_height))
print()

variance_of_means = calculate_variance(sample_mean_list, mean_of_sample_means, trials)
print ('Variance of means = ' + str(variance_of_means))
print('Variance of population divided by sample size = ' + str(variance_height / sample_size))
print()

mean_of_sample_variances = sum(sample_variance_list)/trials

plt.hist(sample_mean_list, bins = 40)
plt.show()

print ('Mean of sample variances = ' + str(mean_of_sample_variances))
print('Variance of population = ' + str(variance_height))
print()

print('end')
