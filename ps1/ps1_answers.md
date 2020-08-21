# Problem A.5: Writeup

## 1. What were your results from compare_cow_transport_algorithms? Which algorithm runs faster? Why?
According to the results from compare_cow_transport_algorithms, greedy_cow_transport took 0.0001251697540283203 seconds and brute_force_cow_transport took 2.5066111087799072 seconds. This means that greedy_cow_transport runs faster, which is likely due to the fact that it does not have to iterate over every possible combination of cows that could be transported in order to find the optimal solution. In other words, greedy_cow_transport simply returns **a solution**, but not necessarily the _best overall solution_.

## 2. Does the greedy algorithm return the optimal solution? Why/why not?
greedy_cow_transport does _not_ return the optimal solution. As you can see in the code, this algorithm simply returns a combination of trips to transport all the cows without exceeding the weight limit in any single trip. However, there is no component in this algorithm to optimize for the number of trips; rather, we simply search for a combination of trips that could work without considering how many times the spaceship will have to go back and forth.

## 3. Does the brute force algorithm return the optimal solution? Why/why not?
brute_force_cow_transport _does_ return the optimal solution because it iterates over all the possible combinations of trips and chooses the one that not only stays within the weight limit for each individual trip, but also minimizes the number of trips overall.
