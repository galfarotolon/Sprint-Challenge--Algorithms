#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity: O(n) - Linear Time
    There is a single while loop that iterates n number of times, increasing
    proportionally depending on the value of n. 


b) Runtime complexity: O(n ^ 2) - 
    There are 2 loops (one loop inside another) increasing runtime complexity 
    exponentially. 


c) Runtime complexity: O(n) - Linear Time
    There are no loops, however as this function is calling itself via recursion,
    will cause the function to essentially loop itself n number of times, increasing linearly depending of the value of n. 

## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->


This problem can be tackled by using a binary search algorithm. Steps to figure 
out the floor at which the egg by breaking the fewer possible eggs:

1- Check the mid floor of the building and throw an egg from there - if it breaks
then check the mid-bottom half, if it doesn't break then check the mid-top half

example: if there are 10 floors, begin at 5. If the egg breaks at 5 then you can automatically discard the top floors, but if it doesn't break then you can discard the bottom floors. Repeat this by setting the current floor where the egg is thrown to the mid of the bottom or top half, narrowing the search by 1/2 each time until the floor is found

2 - Whatever the outcome is, the other half will be discarded and no further interaction is needed with it (reduces floor search by half after each throw).

As it is a binary search algorithm, the runtime complexity will be of O(log n).

