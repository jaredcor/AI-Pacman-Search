"""
This file contains all of the search algrothms that you will have to impliment.

Please only change the parts of the file you are asked to.  Look for the lines
that say

"*** TTU CS3368 YOUR CODE HERE ***"

look for "*** TTU CS3368 READ THIS ***" if there is any 

The parts you fill in start about 3/4 of the way down.  Follow the project
description for details.

Good luck and happy searching!
"""

import util
from util import Stack


class DFS(object):
    def depthFirstSearch(self, problem):
        """
        Search the deepest nodes in the search tree first
        [2nd Edition: p 75, 3rd Edition: p 87]

        Your search algorithm needs to return a list of actions that reaches
        the goal.  Make sure to implement a graph search algorithm
        [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** TTU CS3368 READ THIS ***"
        """
        Remember that you will best strategy is to use a stack. you can import stack from util
        Remember to keep track of visited states
        here is a plan:
        (1) import stack
        (2) intiate you variable
        (3) get the start state/node
        (4) push start node and empty path to stack
        (5) initiate a visted node variable
        (6) while there is something on you stack
            6.1 get the state and path
            6.2 if goal return goal
            6.3 else if you did not visit the state
                6.3.1 pass though all seccessors
                you can get a successor using problem.getSuccessors("yournode")
                    push the sucessor to you statck
            6.4 add the node to visited nodes
                
        prints can always help you alot     
        """
        "*** TTU CS3368 YOU CODE GO HERE ***"
        fringe = Stack()
        

        util.raiseNotDefined()


class BFS(object):
    def breadthFirstSearch(self, problem):
        "*** TTU CS3368 READ CODE HERE ***"
        "Idea is Same as DFS But with Queue, which you Queue import from util"
        util.raiseNotDefined()


class UCS(object):
    def uniformCostSearch(self, problem):
        "*** TTU CS3368 READ CODE HERE ***"
        "This is a Priority Queue so how to push your things to a priority queue?"
        "How to keep track of costs in the priotity queue? how to choose based on priority?"
        util.raiseNotDefined()


class aSearch (object):
    def nullHeuristic(state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0

    def aStarSearch(self, problem, heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        "*** TTU CS3368 YOUR CODE HERE ***"
        "how to extend USC to A*"
        util.raiseNotDefined()
