# Part A.5

## 1. What were your results from compare_cow_transport_algorithms? Which algorithm runs faster? Why?
According to the results from compare_cow_transport_algorithms, greedy_cow_transport took 0.0001251697540283203 seconds and brute_force_cow_transport took 2.5066111087799072 seconds. This means that greedy_cow_transport runs faster, which is likely due to the fact that it does not have to iterate over every possible combination of cows that could be transported in order to find the optimal solution. In other words, greedy_cow_transport simply returns **a solution**, but not necessarily the _best overall solution_.

## 2. Does the greedy algorithm return the optimal solution? Why/why not?
greedy_cow_transport does _not_ return the optimal solution. As you can see in the code, this algorithm simply returns a combination of trips to transport all the cows without exceeding the weight limit in any single trip. However, there is no component in this algorithm to optimize for the number of trips; rather, we simply search for a combination of trips that could work without considering how many times the spaceship will have to go back and forth.

## 3. Does the brute force algorithm return the optimal solution? Why/why not?
brute_force_cow_transport _does_ return the optimal solution because it iterates over all the possible combinations of trips and chooses the one that not only stays within the weight limit for each individual trip, but also minimizes the number of trips overall.

# Part B.2

## 1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there were 30 different egg weights. You do not need to implement a brute force algorithm in order to answer this.
A brute force algorithm would require enumerating all possible combinations of 30 different egg weights before removing the combinations whose total weight exceeds the allowed weight, then choosing the solution with the fewest number of eggs from the remaining combinations. This would significantly increase the run time of this algorithm, making it a difficult approach to use.

## 2. If you were to implement a greedy algorithm for finding the minimum number of eggs needed, what would the objective function be? What would the constraints be? What strategy would your greedy algorithm follow to pick which eggs to take? You do not need to implement a greedy algorithm in order to answer this.
In order to solve this problem with a greedy algorith, the objective function would be to minimize the number of eggs needed. The constraints would be the maximum weight. In terms of strategy, my greedy algorithm would start by putting the heaviest possible egg onto the ship and then continuing to do so until the total weight equals the maximum weight.

## 3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is optimal or give an example of when it will not return the optimal solution. Again, you do not need to implement a greedy algorithm in order to answer this.
No, a greedy algorithm will not always return the optimal solution to this problem. Any set without an egg of weight 1 will cause the algorithm to fail because it will not find a solution that equals the maximum allowable weight. For example, if egg_weights = (5, 10, 25) and target_weight = 99, this algorithm would output 5 eggs (25 x 3 + 10 x 2 = 95) and leave 4 pounds of the maximum weight unused.
