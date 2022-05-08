import sys


# user needs to load file after each time program gives the option of load
def layout():
    i = 0
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
            i+=1
            with open("access.log", "r") as f:
                lines = f.read()
            attempts = lines.split("\n")
            status_codes_list = []
            for i in range(len(attempts)):
                uri = attempts[i].split(',')[1]
                status_code = attempts[i].split(',')[2]
                status_codes_list.append(status_code)
        elif operation == 'S':
            print('Total Entries:',len(attempts))
            break;
        elif operation == 'H':
            print("HTTP Code Summary\n=================\n")
            print("200 : \t" + str(status_codes_list.count("200")) +
                  "(" + str(status_codes_list.count("200") / len(status_codes_list)) + "%)")
            print("201 : \t" + str(status_codes_list.count("201")) +
                  "(" + str(status_codes_list.count("201") / len(status_codes_list)) + "%)")
            print("400 : \t" + str(status_codes_list.count("400")) +
                  "(" + str(status_codes_list.count("400") / len(status_codes_list)) + "%)")
            print("401 : \t" + str(status_codes_list.count("401")) +
                  "(" + str(status_codes_list.count("401") / len(status_codes_list)) + "%)")
            print("404 : \t" + str(status_codes_list.count("404")) +
                  "(" + str(status_codes_list.count("404") / len(status_codes_list)) + "%)")
            print("500 : \t" + str(status_codes_list.count("500")) +
                  "(" + str(status_codes_list.count("500") / len(status_codes_list)) + "%)")
            layout()
        elif operation == 'Q':
            sys.exit()
        else:
            raise Exception("The operation you entered is not listed.")



if __name__ == '__main__':
    layout()
