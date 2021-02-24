# import libraries
import random
import heapq
import time


def availableActions(number_of_pancakes):
    """ Generate a list of available actions ( flips ) that agent can do

    Args:
        number_of_pancakes (int): number of pancakes that we want to order it

    Returns:
        list: available actions ( flips )
    """
    return list(range(2, number_of_pancakes+1))


def goalState(number_of_pancakes):
    """ Generate a goal state ( list ) what the goal state will be

    Args:
        number_of_pancakes (int): number of pancakes that we want to order it

    Returns:
        list: orderd sequence of pancakes from low to high
    """
    return list(range(1, number_of_pancakes+1))


def randomState(num_of_pancakes):
    """ Generate a random state as an initial state to start looking for the goal

    Args:
        num_of_pancakes (int): number of pancakes that we want to order it

    Returns:
        list: random sequence represent the order of pancakes at the start state
    """
    sequence = list(range(1, num_of_pancakes+1))
    random.shuffle(sequence)

    return sequence


class STATE:

    def __init__(self, sequence=[]):
        # Sequence of pancakes ( start state )
        self.Sequence = sequence

    def getSequence(self):
        """ Get the sequence of the current state

        Returns:
            list: current state ( order of the pancakes )
        """
        return self.Sequence

    def getLength(self):
        """ Compute the length of the sequence

        Returns:
            int: lenght of the sequence ( number of pancakes )
        """
        return len(self.Sequence)

    def isGoal(self, goal):
        """ Goal state checker ( check if the agent is in the goal state )

        Args:
            goal (list): goal state ( ordered sequence )

        Returns:
            bool: True if we are in the GOAL, otherwise False
        """
        if (self.Sequence == goal):
            return True
        else:
            return False

    def flip(self, action):
        """ Flip the the pancakes with specific action ( number of pancakes that we have to flip )

        Args:
            action (int): number of pancakes that agent should flip

        Raises:
            ValueError: agent can only flip 2 pancakes or more at the same time ( can't hold one pancake )

        Returns:
            list: new sequence after excute the action 
        """
        available_actions = availableActions(len(self.Sequence))
        flipped_state = []
        if action in available_actions:
            seq_cpy = self.Sequence[:action].copy()
            seq_cpy.reverse()
            flipped_state = seq_cpy + self.Sequence[action:]
        else:
            raise ValueError('Invalid action')

        return flipped_state

    def heuristic(self):
        """ Heuristic, to estimate what the cost it is to reach to the GOAL state, 
        HOW IT WORKS? : we estimate the remaining steps by count the pancakes which are not in the right sequence
        e.g. h([1, 3, 2 ,4]) = 2, because 3 and 2 weren't in the right order 

        Returns:
            int: estimated steps that we have to do to reach to the GOAL
        """
        goal = goalState(len(self.Sequence))
        count = 0
        for idx, i in enumerate(self.Sequence):
            if i is not goal[idx]:
                count += 1

        return count


class AGENT:

    def successor(self, sequence):
        """ Searching the optimal solution, expand the states with the least cost ( f(state) = g(state) + h(state) )
            and update the states and store the f(n) value and the states inside Priority Queue
        Args:
            sequence (obj): initial state ( start state )

        Returns:
            list: sequence of actions ( actions that we have to reach to the solution which is obtimal )
        """
        num_of_pancakes = sequence.getLength()
        goal = goalState(num_of_pancakes)

        # Check if we are in the 'GOAL' state, then return empry list ( there is no action/flips )
        if sequence.isGoal(goal):
            return []

        # Create priority queue to store values for ( h(state), g(state)/cost, expanded states )
        fringe = []

        available_actions = availableActions(num_of_pancakes)
        for action in available_actions:
            new_state = STATE(sequence.flip(action))
            if new_state.isGoal(goal):
                return [action]
            else:
                heapq.heappush(fringe,
                               (new_state.heuristic(),
                                [action],
                                new_state))

        while (len(fringe)-1) > 0:
            lowest_cost_path = heapq.heappop(fringe)
            current_state = lowest_cost_path[2]
            actions_sequence = lowest_cost_path[1]
            last_action = actions_sequence[-1]

            for action in available_actions:
                if (action != last_action):
                    new_state = STATE(current_state.flip(action))
                    if new_state.isGoal(goal):
                        return actions_sequence + [action]
                    else:
                        heapq.heappush(fringe,
                                       (new_state.heuristic(),
                                        actions_sequence + [action],
                                        new_state))

    def goalPath(self, sequence):
        """ Output the seqence of actions that we have to reach to the GOAL state 

        Args:
            sequence (obj): initial state ( start state )
        """
        start = time.time()
        goal_path = self.successor(sequence)
        print('-' * 25)
        print('Start State: ' + str(sequence.getSequence()))
        print('Goal State: ' + str(goalState(sequence.getLength())))
        print('-' * 25)
        if len(goal_path) <= 0:
            print('Already in the GOAL state')
        else:
            for action in goal_path:
                print("FLIP TOP: " + str(action))
        end = time.time()
        elapsed_time = (end - start)
        print('-' * 25)
        print('Done!    Elapsed Time = ' + str(elapsed_time.__round__(4)))


def main():
    # number_of_pancakes = int(input('ENTER NUMBER OF PANCAKES:'))
    state = STATE(randomState(4))
    agent = AGENT()
    agent.goalPath(state)


if __name__ == "__main__":
    main()
