# Diploma_Scheduling_Theory
Solving an inhomogeneous minemax problem of scheduling theory by the goldberg method with different formation of the initial generation.
For the formation of the initial generation, algorithms are considered: The method of minimal elements, the Plotnikov-Zverev method, the method of squares and the barrier method

### The method of minimal elements
The essence of this method is that we simply take the smallest element from each line.

![Метод минмальных элементов](https://user-images.githubusercontent.com/65871712/216844865-c2ba9ff0-0cd9-4bf7-a0a6-f49ba334baec.png)

*screen from methods_analysis.py*
### The Plotnikov-Zverev method
A one-dimensional array is formed equal to the number of elements in each row of the matrix. 
We move this one-dimensional array from the first row of the matrix. 
For each iteration, we add index-wise the elements of the matrix row and one-dimensional array, then compare and add the element that gives us the smallest difference between the elements of the one-dimensional array.

![Метод Плотникова-Зверева](https://user-images.githubusercontent.com/65871712/216844871-f02687c4-6b9f-48b2-82e6-5edc6f5c0917.png) 
*screen from methods_analysis.py*
### The method of squares
The same as the Plotnikov-Zverev method, only when adding we square the sum and then select the element with the least square of the sum.

![Метод квадратов](https://user-images.githubusercontent.com/65871712/216844874-3cee8510-4f5f-4b61-8c99-471bd514c546.png)

*screen from methods_analysis.py*
### The barrier method(hybrid of 1 and 2 methods)
The barrier is calculated equal to the sum of loads per processor using the method of minimum elements divided by the number of processors.
Before the barrier (-), we calculate by the method of minimal elements, and after by the Plotnikov-Zverev method.

![Метод барьера](https://user-images.githubusercontent.com/65871712/216844878-f418f483-3b91-40f1-b7ef-3178f9afffa1.png)

*screen from methods_analysis.py*
## Directory description
Diploma_Scheduling_Theory/diploma/experiments - this is a directory in which, through multiple iterations, the results of the GA execution under different conditions are singled out for the purpose of their subsequent comparison.

Diploma_Scheduling_Theory/diploma/methods_analysis - this is a directory in which we can carefully verify that all the given methods work correctly and check the results of their execution.
