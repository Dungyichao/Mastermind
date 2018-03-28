# Mastermind
This is a program to guess the code. The algorithm implemented in this file can reach about 5.18 times of guessing in average. You can find two python file. The ```mastermind_final.ipynb``` file is a breakdown explanation on playing one time game. The ```mastermind_final.py``` file is to obtain the average number of guessing times after playing 10000 times. Recently, our algorithm is able to obtain average guessing time 5.18 for 10000 plays. The maximum guessing time is 7. You can find the result from the .csv file ```mastermind_final.csv```. 
## 1. About the game<br />
This game also names Bulls and Cows and it involves two persons(ex. Tom, Jack). Each of the player will think of a sequence of 4 digit number without duplicate such as 1234 or 4705. One of the player need to guess another player's answer. During the guessing process, Tom will guess a sequence of number and Jack will response the guessing with two number **A** and **B**.  **A** represents the number of digit with correct value as well as the correct position. **B** represents the number of digit with correct value but wrong position. Tom will give another guess based on the information of A and B and then Jack will give another A, B value as response. The guessing process will terminate untill Tom comes up with the right answer of Jack.<br />

Example: If the real answer is 5032 and our guess is 4023. Then A = 1 because "0" is at the correct position and it is the right value. B = 2 because the anser contains digit "2" and digit "3" but they are at the incorrect position.<br />

It is proven that any number could be solved within seven turns. <br />

## 2. How we design the program<br />
We have a code set containing 5040 combination of 4 digit number without duplicate. We first randomly use a guess and receive the response of A and B. Based on the value of A and B, we remove the element from the code set which is not going to be the correct answer. We then pick up an element from the code set for the next play and receive A and B value. The method of how we pick up the element for the next play will be elaborate more later. We will keep guessing until we get A=4 and B=0 (it means we get 4 digit with correct position and value).<br />
### Which element need to be removed from the code set<br />
In the original code set, there is 0123, 0124, 0125, 0126....... and so on(totally 5040 elements in the beginning). If our first guess is 0521 and receive A=2, B=1. 0123 might be the answer because it will give us the same A and B value, so we keep it in the code set. However 0124 will not be the answer definitely because it will give us A=2, B=0 based on our guess 0521. We will clean the code set based on this rule.<br />
<p align="center"><img src="/image/remove1.jpg"></p>

### Which element need to be picked from the code set for the next play<br />
We give a graph explanation below. Please also refer to the paper ```Eﬃcient solutions for Mastermind using genetic algorithms``` page 8. The main idea is to minimize the code set after we pick an element from the code set. To reduce the checking time for the entire code set, we therefore randomly choose some elements (We implemented 100 as the max number of elements) as S to represent for the entire code set.<br />

We don't expect the chosen one for the next play to be the true answer, our goal is to minimize the number of code set elements after we pick the chosen one. We will examine through all the element in the code set. When we examine the first element (denotes as c), then we will randomly choose a set of elements (denotes as S) in the code set other than c. Each of the element in the S will acts as an answer (denotes as c*) and play against c and receives A, B value by using the function ```A, B = playresult(c*, c)```. We then receive other A, B value by using the function ```a, b = playresult(c**, c)``` where c** is the element in S other than c*. Only the c** with A=a, B=b can remain in S. The score of c is based on the average remaining number of the element in S.
<p align="center"><img src="/image/chooseone_function.jpg"></p>

### The algorithm and the program structure<br />
<p align="center"><img src="/image/structure_final.JPG"></p>

## 3. The Code and the explanation<br />
1. import library. "random" can generate random number. "itertools" can help us to loop through all the element in a list.<br />
<p align="center"><img src="/image/1.JPG"></p>

2. This is a function which will randomly return a sequence of 4 digit number without duplicate.<br />
<p align="center"><img src="/image/2.JPG"></p>

3. This is a function which will return value of **A** and **B**. The outer for loop will loop through all the digit in the code value(unknown and need to be guessed). The inner loop will loop through all the digit in the guess value. If the digit have the same position and value, A will plus 1. If the digit only have the same value with incorrcect position, B will plus 1. <br />
<p align="center"><img src="/image/3.JPG"></p>

4. This is a function which will generate all the combination of 4 digit number without duplicate number such as (1,2,3,4), (3,6,2,4), (5,8,9,1)....and so on.<br />
<p align="center"><img src="/image/4.JPG"></p>

5. This function helps us to choose the element in the code set to play in the next run. This sepecific element we choose should clean more elements in the code set. Please refer to the paper ```Eﬃcient solutions for Mastermind using genetic algorithms``` page 8. 
<p align="center"><img src="/image/chooseone_final.JPG"></p>

6. We use the function **```givenum```** to generate a sequence of code which need to be guessed by our program.<br />
<p align="center"><img src="/image/5.JPG"></p>

7. This is the main program. First, use the function **```ini_population```** to initialize the code set which store all the possible answer. Second, we use randomly guess. We then receive the A and B value when we use the guess to play against the real answer. This play will be counted in the number of play. We store the number of play in the variable "play_count". We will add up the "play_count" by one whenever we guess a value and play against the real answer (which also occurs in the while loop). The while loop will terminate until we obtain the correct answer where A=4 and B=0. <br />

The for loop in the while loop is to check whether we keep or remove the element from the code set. The element to be removed is the one which can not give us the same value of A and B based on our guess. After cleaning the code set, we pick up one element from the code set to act as the next guess. The picking method has already elaborated in the previous section. This guess will play against the true answer and receive A and B value. The while loop will end when we get the guess with A=4. Lastly, the program output the number of time we play to get the true answer.
<p align="center"><img src="/image/main_final.JPG"></p>

## 4. Result
After playing 1256 times, the average number of guessing is 5.14. The code is as the following.<br />

## 5. Reference 
NCCU(in Chinese): http://www.cs.nccu.edu.tw/~chaolin/papers/science3203.pdf  <br />
Genetic algorithms: https://www.sciencedirect.com/science/article/pii/S030505480800110X <br />
Optimal algorithms for mastermind and bulls-cows games: http://slovesnov.users.sourceforge.net/index.php?bullscows_tree,english,crushBullsCows <br />

