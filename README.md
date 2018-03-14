# Mastermind
## 1. About the game<br />
This game involves two persons(ex. Tom, Jack). Each of the player will think of a sequence of 4 digit number without duplicate such as 1234 or 4705. One of the player need to guess another player's answer. During the guessing process, Tom will guess a sequence of number and Jack will response the guessing with two number **A** and **B**.  A represents the number of digit with correct value as well as the correct position. B represents the number of digit with correct value but wrong position. Tom will give another guess based on the information of A and B and then Jack will give another A, B value as response. The guessing process will terminate untill Tom come up with the right answer of Jack.<br />

Example: If the real answer is 5032 and our guess is 4023. A = 1 because "0" is at the correct position and it is the right value. B = 2 because the anser contains digit "2" and digit "3" but they are at the incorrect position.
## 2. How we design the program<br />
We have a code set containing 5040 combination of 4 digit number without duplicate. We randomly give a sequence of number as the first guess and receive the response of A and B. Based on the value of A and B, we remove the element from the code set which is not going to be the correct answer. We then pick up an element from the code set for the next play and receive A and B value. We will keep guessing until we get A=4 and B=0 (it means we get 4 digit with correct position and value).<br />
### Which element need to be removed from the code set<br />
In the original code set, there is 0123, 0124, 0125, 0126....... and so on. If our first guess is 0521 and receive A=2, B=1. 0123 can be the answer because it will give us the same A and B value, so we keep it in the code set. However 0124 will not be the answer definitely because it will give us A=2, B=0. We will clean the code set based on this rule.<br />

## 3. The Code and the explanation<br />
1. import library<br />
<p align="center"><img src="/image/1.JPG"></p>

2. This is a function which will randomly return a sequence of 4 digit number without duplicate.<br />
<p align="center"><img src="/image/2.JPG"></p>

3. This is a function which will return value of **A** and **B**. The outer for loop will loop through all the digit in the code value(unknown and need to be guessed). The inner loop will loop through all the digit in the guess value. If the digit have the same position and value, A will plus 1. If the digit only have the same value with incorrcect position, B will plus 1. <br />
<p align="center"><img src="/image/3.JPG"></p>

4. This is a function which will generate all the combination of 4 digit number without duplicate number such as (1,2,3,4), (3,6,2,4), (5,8,9,1)....and so on.<br />
<p align="center"><img src="/image/4.JPG"></p>

5. We use the function **```givenum```** to generate a sequence of code which need to be guessed by our program.<br />
<p align="center"><img src="/image/5.JPG"></p>

6. This is the main program. First, use the function **```ini_population```** to initialize the code set which store all the possible answer. Second, we randomly use a sequence of digit as our first guess <br />
<p align="center"><img src="/image/6.JPG"></p>

## 4. Result
