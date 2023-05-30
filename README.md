# Diploma_Scheduling_Theory

<img src="https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/8d9e7e06-78fd-434c-86dc-58ea214db03e" width="500" height="250"></a>
<img src="https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/c2f258c2-bc62-43fa-8383-2f01b4872232" width="500" height="250"></a>

## Navigation:

##### 1. [Problem](#problem)
##### 2. [Libraries](#libraries)
##### 3. [What programm do?](#wpd?)
##### 4. [Results](#results)

### 1. Problem <a name="problem"></a>:
The problem of scheduling theory is to efficiently allocate resources over time to achieve specific goals. This problem is important in a wide range of fields, including manufacturing, transportation, healthcare, and computer science. By developing effective scheduling algorithms, businesses and organizations can optimize their operations, reduce costs, and improve productivity. 

### 2. Libraries <a name="libraries"></a>:
[![tqdm](https://img.shields.io/badge/tqdm-black?style=for-the-badge&logo=tqdm&logoColor=white)]("https://tqdm.github.io/")

[![matplotlib](https://img.shields.io/badge/matplotlib-blue?style=for-the-badge&logo=anaconda&logoColor=white)]("https://matplotlib.org/stable/index.html")

[![numpy](https://img.shields.io/badge/numpy-green?style=for-the-badge&logo=numpy)]("https://numpy.org/")

[![pyqt5](https://img.shields.io/badge/pyqt5-red?style=for-the-badge&logo=qt&logoColor=white)]("https://pypi.org/project/PyQt5")

[![sqlite3](https://img.shields.io/badge/sqlite3-gold?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/index.html)

### 3. What programm do? <a name="wpd"></a>:
The program facilitates the creation of an initial population through various partitioning techniques, which will be further elucidated. Moreover, it enables the generation of initial genes based on specific boundaries between two processors.

#### Methods for the formation of the initial generation
*All screens are from methods_analysis.py*

#### The method of minimal elements
The essence of this method is that we simply take the smallest element from each line.

![Метод минмальных элементов](https://user-images.githubusercontent.com/65871712/216844865-c2ba9ff0-0cd9-4bf7-a0a6-f49ba334baec.png)

#### The Plotnikov-Zverev method
A one-dimensional array is formed equal to the number of elements in each row of the matrix. 
We move this one-dimensional array from the first row of the matrix. 
For each iteration, we add index-wise the elements of the matrix row and one-dimensional array, then compare and add the element that gives us the smallest difference between the elements of the one-dimensional array.

![Метод Плотникова-Зверева](https://user-images.githubusercontent.com/65871712/216844871-f02687c4-6b9f-48b2-82e6-5edc6f5c0917.png) 

#### The barrier method(hybrid of 1 and 2 methods)
The barrier is calculated equal to the sum of loads per processor using the method of minimum elements divided by the number of processors.
Before the barrier (-), we calculate by the method of minimal elements, and after by the Plotnikov-Zverev method.

![Метод барьера](https://user-images.githubusercontent.com/65871712/216844878-f418f483-3b91-40f1-b7ef-3178f9afffa1.png)


### 4. The results <a name="results"></a>:
*Screen is from experiments.py*
![216846398-968f404b-8b61-423b-902b-14323f54bb0d](https://user-images.githubusercontent.com/65871712/216846824-0aa1f0d9-1c67-4031-b387-67a0bd255eb8.png)

*Screens are from app.py*

![tmponigzmg9](https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/111ce607-68cd-4bfb-9b76-fdb3cd15f47b)

![tmp80ypndqj](https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/1078471b-ed04-478a-af4e-a53707fd171b)

![tmpqqc8eu0_](https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/546d37ef-71f1-4d24-80af-d07b7812b0a2)

![tmp2fjesezk](https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/c8151188-a17b-4d6a-a2e2-65b3e31b5f9c)

![tmpvuhtdovy](https://github.com/socloseeee/Diploma_Scheduling_Theory/assets/65871712/d65eeeb5-da05-4f29-b17d-9adff167f14d)
