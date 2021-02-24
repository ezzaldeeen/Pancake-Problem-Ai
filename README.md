# Pancacke Problem in AI
 ### MAIN IDEA: We have random sequence of pancakes that we want to order form low to high using A* algorithm.

 * **First**: A* algo. must contain Heuristic function this will estimate the steps left that we have to do to reach the goal, Because A* algo. is ( Informd Search Algorithm ). Heruristic function must be admissible and consistant, How we could figure out that?
 
    > Our Heuristic fun. makes estimation based on the number of pancakes that are not in the right place. It is admissible Because that method gives us a number that is lower than the actual cost.

 * **Second**: We must know how A* algo. works. 
    * it checks the "STATE" if it was GOAL state or not.
    * Expand the least cost state ( Backward cost + Forward cost)
    * Store actions ( sequence of actions ) that hold us to the goal
    * We store the **Backward** cost, **Forward** cost, **New State** inside **priority Queue**

* **Third**: How Priority Queue does work?

    ```python
    import heapq
    fringe = [] # create new empty list
    heapq.heappush(fringe, # --> priority queue
     ( new_state.heuristic(), # --> estimation
      actions_sequence + [action], # --> flips ( actions )
      new_state )) # --> new state after excute that action
    ```

    ### Example: Fringe

    | Heuristic     | Actions( cost )   | New State  |
    | ------------- |:-------------:| -----:|
    | 3     | [2, 3] | [2, 1, 3, 4] |
    | 2     | [4, 2]      |   [3, 2, 1, 4] |
    | **0**     | **[2,3,3]**     |    **[1, 2, 3, 4]** |

    ```python
    heapq.heappop(fringe)
    ```

    At this case **Fringe** will pop least cost path which is:
    **[1, 2, 3, 4]**, Priority Queue sum the items
    For example: the bold row ( last item ) = 0 + 2 + 3 + 3 + ~~state~~ ( all state has the same sum ), then the fringe will choose the lowest one.
    

