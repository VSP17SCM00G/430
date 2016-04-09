import sys
class Jug():

    """This class contain jug capacity and how many water in this jug.  """

    def __init__(self, capacity, water):
        self.capacity = capacity
        self.water = water

    def pour(self, jug):
        """ pour water to another jug until that jug is fill.

        :jug: jug that receive water
        :returns: void

        """

        empty = jug.capacity - jug.water

        if empty>0:
            if empty <= self.water:
                jug.water = jug.capacity
                self.water = self.water - empty
            else:
                jug.water = jug.water + self.water
                self.water = 0

        pass

class Vertex(object):

    """Docstring for Vertex. Use this class to search in graph."""

    def __init__(self, parent, waterInJugs):
        self.parent = parent
        self.waterInJugs = waterInJugs


def getWater(jugs):
    """

    :jugs: jugs
    :returns: tuple for water distribution

    """

    waterInJugs = ()
    for each in jugs:
        waterInJugs += (each.water,)

    return waterInJugs

def setJugs(jugs, vertex):
    """ set jugs water to vertex condition
    :returns: void

    """
    for each in range(len(jugs)):
        jugs[each].water = vertex.waterInJugs[each]

def verifyVertexList(vertex, vertexList):
    """ verify whether new vertex has existed in list
    :returns: True or False

    """

    for each in vertexList:
        if vertex.waterInJugs == each.waterInJugs:
            return True

    return False

def getAdjacentVertex(jugs, vertex, grayVertexList, blackVertexList, target):
    """ get vertex every adjacent vertex

    :grayVertexList:
    :blackVertexList:
    :returns: target vertex

    """


    for i, pourJug in enumerate(jugs):
        for j, receiveJug in enumerate(jugs):
            if i == j:
                continue
            setJugs(jugs, vertex)
            pourJug.pour(receiveJug)
            newJugs = jugs[:]
            newJugs[i] = pourJug
            newJugs[j] = receiveJug
            waterInJugs = getWater(newJugs)
            newVertex = Vertex(vertex, waterInJugs)


            if verifyVertexList(newVertex, grayVertexList):
                continue
            elif verifyVertexList(newVertex, blackVertexList):
                continue
            else:
                grayVertexList.append(newVertex)
                if target in waterInJugs:
                    return newVertex

    return None

def printVertexPath(vertex):
    """ display how to get target amount of water
    :returns: void

    """
    print vertex.waterInJugs

    while 1:
        if vertex.parent == None:
            break
        vertex = vertex.parent
        print vertex.waterInJugs

    pass

jugNum = raw_input("Input the number of jugs.\n")

print("Input the capability of each jugs, final jug capability equal the total amount of water.\n")

jugNum = int(jugNum)

jugs = []

for i in range(jugNum):
    print"Input jug", i, "capability: "
    capacity = raw_input();
    jug = Jug(int(capacity), 0)
    jugs.append(jug)

jugs[jugNum - 1].water = jugs[jugNum - 1].capacity

target = raw_input("Input target amount of water:")
target = int(target)

blackVertexList = []
grayVertexList = []

waterInJugs = getWater(jugs)
vertex = Vertex(None, waterInJugs)
grayVertexList.append(vertex)

if target in waterInJugs:
    print waterInJugs
    sys.exit(0)

while 1:
    if len(grayVertexList) == 0:
        print "It's impossible to get target amount of water."
        break

    targetVertex = getAdjacentVertex(jugs, grayVertexList[0], grayVertexList, blackVertexList, target)

    """
    for each in blackVertexList:
        print "black: ", each.waterInJugs
    for each in grayVertexList:
        print "gray: ", each.waterInJugs
    #raw_input()
    """

    if targetVertex != None:
        printVertexPath(targetVertex)
        break

    blackVertexList.append(grayVertexList.pop(0)) # remove first gray element and added into black vertex list
