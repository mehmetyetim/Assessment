import pandas as pd

split_list = []
lap_data = open('lap_times.txt', 'r')
for line in lap_data:
    initial = line.split(',')[0]
    make = line.split(',')[1]
    time = float(line.split(',')[2][:7])
    split_list.append([initial, make, time])

df = pd.DataFrame(split_list, columns=['initial', 'make', 'time'])
grouped = df.groupby(['initial', 'make'])['time']
# grouped is used to take min and mean of each initial
merged = pd.merge(grouped.min(), grouped.mean().round(3), right_index=True, left_index=True)
merged.rename(columns={'time_x': 'min_time', 'time_y': 'mean_time'}, inplace=True)
merged = merged.sort_values(by='min_time').reset_index()
print("Grand Prix Practice Times\n=========================\n")
for index, row in merged.iterrows():
    print(row['initial'],
          '(' + row['make'] + ')', end='')
    for i in range(int(len(row['make']) / 5), 3):
        print('\t', end='')
    print(str(row['min_time']) + ' (Avg: ' + str(row['mean_time']) + ')')