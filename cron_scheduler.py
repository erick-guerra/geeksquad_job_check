import sys
import os
import subprocess
from datetime import datetime

#TODO: Resolve windows task schedulin issue.

def time_convert(time):
    """ Converts user time input into military time for windows task scheduler """
    return datetime.strptime(time, '%I:%M:%S%p').strftime('%H:%M:%S') #Input should be HH:MM:SSam/pm

def create_schedule(task_name, task_run, schedule, start_time):
    cmd = "schtasks /create /tn '{tn}', /tr {tr}, /sc {sc} /st {st}".format(tn=task_name, tr=task_run, sc=schedule, st=start_time)
    subprocess.call(cmd)