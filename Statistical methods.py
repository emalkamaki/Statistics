""" Calculate confidence intervals using bootstrapping """
import numpy as np
import dc_stat_think as dcst

# Compute mean 
mean_x = np.mean(x)

# Draw bootstrap replicates
bs_reps_x = dcst.draw_bs_reps(x, np.mean, size=10000)

# Compute 95% confidence intervals
conf_int_x = np.percentile(bs_reps_x, [2.5, 97.5])

# Print the results
print("""
x:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
""".format(mean_wt, *conf_int_wt))

""" Test hypothesis with a p-value using permutation """
# Compute the difference of means: x, y
diff_means = np.mean(x) - np.mean(y)

# Draw permutation replicates: perm_reps
perm_reps = dcst.draw_perm_reps(x, y, dcst.diff_of_means, size=10000)

# Compute the p-value: p-val
p_val = np.sum(perm_reps >= diff_means) / len(perm_reps)

# Print the result
print('p =', p_val)

""" Compute p-value using bootstrapping, two arrays of data """
# Compute the difference of means: x, y
diff_means = np.mean(x) - np.mean(y)

# Concatenate arrays: x_y_concat
x_y_concat = np.concatenate((x, y))

# Compute mean of all: mean_x_y
mean_x_y = np.mean(x_y_concat)

# Generate shifted arrays
x_shifted = x - np.mean(x) + mean_x_y
y_shifted = y - np.mean(y) + mean_x_y

# Compute 10,000 bootstrap replicates from shifted arrays
bs_reps_x = dcst.draw_bs_reps(x_shifted, np.mean, size=10000)
bs_reps_y = dcst.draw_bs_reps(y_shifted, np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_reps = bs_reps_x - bs_reps_y

# Compute and print p-value: p. The diff_means is the original before shift
p = np.sum(bs_reps >= diff_means) / len(bs_reps)
print('p-value =', p)
