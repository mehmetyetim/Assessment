import sys
import pandas
import pandas as pd

print("Grand Prix Race Times")
race_name = input("Enter name of race: ")
driver_name_time = input("Enter Driver and Time [Enter to Finish]: ")
table = pd.DataFrame(columns=["name", "time"])

if driver_name_time == "":
    sys.exit("No data entered.")
while True:
    driver_name = driver_name_time[:3]
    driver_time = float(driver_name_time[3:])
    new_row = {
        'name': [driver_name],
        'time': [driver_time]
    }
    # it generates data frame from dictionary
    new_data_frame = pandas.DataFrame.from_dict(new_row)
    table = pd.concat([table, new_data_frame], ignore_index=True)
    driver_name_time = input("Enter Driver and Time [Enter to Finish]: ")
    if driver_name_time == "":
        break
if race_name == "":
    print("\nGrand Prix de Yorkshire Timings")
    print("===============================\n")
else:
    print("\nGrand Prix de Yorkshire Timings".replace("Yorkshire", race_name))
    print("==============", end="")
    i = 0
    while i < len(race_name):
        print("=", end="")
        i = i + 1
    print("========\n")
# it generates the number of unique driver name
if table['name'].nunique() == 1:
    print(table['name'].nunique(), "Driver Entered.\n")
else:
    print(table['name'].nunique(), "Drivers Entered.\n")

# it generates the table which the titles are laps, fast, slow, mean
df = pd.concat([table['name'].value_counts().rename('Laps'),
                table.groupby(['name'])['time'].min().rename('Fast'),
                table.groupby(['name'])['time'].max().rename('Slow'),
                table.groupby(['name'])['time'].mean().round(decimals=3).rename('Mean')
                ], axis=1)
print(df.sort_values('Fast', ascending=False))
