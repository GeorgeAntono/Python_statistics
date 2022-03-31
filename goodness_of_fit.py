import random
import scipy.stats as st

random.seed(1)

def count_between_limits(sample_values, bin_min, bin_max):
    between = 0
    for i in sample_values:
        if i > bin_min and i <= bin_max:
            between += 1
    return between


def count_observed_frequencies_from_sample(sample_values, bin_list):
    result_freqs = []
    width = bin_list[1] - bin_list[0]
    for i in range(len(bin_list)):
        bin_min = bin_list[i]
        bin_max = bin_list[i] + width

        sum_of_occurences = count_between_limits(sample_values, bin_min, bin_max)
        sum_of_occ = sum(map(lambda x : x > bin_min and x <= bin_max, sample_values))
        result_freqs.append(sum_of_occurences)

    return result_freqs


def get_expected_for_normal_distribution(bin_list, sample_size, hyp_mean=None, hyp_std=None):
    expected = []
    width = bin_list[1] - bin_list[0]
    for i in range(len(bin_list)):
        bin_min = bin_list[i]
        bin_max = bin_list[i] + width

        prob_max = st.norm.cdf(bin_max, loc=hyp_mean, scale=hyp_std)
        prob_min = st.norm.cdf(bin_min, loc=hyp_mean, scale=hyp_std)
        prob_of_bin = prob_max - prob_min

        standardized_bin_min = (bin_min - hyp_mean) / hyp_std
        standardized_bin_max = (bin_max - hyp_mean) / hyp_std

        prob_max2 = st.norm.cdf(standardized_bin_max)
        prob_min2 = st.norm.cdf(standardized_bin_max)

        expected.append(prob_of_bin * sample_size)
    return expected

trials = 1000
rej = 0

for t in range(trials):
    sample_size = 10000
    sample_values = []

    mean = 500
    std_dev = 30
    for i in range(sample_size):
        sample_values.append(random.normalvariate(500, 30))

    # print(sample_values)

    minim = min(sample_values)
    maxim = max(sample_values)

    # print(min)
    # print(max)

    minim_value = 380
    maxim_value = 610

    rng = maxim_value - minim_value

    bins = 10
    width = rng/10

    bin_list = []


    for i in range(bins):
        bin_list.append(minim_value + i * width)

    observed_frequencies = count_observed_frequencies_from_sample(sample_values, bin_list)
    expected_frequencies = get_expected_for_normal_distribution(bin_list, len(sample_values), mean, std_dev)

    result = st.chisquare(observed_frequencies, expected_frequencies, ddof = 0)

    if result.pvalue < 0.05:
        rej += 1
        print(str(t) + " REJECT")
    else:
        print(str(t) + " NOT REJECT")



print(rej/trials)
