from copy import deepcopy


class Node:
  def __init__(self):
    self.state=[[],[],[]]
    self.nodeNumber=0
    self.status='idle'
    self.neighbours=[]
    self.parent=None
    self.children=[] #For BFS
    self.point=10

def move(st1,st2):
    s1=st1[:] #copiar lista a s1
    s2=st2[:] #copiar lista a s2
    
    if len(s1)>0:
        topDisc=s1[len(s1)-1]
        lastofS2=len(s2)-1
       
        if len(s2)==0 or s2[lastofS2]>topDisc:
            s2.append(topDisc)
            s1.pop()

            return s1,s2
        else:
            return None
    else:
        return None

def moveDisc(n):
    stacks=[]

    for x in range(0,3):
        for y in range(0,3):
            #print('x:',x,'y:',y)
            stacks=move(n.state[x],n.state[y])

            if stacks!=None:
                # print 'states after move', states
                nextnode=Node()
                nextnode=deepcopy(n)
                nextnode.state[x]=deepcopy(stacks[0])
                nextnode.state[y]=deepcopy(stacks[1])

                # print 'states', states
                # print '\n'
                # print 'next node',nextnode.state
                if nextnode.state  in states:
                    #print 'nextnode in states'
                    a=1#dumb value
                else:
                    nodenumber=nextnode.nodeNumber
                    # print nextnode.state, 'next not in states'
                    states.append(nextnode.state)
                    return nextnode
    #print 'DEAD END'
    return None

def printPath(node):
    print ('Tracing back the Path')
    while True:
        print ('Node number: ', node.nodeNumber,'  State:  ', node.state)
        if node.parent!=None:
            node=node.parent
        else:
            break

def dfs(node):
    global targetFound
    global nodenumber
    if targetFound==False:
        node.status='ongoing'
        parent=deepcopy(node)
        node=moveDisc(node)
        print('node:',node)
        if node!=None:
            nodenumber+=1
            node.nodeNumber=nodenumber
            node.parent=parent
            #print ('Node ',node.nodeNumber, node.state,'\n')
            if node.state==finalState:
                #print ('Final target reached')
                printPath(node)
                targetFound=True

            dfs(node)
        else:
            #print 'node is None'
            parent.status='done'
            node=parent.parent
            #print ('moving back to Node',node.nodeNumber,'State',node.state)
            dfs(node)
    else:
        #print 'Target found'
        return False

def readStartState(numDisk):
    state=[]
    
    torre1 = [int(x) for x in range(numDisk, 0, -1)]
    state.append(torre1)
    torre2 = []
    state.append(torre2)
    torre3 = []
    state.append(torre3)

    return state

def readFinalState(numDisk):
    state=[]

    torre1 = []
    state.append(torre1)
    torre2 = []
    state.append(torre2)
    torre3 = [int(x) for x in range(numDisk, 0, -1)]
    state.append(torre3)

    return state

print('\nTorre de Hanoi com algoritmo DFS - Depth First Seach (Busca em Profundidade)')

numDisk = int(input('\nInforme a quantidade de discos: '))

initialState=readStartState(numDisk)
finalState = readFinalState(numDisk)

print ('\nInitial state : ',initialState)
print ('Final state : ',finalState)

states=[]
states=[initialState]
nodenumber=1
time=1
targetFound=False

node=Node()
node.state=initialState
node.nodeNumber=nodenumber
parentList=[node]
childList=[]
targetFound=False
largestInTarget=False

step=1

parentList=[node]
childList=[]

dfs(node)