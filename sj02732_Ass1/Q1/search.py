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
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        util.raiseNotDefined()


def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """
    visited=frontier=[]
    visited.append((start,action,0))
    reached=False
    cost=0
    while(reached!=True):
        frontier+=problem.getSuccessors(start)
        smallest=frontier[0][2]+cost+problem.getHeuristic(frontier[0][0])
        small=0
        for i in range(len(frontier)):
            if (frontier[i][2]+cost+problem.getHeuristic(frontier[i][0])) <smallest:
                smallest=frontier[i][2]+problem.getHeuristic(frontier[i][0])
                small=i
        visited.append(frontier.pop(small))
        actions.append(visited[-1][1])
        cost=problem.getCostofActions(actions)
        start=visited[-1][0]
        if (problem.isGoalState(start)==True) or(len(frontier)==0):
            reached=True
    return visited
    """
    start = problem.getStartState()
    parent = util.Counter()
    cost = util.Counter()
    frontier=util.PriorityQueue()
    frontier.push(start,0)
    parent[start]=None
    cost[start]=0
    path=[]
    while frontier.isEmpty()!=True:
        current=frontier.pop()
        if problem.isGoalState(current)==True:
            while current:
                path=[current]+path
                stop = current
                current= parent[current]
                del parent[stop]
            break
        lst=problem.getSuccessors(current)
        i=0
        while i<len(lst):
            cost_new=cost[current]+lst[i][2]
            if (lst[i][0] not in cost) or cost_new<cost[lst[i][0]]:
                cost[lst[i][0]]=cost_new
                pri=cost_new+problem.getHeuristic(lst[i][0])
                frontier.push(lst[i][0],pri)
                parent[lst[i][0]]=current
            i+=1
    return path
"""
IMPORTANT!
Please Note the references:
Referenced from:
A* search problem: https://www.redblobgames.com/pathfinding/a-star/implementation.html
"""