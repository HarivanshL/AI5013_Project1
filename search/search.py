# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    closed = set() #stores the nodes that we have seen
    fringe = util.Stack() #stores the current node that has the state and moves that led up to it
    node = (problem.getStartState(), []) #creates start node
    fringe.push(node) #push start node onto stack

    #Performs DFS
    while(True):

        #If stack is empty then failed
        if fringe.isEmpty():
            return []
        
        #Extracts information from the current node
        state, moves = fringe.pop()

        #Found goal and returns list of moves
        if problem.isGoalState(state):
            return moves

        #Explores new node
        if state not in closed:
            #Adds to explored node list
            closed.add(state)
            
            #Grabs succesors of current node
            succesors = problem.getSuccessors(state)
            #Stores variation of move list
            temp = []

            #Iterates over succesors
            for child_state, choice, cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                if child_state not in closed:

                    # I think it just fine to add the choice to moves list
                    # Just like ['South', 'South', 'North', 'South', 'East', ..., 'West']
                    temp = moves + [choice]
                    
                    #Adds new node to stack
                    fringe.push((child_state, temp))


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set() #stores the nodes that we have seen
    fringe = util.Queue() #stores the current node that has the state and moves that led up to it
    node = (problem.getStartState(), []) #creates start node
    fringe.push(node) #push start node into queue

    #Performs DFS
    while(True):

        #If stack is empty then failed
        if fringe.isEmpty():
            return []
        
        #Extracts information from the current node
        state, moves = fringe.pop()

        #Found goal and returns list of moves
        if problem.isGoalState(state):
            return moves

        #Explores new node
        if state not in closed:
            #Adds to explored node list
            closed.add(state)
            
            #Grabs succesors of current node
            succesors = problem.getSuccessors(state)
            #Stores variation of move list
            temp = []

            #Iterates over succesors
            for child_state, choice, cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                if child_state not in closed:

                    temp = moves + [choice]
                    
                    #Adds new node to stack
                    fringe.push((child_state, temp))


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = set() #stores the nodes that we have seen
    fringe = util.PriorityQueue() #stores the current node that has the state and moves that led up to it along with cost
    node = (problem.getStartState(), [], 0) #creates start node with cost
    fringe.push(node, 0) #push start node and cost into priority queue

    fringe_states = {problem.getStartState(): 0} # dictionary for tracking the cost of nodes in fringe

    #Performs DFS
    while(True):

        #If stack is empty then failed
        if fringe.isEmpty():
            return []
        
        #Extracts information from the current node
        state, moves, cost= fringe.pop()

        #Found goal and returns list of moves
        if problem.isGoalState(state):
            print(f"Cost: {cost}")
            return moves

        #Explores new node
        if state not in closed:
            #Adds to explored node list
            closed.add(state)
            
            #Grabs succesors of current node
            succesors = problem.getSuccessors(state)
        
            #NEED TO ADD COST with path

            #Iterates over succesors
            for child_state, choice, step_cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                temp_move = moves + [choice]
                temp_cost = cost + step_cost
                
                if child_state not in closed and child_state not in fringe_states:
                    # if child state is not in closed and not in fringe, adds new node to queue
                    fringe.push((child_state, temp_move, temp_cost), temp_cost)
                    fringe_states[child_state] = temp_cost

                elif child_state in fringe_states and temp_cost < fringe_states[child_state]:
                    # if child state is in fringe and new cost is smaller, updates the cost to new one
                    fringe.update((child_state, temp_move, temp_cost), temp_cost)
                    fringe_states[child_state] = temp_cost


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    closed = set() #stores the nodes that we have seen
    fringe = util.PriorityQueue() #stores the current node that has the state and moves that led up to it along with cost and heuristic
    start_state = problem.getStartState()
    node = (start_state, [], 0) #creates start node + node contains cost
    print(heuristic(start_state, problem))
    fringe.push(node, heuristic(start_state, problem))  #push start node and heuristic into priority queue
                                                        # use heuristic as priority

    fringe_states = {start_state: 0} # dictionary for checking states in fringe and their cost

    #Performs A*
    while(True):

        #If priority queue is empty then failed
        if fringe.isEmpty():
            return []
        
        #Extracts information from the current node
        state, moves, cost = fringe.pop()

        #Found goal and returns list of moves
        if problem.isGoalState(state):
            return moves

        #Explores new node
        if state not in closed:
            #Adds to explored node list
            closed.add(state)
            
            #Grabs succesors of current node
            succesors = problem.getSuccessors(state)

            #NEED TO ADD COST with path

            #Iterates over succesors
            for child_state, choice, step_cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                temp_move = moves + [choice]
                temp_cost = cost + step_cost
                priority = temp_cost + heuristic(child_state, problem)
                
                if child_state not in closed and child_state not in fringe_states:

                    #Adds new node to priority queue
                    fringe.push((child_state, temp_move, temp_cost), priority=priority)
                    # add new status
                    fringe_states[child_state] = temp_cost
                
                elif child_state in fringe_states and temp_cost < fringe_states[child_state]:
                    fringe.update((child_state, temp_move, temp_cost), priority=priority)
                    # update the status
                    fringe_states[child_state] = temp_cost


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch