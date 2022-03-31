import random
import scipy.stats as st
import math
random.seed(1)

# generate poulation of heights
population_size = 1000
population_heights_1 = []
for i in range(1000):
    ht = random.randint(150, 210)
    population_heights_1.append(ht)

population_heights_2 = population_heights_1.copy()

# generate sample
def generate_sample(sample_size, population):
    sample_heights = []
    for i in range(sample_size):
        index = random.randint(0, len(population) - 1)
        ht = population[index]
        sample_heights.append(ht)
    return sample_heights

def hypothesis_testing_two_populations(sample1, sample2, hyp_diff, a):
    sample_size_1 = len(sample1)
    sample_size_2 = len(sample2)
    t_a_div_2 = abs(st.t.ppf(a / 2, sample_size_1 + sample_size_2 - 2))

    sample_mean_1 = sum(sample1) / len(sample1)
    sample_variance_1 = sum((i - sample_mean_1) ** 2 for i in sample1) / (len(sample1) - 1)

    sample_mean_2 = sum(sample2) / len(sample2)
    sample_variance_2 = sum((i - sample_mean_2) ** 2 for i in sample2) / (len(sample2) - 1)

    pooled_var = ((sample_size_1 - 1) * sample_variance_1 + (sample_size_2 - 1) * sample_variance_2) / (sample_size_1 + sample_size_2 - 2)
    std_error = math.sqrt((pooled_var/sample_size_1) + (pooled_var / sample_size_2))

    t_stat = (sample_mean_1 - sample_mean_2 - hyp_diff) / std_error
    if abs(t_stat) > t_a_div_2:
        return True
    return False

trials  = 100000
rejections = 0
sample_size_1 = 30
sample_size_2 = 25

# type 1 error
for i in range(trials):
    sample1 = generate_sample(sample_size_1, population_heights_1)
    sample2 = generate_sample(sample_size_2, population_heights_2)
    a = 0.05

    # hyp_0_rejected = hypothesis_testing_two_populations(sample1, sample2, 0, a)
    # if hyp_0_rejected:
    #     rejections += 1

    # provided by python
    t_stat, p_value = st.ttest_ind(sample1, sample2, equal_var=True)
    if p_value < a:
        rejections += 1

type_1_error_probability = rejections/trials
print(type_1_error_probability)
print(1)
