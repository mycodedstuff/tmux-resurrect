import psutil
import sys

child_process = psutil.Process(int(sys.argv[1])).children()

process_command = ""

if len(child_process) == 1:
    for arg in child_process[0].cmdline():
        if " " in arg:
            process_command += '"' + arg + '" '
        else: process_command += (arg + " ")


process_command = process_command.replace("\'", "'")
print(process_command)

