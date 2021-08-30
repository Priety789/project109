import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
df_list1 = df["race/ethnicity"].tolist()
df_list2 = df["gender"].tolist()
result = []
count = []
for i in range(0, 1000):
    data1 = random.randint(1, len(df_list1))
    data2 = random.randint(1, len(df_list2))
    result.append(data1 + data2)
    count.append(i)
mean = sum(result)/len(result)
median = statistics.median(result)
mode = statistics.mode(result)
std_deviation = statistics.stdev(result)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
fig = ff.create_distplot([result], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.show()
list_of_data_within_1_std_deviation = [result for result in result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in result if result > third_std_deviation_start and result < third_std_deviation_end]
print("mean of this data is {}".format(mean))
print("median of this data is {}".format(median))
print("mode of this data is {}".format(mode))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(result)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(result))) 
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(result)))