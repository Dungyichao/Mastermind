# Mastermind
## 1. About the game<br />
This game involves two persons(ex. Tom, Jack). Each of the player will think of a sequence of 4 digit number without duplicate such as 1234 or 4705. One of the player need to guess another player's answer. During the guessing process, Tom will guess a sequence of number and Jack will response the guessing with two number **A** and **B**.  A represents the number of digit with correct value as well as the correct position. B represents the number of digit with correct value but wrong position. Tom will give another guess based on the information of A and B and then Jack will give another A, B value as response. The guessing process will terminate untill Tom come up with the right answer of Jack.<br />
Example: If the real answer is 5032 and our guess is 4023. A = 1 because "0" is at the correct position and it is the right value. B = 2 because the anser contains digit "2" and digit "3" but they are at the incorrect position.
## 2. How we design the program<br />
We have a code set containing 5040 combination of 4 digit number without duplicate. We randomly give a sequence of number as the first guess and receive the response of A and B. Based on the value of A and B, we remove the element from the code set which is not going to be the correct answer. We then pick up an element from the code set for the next play and receive A and B value. We will keep guessing until we get A=4 and B=0 (it means we get 4 digit with correct position and value).<br />
### Which element need to be removed from the code set<br />

