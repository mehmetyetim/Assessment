import sys

import pandas as pd

split_list = []

if __name__ == '__main__':
    i = 0
    df = pd.DataFrame()
    print("Log File Analyser" + "\n=================\n")
    print("L: Load / Reload File")
    print("S: Show Basic Statistics")
    print("H: Summarise HTTP Codes\n")
    print("Q: Quit\n")
    while True:
        operation = input("Enter Operation: ")
        if i == 0 and (operation == 'S' or operation == 'H'):
            sys.exit("No log file loaded. Do that first.")
        if operation == 'L':
            i += 1
            exec(open('log_file_generator.py').read())
            log_data = open('access.log', 'r')
            for line in log_data:
                ip = line.split(',')[0]
                uri = line.split(',')[1]
                status_code = int(line.split(',')[2][:3])
                split_list.append([ip, uri, status_code])
            df = pd.DataFrame(split_list, columns=['ip', 'uri', 'status_code'])
        elif operation == 'H':
            print("HTTP Code Summary\n=================\n")
            for i in range(0, len(df['status_code'].unique())):
                print(str(df['status_code'].sort_values().unique()[i]) + ":\t" + str(
                    len(df.loc[df['status_code'] == df['status_code'].sort_values().unique()[i]]))
                      + " (" + str('%.2f' % float(
                    len(df.loc[df['status_code'] == df['status_code'].sort_values().unique()[i]]) * 100 / len(
                        df))) + "%)")

        elif operation == 'S':
            print('Total Entries:', len(df.index))
            break
        elif operation == 'Q':
            sys.exit()
        else:
            raise Exception("The operation you entered is not listed.")
