import random
import math
import scipy.stats as st
random.seed(1)
beta_0 = 50
beta_1 = 2
error_variance = 0.8

x_values = [10, 15, 20, 40, 42, 45, 60]

def get_sample_values(x_values, beta_0, beta_1, error_variance):
    result = []
    std_error = math.sqrt(error_variance)
    for x in x_values:
        error_term = random.normalvariate(0, std_error)
        yi = beta_0 + beta_1 * x + error_term
        result.append(yi)
    return result

def get_b1_value(x_values, y_values):
    x_mean = sum(x_values)/len(x_values)
    y_mean = sum(y_values) / len(y_values)
    nominator = 0
    denominator = 0
    for i in range(len(x_values)):
        xi = x_values[i]
        yi = y_values[i]
        nominator += ((xi-x_mean) * (yi - y_mean))
        denominator += ((xi-x_mean)**2)
    res = nominator / denominator
    return res

def get_b0_value(x_values, y_values, b1):
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)
    return y_mean - (b1 * x_mean)


def get_SSE_value(b0, b1, x_values, y_values):
    result = 0
    for i in range(len(x_values)):
        x_i = x_values[i]
        y_pred = b0 + b1 * x_i
        y_i = y_values[i]
        result += ((y_pred - y_i) ** 2)
    return result

def get_SST_value(y_values):
    y_mean = sum(y_values)/len(y_values)
    res = 0
    for y_i in y_values:
        res += ((y_i - y_mean)**2)
    return res


def get_std_error_b1(se_2, x_values):
    denominator = 0
    x_mean = sum(x_values)/len(x_values)
    for x_i in x_values:
        denominator += ((x_i - x_mean) ** 2)
    denominator = math.sqrt(denominator)
    return se_2 / denominator

def b1_hypothesis(alpha, b1, hyp_beta1, df, std_error_b1_estimator):
    t = (b1 - hyp_beta1) / std_error_b1_estimator
    t_crit = abs(st.t.ppf(alpha/2, df))
    p_value = 2 * st.t.cdf(-abs(t), df)
    if abs(t) > t_crit:
        return True
    return False

beta1_in_conf_interval = 0
rejections = 0
trials = 100000
sum_b1 = 0
for i in range(trials):
    y_values = get_sample_values(x_values, beta_0, beta_1, error_variance)
    # for i in range(len(x_values)):
    #     print (str (x_values[i]) + " " + str(y_values[i]))
    b1 = get_b1_value(x_values, y_values)
    b0 = get_b0_value(x_values, y_values, b1)
    SSE = get_SSE_value(b0, b1, x_values, y_values)
    SST = get_SST_value(y_values)
    SSR = SST - SSE
    R_squared = SSR/SST
    # print(R_squared)
    MSE = SSE / (len(y_values) - 2)
    std_dev_errors_from_sample = math.sqrt(MSE)
    std_error_b1_estimator = get_std_error_b1(std_dev_errors_from_sample, x_values)
    alpha = 0.05
    conf_level = 1 - alpha
    t_student_val = abs(st.t.ppf(alpha/2, len(x_values) - 2))
    conf_inerval_beta1_a = b1 - t_student_val * std_error_b1_estimator
    conf_inerval_beta1_b = b1 + t_student_val * std_error_b1_estimator

    if beta_1 >= conf_inerval_beta1_a and beta_1 <= conf_inerval_beta1_b:
        beta1_in_conf_interval += 1

    hyp_beta1 = 2
    rejected = b1_hypothesis(alpha, b1, hyp_beta1, len(x_values) - 2, std_error_b1_estimator)
    if rejected:
        rejections += 1

    sum_b1 += b1

prob = beta1_in_conf_interval / trials
print(prob)

prob_rej = rejections/trials
print(prob_rej)

avg_b1 = sum_b1 / trials
print(avg_b1)
