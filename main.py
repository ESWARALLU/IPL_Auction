from prettytable import PrettyTable
from players import nl
from teams import teams
from stack import priceStack

#nl.head.data.name='kaushik'
n1=nl.head
#print(nl.head.data.name)
#print(nl.head.next.data.name)
d={'Bowler':0,'Batsman':1,'All-Rounde1r':2}

nl.print_by_name('eswar')
def findteam(t):
    for i in range(len(teams)):
        if t==teams[i].root.data:
            return teams[i]
    return" Team Not Found"
def getplayer():
    global n1 
    if n1 is nl.head:
        player = n1
        n1=n1.next
        return player
    elif n1 is not None:
        player = n1
        n1=n1.next
        return player
    elif n1 is None:
        return n1
while True:
    print("\nWelcome to IPL Auction 2024")
    print("1. View all players")
    print("2. View a team's player list")
    print("3. Start bidding")
    print("4. View unsold players")
    print("5. Exit")
    ch=int(input())
    if(ch==1):
        nl.print_all_details()
    elif ch==2:
        t=input("ENTER TEAM NAME").upper()
        for i in range(len(teams)):
            if t==teams[i].root.data:
                print("BOWLERS")
                teams[i].root.child[0].data1.display()
                print("NO OF PLAYERS",teams[i].root.child[0].data1.sz)
                print("BATTERS")
                teams[i].root.child[1].data1.display()
                print("NO OF PLAYERS",teams[i].root.child[1].data1.sz)
                print("ALLROUNDERS")
                teams[i].root.child[2].data1.display()
                print("NO OF PLAYERS",teams[i].root.child[1].data1.sz)
                break
    elif ch==3:
        player=getplayer()
        if player is not None:
            playername=player.data.name
            role=player.data.role
            bsp=player.data.baseprice
            nationality=player.data.nationality
            print(playername)
            print(player.data.role)
            print('base price',bsp)
            bch=input("enter x to skip player or to continue with the press any key")
            if bch!='x':
                while True:
                    t=input("ENTER TEAM NAME:").upper()
                    team=findteam(t)
                    vaild=team.biddingcheck(bsp,nationality)
                    if(priceStack.top is None):
                        if vaild:
                            price=bsp
                            priceStack.push(team,bsp)
                            con=input("If no one wants bid express n")
                            if(con=='n'):
                                team.root.child[d[role]].data1.insert(player.data.name,nationality)
                                team.budget-=priceStack.top.price
                                if nationality=='foreign':
                                    team.foriegnplayers+=1
                                else:
                                    team.indianplayers+=1
                                priceStack.deletestack()
                                break
                    else:
                        price=int(input("enter bid amount"))
                        if vaild and priceStack.top.price < price and priceStack.top.team!=team:
                            priceStack.push(team,price)
                            con=input("If no one wants bid express n")
                            if(con=='n'):
                                team.root.child[d[role]].data1.insert(playername,nationality)
                                priceStack.deletestack()
                                break
                        else:
                            print("enter vaild price")
                            

            else:
                player.data.soldprice=-1          
                        
                        
        else:
            print("REACHED TO END OF PLAYERS")

    



    elif ch==4:
        n2=nl.head
        while n2 is not None:
            if n2.data.soldprice ==-1:
                print(n2.data.name)
            n2=n2.next
    elif ch==5:
        break

        


        