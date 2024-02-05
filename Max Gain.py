

""" Pseudocode:


Function read_jobs():
    Read the filename from command line arguments
    Open the file with the given filename
    Create an empty list 'jobs'
    For each line in the file:
        Parse the line into (id, end_time, gain) as integers
        Add (id, end_time, gain) to 'jobs'
    Close the file
    Return 'jobs'

Function job_scheduling(jobs):
    Sort 'jobs' by descending gain and ascending end_time
    Initialize 'vacancy' as an empty list
    Initialize 'total_gain' to 0
    For each 'job' in the sorted 'jobs':
        For 't' in range from job's end_time down to 1:
            If 'vacancy[t]' is empty:
                Assign 'job[0]' to 'vacancy[t]'
                Add 'job[2]' to 'total_gain'
                Exit the inner loop
    Return 'vacancy' and 'total_gain'

Function write_output(file_name, jobs, slots, total_gain):
    Open the file with the given 'file_name' for writing
    For each 'job' in 'jobs':
        Write 'job' details to the file
    For each 'job_id' from 1 to the number of jobs:
        Determine the 'end_time' from 'slots'
        Write 'job_id' and 'end_time' to the file
    Write 'total_gain' to the file

 main program:
    Define the output file path (e.g., "output.txt")
    Call 'read_jobs' to read job data
    Call 'job_scheduling' to schedule the jobs and get 'slots' and 'total_gain'
    Call 'write_output' to write the results to the output file

"""

import os
import sys


def read_jobs():
    file_name = sys.argv[1]
    with open(file_name, "r") as f:
        jobs = []
        for line in f:
            text = line.strip().split()
            (id, end_time, gain) = map(int, text)
            jobs.append((id, end_time, gain))      

    
    return jobs

def job_scheduling(jobs):
    jobs = sorted(jobs, key=lambda x: (-x[2], x[1])) 
    maximum_deadline = max([job[1] for job in jobs])
    vacancy = [0] * (maximum_deadline + 1)

    total_gain = 0
    
    for job in jobs:
        for t in range(job[1], 0, -1):  # Check available vacancy from the job's deadline down to 1
            if vacancy[t] == 0:
                vacancy[t] = job[0]
                total_gain += job[2]
                break

    return vacancy, total_gain

def write_output(file_name, jobs, slots, total_gain):
    with open(file_name, "w") as f:
        for id, end_time, gain in jobs:
            f.write(f"{id} {end_time} {gain}\n")
        for job_id in range(1, len(jobs) + 1):
            end_time = slots.index(job_id) if job_id in slots else 0
            f.write(f"{job_id} {end_time}\n")
        f.write(str(total_gain))

if __name__ == "__main__":
    # input_filepath = "input.txt"
    output_filepath = "output.txt"
    jobs = read_jobs()
    slots, total_gain = job_scheduling(jobs)
    write_output(output_filepath, jobs, slots, total_gain)
