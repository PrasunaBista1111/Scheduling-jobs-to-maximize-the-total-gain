
• Problem
The goal of this algorithm is to efficiently schedule jobs to maximize the total gain. Each job must be completed within a specific deadline to yield a gain. If a job isn't completed by its deadline, it provides no gain. We need a scheduling strategy that ensures maximum total gain.

• Approach
I will sort the jobs in descending order of gains. In case of tie on gains, I'll sort them in ascending order of deadlines.
After sorting, I'll attempt to schedule each job, checking the available slots in descending order from its deadline.




• Explanation
The greedy algorithm works here because once I've sorted the jobs by their gain (and then by their deadline for ties), I're ensuring that I am giving the higher gain jobs the best chances of being scheduled by checking for available slots starting from their deadline and moving backwards.



Calculating the Time Complexity :

-Reading the Jobs: O(n), where n is the number of jobs in the input file.

-Sorting the Jobs: O(n log n)

-Finding the Maximum Deadline: O(n)

-Scheduling Jobs: O(n^2), 

-Writing the Output: O(n + max_deadline)


The time complexity of the algorithm is O(n^2), primarily because we have a loop that goes through each job, and for each job, there is another nested loop that iterates through available time slots. The nested loop, in this case, is the dominant factor contributing to the overall time complexity.
