import random
import scipy.stats as st
import numpy as np

observed_values = np.array([[12, 4], [52, 23]])

dof = observed_values.size - sum(observed_values.shape) + observed_values.ndim - 1



chi_stat, p, dof, exp = st.chi2_contingency(observed_values, correction=False)


# https://en.wikipedia.org/wiki/Yates%27s_correction_for_continuity#:~:text=To%20reduce%20the%20error%20in,2%20%C3%97%202%20contingency%20table.
print(st.chi2_contingency(observed_values, correction=False))
print(st.chi2_contingency(observed_values))
