# shortest-route-genetic-algorithm
Implementation of a genetic algorithm that minimizes the total distance a route takes. 

I created this program to aid in my student job at the library. I pull and reshelve boxes of archived materials from my institution's huge library (100,000+ books).

My task is constrained by:
  1. The size of my cart (Holds 24 boxes)
  2. The number and layout of the shelves (4 tall rows, 42 subshelves each) - this is only a subset of the shelves holding archive materials that I'm allowed to touch.
I wanted to optimize the route I took.
This program returns the optimal route to take after 10 generations of a genetic algorithm that calculates the Manhattan Distance (distance in terms of grid-based moves like up/down or left/right). While Dijkstra's algorithm might (as in this implementation only returns an approximately optimal solution, where as the Dijkstra's algorithm would guarantee an exact path) be more effective, my task isn't performance critical and any optimization would sufface. I mainly wanted to explore my interest in genetic algorithms.

One feature I'm proud of is the use of lambda functions in the select_parents function. This was a huge improvement over my initial approach, which created another list for the tournament using the t_distance function and using that to select the parents.


