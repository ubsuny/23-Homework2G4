# Documentation for our Project.
#### We have chosen the return of diagnol to compare the execution time of different implementions and Einstein notation.
##### 1. First, we carried out the coding using naive loop based implementation for the return of diagnol. We have used the code for the return of diagnol of 3*3 matrix.
   
   import numpy as np
import time

def diagonal_elements(matrix):
    n = len(matrix)
    diagonal = []

    # Start measuring time for the loop
    start_time = time.time()

    for i in range(n):
        diagonal.append(matrix[i][i])
###### The example of the unit test is given below. We used 3*3 matrix here.
      
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]                # Replace with your matrix
diagonal, loop_time = diagonal_elements(matrix)
m1=loop_time
print("Diagonal elements:", diagonal)
print("Loop execution time:", m1)

###### And, we got the execution time 2.86102294921875e-06.

Diagonal elements: [1, 5, 9]
Loop execution time: 2.86102294921875e-06
