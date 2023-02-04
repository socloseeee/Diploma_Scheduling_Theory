# Diploma_Scheduling_Theory
Solving an inhomogeneous minemax problem of scheduling theory by the goldberg method with different formation of the initial generation.
For the formation of the initial generation, algorithms are considered: The method of minimal elements, the Plotnikov-Zverev method, the method of squares and the barrier method

### The method of minimal elements
The essence of this method is that we simply take the smallest element from each line.
![Метод минмальных элементов](https://user-images.githubusercontent.com/65871712/216768440-aeac3a1b-0636-4588-88b1-6699748891b9.png)
### The Plotnikov-Zverev method
A one-dimensional array is formed equal to the number of elements in each row of the matrix. 
We move this one-dimensional array from the first row of the matrix. 
For each iteration, we add index-wise the elements of the matrix row and one-dimensional array, then compare and add the element that gives us the smallest difference between the elements of the one-dimensional array.
![Метод Плотникова-Зверева](https://user-images.githubusercontent.com/65871712/216768443-5dc60ea9-b155-496d-b1a9-170d5b94466e.png)
### The method of squares
The same as the Plotnikov-Zverev method, only when adding we square the sum and then select the element with the least square of the sum.
![Метод квадратов](https://user-images.githubusercontent.com/65871712/216768448-0c64235f-b475-4db1-b6e5-ea6e17fb0e7c.png)
### The barrier method(hybrid of 1 and 2 methods)
The barrier is calculated equal to the sum of loads per processor using the method of minimum elements divided by the number of processors.
Before the barrier (-), we calculate by the method of minimal elements, and after by the Plotnikov-Zverev method.
![Метод барьера](https://user-images.githubusercontent.com/65871712/216768451-69018814-bd08-4b80-a3a7-9ad8f97dfb55.png)
## Directory description
Diploma_Scheduling_Theory/diploma/experiments - this is a directory in which, through multiple iterations, the results of the GA execution under different conditions are singled out for the purpose of their subsequent comparison.

Diploma_Scheduling_Theory/diploma/methods_analysis - this is a directory in which we can carefully verify that all the given methods work correctly and check the results of their execution.
