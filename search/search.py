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

    #Grabs the directions for the game
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST  
    n = Directions.NORTH
    e = Directions.EAST  

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

    #Grabs the directions for the game
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST  
    n = Directions.NORTH
    e = Directions.EAST  

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

                    #Converts the direction to a move
                    if choice == 'South':
                        temp = moves +[s]
                    if choice == 'North':
                        temp = moves +[n]
                    if choice == 'West':
                        temp = moves +[w]
                    if choice == 'East':
                        temp = moves +[e]
                    
                    #Adds new node to stack
                    fringe.push((child_state, temp))


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = set() #stores the nodes that we have seen
    fringe = util.PriorityQueue() #stores the current node that has the state and moves that led up to it along with cost
    node = (problem.getStartState(), []) #creates start node
    fringe.push(node, 0) #push start node and cost into priority queue

    #Grabs the directions for the game
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST  
    n = Directions.NORTH
    e = Directions.EAST  

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


            #NEED TO ADD COST with path

            #Iterates over succesors
            for child_state, choice, cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                    #Converts the direction to a move
                if choice == 'South':
                    temp = moves +[s]
                if choice == 'North':
                    temp = moves +[n]
                if choice == 'West':
                    temp = moves +[w]
                if choice == 'East':
                    temp = moves +[e]
                
                if child_state not in closed:

                    #Adds new node to stack
                    fringe.push((child_state, temp), cost)
                else:
                    fringe.update((child_state, temp), cost)


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
    fringe = util.PriorityQueueWithFunction(heuristic) #stores the current node that has the state and moves that led up to it along with cost and heuristic
    node = (problem.getStartState(), []) #creates start node
    print(heuristic(problem.getStartState(), problem, []))
    fringe.push((problem.getStartState(), problem)) #push start node and cost into priority queue

    #Grabs the directions for the game
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST  
    n = Directions.NORTH
    e = Directions.EAST  

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


            #NEED TO ADD COST with path

            #Iterates over succesors
            for child_state, choice, cost in succesors:

                #Ensures we dont push already explored child nodes onto the stack
                    #Converts the direction to a move
                if choice == 'South':
                    temp = moves +[s]
                if choice == 'North':
                    temp = moves +[n]
                if choice == 'West':
                    temp = moves +[w]
                if choice == 'East':
                    temp = moves +[e]
                
                if child_state not in closed:

                    #Adds new node to stack
                    fringe.push((child_state, temp))
                else:
                    fringe.push((child_state, temp))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch