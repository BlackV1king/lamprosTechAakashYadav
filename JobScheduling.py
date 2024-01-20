# Problem Description: 
# Schedule a list of jobs with deadlines and processing times to maximize the total
# number of jobs completed before their deadlines.

def schedule_jobs( jobs ):
    
    # Sort the jobs based on their deadlines in ascending order
    sorted_jobs = sorted( jobs, key=lambda x: x[0], reverse=True)
    
    # Create a list to store the schedule jobs
    schedule = []
    
    # Initialize Time Counter
    current_time = 0
    
    for job in sorted_jobs:
        # Get the Processing Time and Deadlines
        deadline, processing_time = job
        
        # Check if the most urgent task can be completed within its deadline,
        # If yes, add it to schedule, else skip it
        if current_time + processing_time <= deadline:
            schedule.append(job)
            
            # Updating the current time counter
            current_time += processing_time
            
    return schedule

# Take Input
n = int(input(" Enter number of jobs: "))
jobs = []
for i in range(n):
    jobs.append( list(map(int, input("Enter the (Deadline, Processing_Time) space separated: ").split())))
    
# Print the Answer
print("The scheduled jobs are : ", schedule_jobs(jobs))