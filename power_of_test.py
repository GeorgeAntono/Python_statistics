import random
import scipy.stats as st
import math
random.seed(1)
import statistics

# generate poulation of heights
population_size = 100000
population = []
for i in range(100000):
    ht = random.normalvariate(171, math.sqrt(10))
    population.append(ht)

# generate sample
def generate_sample(sample_size, population):
    sample = []
    for i in range(sample_size):
        index = random.randint(0, len(population) - 1)
        ht = population[index]
        sample.append(ht)
    return sample

trials = 100000
sample_size = 50

pop_variance = st.tvar(population, ddof=0)

print(1)

def z_test_mean_one_way_upper(m0, pop_variance, a, sample):
    sample_mean = sum(sample) / len(sample)
    std_error = math.sqrt(pop_variance / len(sample))
    z_stat = (sample_mean - m0)/std_error
    z_crit = abs(st.norm.ppf(a))
    if z_stat > z_crit:
        return True
    return False

rejections = 0
non_rejections = 0

for i in range(trials):
    sample = generate_sample(sample_size, population)
    m0 = 170
    a = 0.05
    rejected = z_test_mean_one_way_upper(m0, pop_variance, a, sample)
    if rejected:
        rejections += 1
    else:
        non_rejections += 1

obs_prob_non_rejections = non_rejections/trials
print(obs_prob_non_rejections)
