# Diploma_Scheduling_Theory
Solving an inhomogeneous minemax problem of scheduling theory by the goldberg method with different formation of the initial generation.
For the formation of the initial generation, algorithms are considered: The method of minimal elements, the Plotnikov-Zverev method, the method of squares and the barrier method

### Libraries:
<a href="https://tqdm.github.io/"><img src="https://user-images.githubusercontent.com/65871712/218452173-faa8ad53-1248-441a-8638-6685d10fdfe1.png" alt="tqdm" width="100" height="100"></a>
<a href="https://matplotlib.org/stable/index.html"><img src="https://user-images.githubusercontent.com/65871712/218449590-b1a28106-1c93-487a-a74a-eefe422006a5.png" alt="matplotlib" width="100" height="100"></a>
<a href="https://numpy.org/"><img src="https://user-images.githubusercontent.com/65871712/218452060-ed889a4c-caad-4900-bf59-b030c2794247.png" alt="numpy" width="100" height="100"></a>

<a href="https://pypi.org/project/colorama/"><img src="https://user-images.githubusercontent.com/65871712/218449346-3b8335f9-5974-4d47-a385-5ce6e3666891.png" alt="colorama" width=310 height=50></a>

## The essence of the work
Form the initial generation using various methods and compare their effectiveness as a solution to the distribution problem of scheduling theory using the Goldberg method.
### Algorythm(n repeats):
1. We choose how we form the initial generation. For example, 50 randomly + 50 by determinate method, etc.
2. Choose determinate method (a little below there is a brief description of each method) to form initial generation
3. This is where GA (Genethic Algorythm) comes into play. We take z individuals. Crossing with each other using the crossover operation, along the way, do not forget about mutations! At the end, we compare the loads of the best children with their parents and select the best individuals for subsequent generations. This is all we do until the best result of the load in generation is repeated k times.

## Methods for the formation of the initial generation
*All screens are from methods_analysis.py*

### The method of minimal elements
The essence of this method is that we simply take the smallest element from each line.

![Метод минмальных элементов](https://user-images.githubusercontent.com/65871712/216844865-c2ba9ff0-0cd9-4bf7-a0a6-f49ba334baec.png)

### The Plotnikov-Zverev method
A one-dimensional array is formed equal to the number of elements in each row of the matrix. 
We move this one-dimensional array from the first row of the matrix. 
For each iteration, we add index-wise the elements of the matrix row and one-dimensional array, then compare and add the element that gives us the smallest difference between the elements of the one-dimensional array.

![Метод Плотникова-Зверева](https://user-images.githubusercontent.com/65871712/216844871-f02687c4-6b9f-48b2-82e6-5edc6f5c0917.png) 

### The method of squares
The same as the Plotnikov-Zverev method, only when adding we square the sum and then select the element with the least square of the sum.

![Метод квадратов](https://user-images.githubusercontent.com/65871712/216844874-3cee8510-4f5f-4b61-8c99-471bd514c546.png)

### The barrier method(hybrid of 1 and 2 methods)
The barrier is calculated equal to the sum of loads per processor using the method of minimum elements divided by the number of processors.
Before the barrier (-), we calculate by the method of minimal elements, and after by the Plotnikov-Zverev method.

![Метод барьера](https://user-images.githubusercontent.com/65871712/216844878-f418f483-3b91-40f1-b7ef-3178f9afffa1.png)


## The result of work with various formations of the initial generation
*Screen is from experiments.py*
![216846398-968f404b-8b61-423b-902b-14323f54bb0d](https://user-images.githubusercontent.com/65871712/216846824-0aa1f0d9-1c67-4031-b387-67a0bd255eb8.png)

*Screens are from visualizing_histogram.py*

![image](https://user-images.githubusercontent.com/65871712/218283100-528414bd-0ded-4d2d-b133-bf1970947cbb.png)

![image](https://user-images.githubusercontent.com/65871712/218254541-6d6d1ee9-418e-4949-a8d0-37e5cfcfc2ba.png)

![image](https://user-images.githubusercontent.com/65871712/218282253-48925756-8f1f-413f-9421-61a920cf8512.png)

![image](https://user-images.githubusercontent.com/65871712/218282259-b20de175-5f61-4cf2-8bdf-990f91966572.png)

![image](https://user-images.githubusercontent.com/65871712/218282241-1d7a8fff-b064-4303-bbc0-d06b49975812.png)


## Directory description
Diploma_Scheduling_Theory/diploma/experiments - this is a directory in which, through multiple iterations, the results of the GA execution under different conditions are singled out for the purpose of their subsequent comparison.

Diploma_Scheduling_Theory/diploma/methods_analysis - this is a directory in which we can carefully verify that all the given methods work correctly and check the results of their execution.
