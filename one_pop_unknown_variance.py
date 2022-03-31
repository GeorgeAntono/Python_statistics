import random
import scipy.stats as st
import math
random.seed(1)

# generate population of heights
population_size = 1000
population_heights = []
for i in range(1000):
    ht = random.randint(150, 210)
    population_heights.append(ht)

mean_population_height = sum(population_heights)/len(population_heights)

# modification of the two sided ttest provided by python
def one_sample_one_tailed(sample_data, popmean, alpha=0.05, test_direction='greater'):
    t, p = st.ttest_1samp(sample_data, popmean)
    if test_direction == 'greater' and (p/2 < alpha) and t > 0:
        print ('Reject Null Hypothesis for greater-than test')
    if test_direction == 'less' and (p/2 < alpha) and t < 0:
        print ('Reject Null Hypothesis for less-than test')

# generate sample
def generate_sample(sample_size, population):
    sample_heights = []
    for i in range(sample_size):
        index = random.randint(0, len(population) - 1)
        ht = population[index]
        sample_heights.append(ht)
    return sample_heights


def hypothesis_testing_two_tails(sample, m0, a):
    sample_size = len(sample)
    t_a_div_2 = abs(st.t.ppf(a / 2, sample_size - 1))
    sample_mean = sum(sample) / len(sample)
    sample_variance = sum((i - sample_mean) ** 2 for i in sample) / (len(sample) - 1)
    std_error = math.sqrt(sample_variance / sample_size)
    t_stat = (sample_mean - m0) / std_error
    if abs(t_stat) > t_a_div_2:
        return True
    return False

trials  = 10000
rejections = 0
pop_mean_in_conf_interval = 0
sample_size = 30

# type 1 error
for i in range(trials):
    sample = generate_sample(sample_size, population_heights)
    m0 = mean_population_height
    a = 0.05

    hyp_0_rejected = hypothesis_testing_two_tails(sample, m0, 0.05)
    if hyp_0_rejected:
        rejections += 1

    # provided by python
    # t_stat, p_value = st.ttest_1samp(sample, m0)
    # if p_value < a:
    #     rejections += 1



type_1_error_probability = rejections/trials

print(type_1_error_probability)

print(1)
