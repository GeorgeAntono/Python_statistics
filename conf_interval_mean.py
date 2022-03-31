import random
import scipy.stats as st
import math
random.seed(1)

# generate poulation of heights
population_size = 1000
population_heights = []
for i in range(1000):
    ht = random.randint(150, 210)
    population_heights.append(ht)

mean_population_height = sum(population_heights)/len(population_heights)
var_population_height = sum((i - mean_population_height) ** 2 for i in population_heights) / len(population_heights)

# generate sample
def generate_sample(sample_size, population):
    sample_heights = []
    for i in range(sample_size):
        index = random.randint(0, len(population) - 1)
        ht = population[index]
        sample_heights.append(ht)
    return sample_heights


trials  = 10000
pop_mean_in_conf_interval = 0
sample_size = 30
confidence_level = 0.95
a = 1 - confidence_level
a_div_2 = a / 2
Z_a_div_2 = abs(st.norm.ppf(a_div_2))

variance_sample_mean = var_population_height / sample_size
std_dev_sample_mean = math.sqrt(variance_sample_mean)

for i in range(trials):
    sample = generate_sample(sample_size, population_heights)
    sample_mean = sum(sample)/len(sample)

    confidence_interval_a = sample_mean -  Z_a_div_2 * std_dev_sample_mean
    confidence_interval_b = sample_mean +  Z_a_div_2 * std_dev_sample_mean

    if (mean_population_height >= confidence_interval_a and mean_population_height <= confidence_interval_b):
        pop_mean_in_conf_interval += 1

observed_probability = pop_mean_in_conf_interval / trials

print(confidence_level)
print(observed_probability)
print(1)