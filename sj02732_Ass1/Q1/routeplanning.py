import search
import random
import util
class RoutePlanning(search.SearchProblem):
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """
    def __init__(self,start,end):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.current=self.start=start
        self.end=end

    def getStartState(self):
        return self.start

    def isGoalState(self,state):
        if state==self.end:
            return True
        return False

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        words=[]
        connections=[]
        with open("Connections.csv", "r") as f:
            data = f.readlines()
        for line in data:
            words=words+[[x.strip("\n") for x in line.split(',')]]
        lst=words.pop(0)
        for a in words:
            legal=False
            if (state == a[0]):
                for i in range(1,len(a)):
                        if(int(a[i])>0):
                            connections.append((lst[i],lst[i],int(a[i])))
                            legal=True
            if(legal==True):
                break
        return connections


    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        curr=self.current
        cost=0
        for action in actions:
            succ = self.getSuccessors(curr)
            for b in succ:
                if(action==b[0]):
                    curr=b[0]
                    cost+=int(b[1])
                    break
        return cost


    def getHeuristic(self,state):
        words = []
        heuristic=0
        with open("heuristics.csv", "r") as f:
            data = f.readlines()
        for line in data:
            words=words+[[x.strip("\n") for x in line.split(',')]]
        lst=words.pop(0)
        for a in words:
            legal=False
            if (state == a[0]):
                for i in range(1,len(a)):
                    if (int(a[i]) > 0)&(self.isGoalState(lst[i])):
                        heuristic=int(a[i])
                        legal=True
                        break
            if(legal==True):
                break
        return heuristic

problem = RoutePlanning("Islamabad","Skardu")
path = search.aStarSearch(problem)
print('Search found a path of %d moves: ' % (len(path)-1))
print(path)