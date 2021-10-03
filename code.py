import pandas as pd
import statistics
import csv

df=pd.read_csv("StudentsPerformance.csv")
math_list=df["math score"].to_list()

height_mean=statistics.mean(math_list)

height_median=statistics.median(math_list)

height_mode=statistics.mode(math_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))


height_stdev=statistics.stdev(math_list)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_stdev, height_mean+height_stdev

height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_stdev), height_mean+(2*height_stdev)

height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_stdev), height_mean+(3*height_stdev)



math_list_of_data_within_1_std_deviation = [result for result in math_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]

math_list_of_data_within_2_std_deviation = [result for result in math_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]

math_list_of_data_within_3_std_deviation = [result for result in math_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]


print("{}% of data for height lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list))) 
print("{}% of data for height lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list))) 
