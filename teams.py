class Node:
    def __init__(self, da, am) -> None:
        self.data = da
        self.amount = am
        self.data1 = Linklist()
        self.child = []
class teamplayer:
    def __init__(self,name,country) -> None:
        self.name=name
        self.country=country
        self.next=None
class Linklist:
    def __init__(self) -> None:
        self.head=None
        self.sz=0
    def insert(self,name,country):
        newnode=teamplayer(name,country)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.sz+=1
    def display(self):
        if self.head is None:
            print("No Players")
        else:
            n=self.head
            while n:
                print(n.name,n.country)
                n=n.next
class Teams:
    def __init__(self) -> None:
        self.root = None
        self.budget =20000
        self.foriegnplayers=0
        self.indianplayers=0
        self.sz=self.foriegnplayers+self.indianplayers
    def biddingcheck(self,bsp,nationality):
        a=self.budget
        if a-bsp>0:
            if self.sz<=15 and nationality=='foreign'and self.foriegnplayers<4:
                return True
            elif self.sz<=15 and nationality=='foreign'and self.foriegnplayers==4:
                print("exceeding foreingn player limit")
                return False
            elif self.sz<=15 and nationality=='Indian':
                return True
        else:
            print("excedding budget")
            return False

    

RCB = Teams()
RCB.root = Node('RCB', 600)
RCB.root.child.append(Node('bowlers', 0))
RCB.root.child.append(Node('batter', 0))
RCB.root.child.append(Node('allrounder', 0))
CSK=Teams()
CSK.root=Node("CSK",0)
CSK.root.child.append(Node('bowlers', 0))
CSK.root.child.append(Node('batter', 0))
CSK.root.child.append(Node('allrounder', 0))
SRH=Teams()
SRH.root=Node("SRH",0)
SRH.root.child.append(Node('bowlers', 0))
SRH.root.child.append(Node('batter', 0))
SRH.root.child.append(Node('allrounder',0))
MI=Teams()
MI.root=Node('MI',0)
MI.root.child.append(Node('bowlers', 0))
MI.root.child.append(Node('batter', 0))
MI.root.child.append(Node('allrounder', 0))
teams=[]
teams.append(RCB)
teams.append(CSK)
teams.append(SRH)
teams.append(MI)

