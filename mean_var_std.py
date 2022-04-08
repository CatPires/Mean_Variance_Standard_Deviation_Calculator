import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  my_arr = [[list[0], list[1], list[2]], [list[3], list[4], list[5]], [list[6], list[7], list[8]]]

  # axis 1
  ax1_mean = [np.mean([i[0] for i in my_arr]), np.mean([i[1] for i in my_arr]), np.mean([i[2] for i in my_arr])]
  ax1_variance = [np.var([i[0] for i in my_arr]), np.var([i[1] for i in my_arr]), np.var([i[2] for i in my_arr])]
  ax1_std_deviation = [np.std([i[0] for i in my_arr]), np.std([i[1] for i in my_arr]), np.std([i[2] for i in my_arr])]
  ax1_max = [np.max([i[0] for i in my_arr]), np.max([i[1] for i in my_arr]), np.max([i[2] for i in my_arr])]
  ax1_min = [np.min([i[0] for i in my_arr]), np.min([i[1] for i in my_arr]), np.min([i[2] for i in my_arr])]
  ax1_sum = [np.sum([i[0] for i in my_arr]), np.sum([i[1] for i in my_arr]), np.sum([i[2] for i in my_arr])]

  # axis 2
  ax2_mean = [np.mean(my_arr[0]), np.mean(my_arr[1]), np.mean(my_arr[2])]
  ax2_variance = [np.var(my_arr[0]), np.var(my_arr[1]), np.var(my_arr[2])]
  ax2_std_deviation = [np.std(my_arr[0]), np.std(my_arr[1]), np.std(my_arr[2])]
  ax2_max = [np.max(my_arr[0]), np.max(my_arr[1]), np.max(my_arr[2])]
  ax2_min = [np.min(my_arr[0]), np.min(my_arr[1]), np.min(my_arr[2])]
  ax2_sum = [np.sum(my_arr[0]), np.sum(my_arr[1]), np.sum(my_arr[2])]

  # axis 3
  ax3_mean = np.mean(my_arr)
  ax3_variance = np.var(my_arr)
  ax3_std_deviation = np.std(my_arr)
  ax3_max = np.max(my_arr)
  ax3_min = np.min(my_arr)
  ax3_sum = np.sum(my_arr)

  #final
  calculations = {}
  calculations['mean'] = [ax1_mean, ax2_mean, ax3_mean]
  calculations['variance'] = [ax1_variance, ax2_variance, ax3_variance]
  calculations['standard deviation'] = [ax1_std_deviation, ax2_std_deviation, ax3_std_deviation]
  calculations['max'] = [ax1_max, ax2_max, ax3_max]
  calculations['min'] = [ax1_min, ax2_min, ax3_min]
  calculations['sum'] = [ax1_sum, ax2_sum, ax3_sum]

  return calculations