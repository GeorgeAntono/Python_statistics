import random
import scipy.stats as st
import math
random.seed(2)

# generate poulation of heights
population_size = 1000
population_binary_values = []
for i in range(1000):
    ht = 0
    if random.uniform(0,1) < 0.265:
        ht = 1
    population_binary_values.append(ht)

percentage_population = sum(population_binary_values)/len(population_binary_values)

# generate sample
def generate_sample(sample_size, population):
    sample_binary_values = []
    for i in range(sample_size):
        index = random.randint(0, len(population) - 1)
        ht = population[index]
        sample_binary_values.append(ht)
    return sample_binary_values


trials  = 100000
pop_percentage_in_conf_interval = 0
sample_size = 40
confidence_level = 0.95
a = 1 - confidence_level
a_div_2 = a / 2
Z_a_div_2 = abs(st.norm.ppf(a_div_2))

for i in range(trials):
    sample = generate_sample(sample_size, population_binary_values)
    sample_percentage = sum(sample)/len(sample)

    std_error_percentage = math.sqrt(sample_percentage * (1 - sample_percentage) / sample_size)

    confidence_interval_a = sample_percentage -  Z_a_div_2 * std_error_percentage
    confidence_interval_b = sample_percentage +  Z_a_div_2 * std_error_percentage

    if (percentage_population >= confidence_interval_a and percentage_population <= confidence_interval_b):
        pop_percentage_in_conf_interval += 1

observed_probability = pop_percentage_in_conf_interval / trials

print(confidence_level)
print(observed_probability)
print(1)
