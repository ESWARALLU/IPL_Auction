from prettytable import PrettyTable

class Players:
    def __init__(self, id, n, nt, ct, rl, ba, bw, nm, r, w, bsp, sp):
        self.id = id
        self.name = n
        self.nationality = nt 
        self.country = ct
        self.role = rl
        self.batting_style = ba
        self.bowling_style = bw
        self.no_of_matches = nm
        self.runs = r
        self.wickets = w
        self.baseprice = bsp
        self.soldprice = sp


    

class Node:
    def __init__(self,da):
        self.data=da
        self.next=None
class List:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=newnode
    def print_all_details(self):
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Nationality", "Country", "Role", "Batting Style", "Bowling Style", "No. of Matches", "Runs", "Wickets", "Base Price", "Sold Price"]
        n = self.head
        while n:
            player = n.data
            table.add_row([player.id, player.name, player.nationality, player.country, player.role, player.batting_style, player.bowling_style, player.no_of_matches, player.runs, player.wickets, player.baseprice, player.soldprice])
            n = n.next
        print(table)
    def print_node(self,node):
        print(node.data.name,end=",")
        print(node.data.batting_style,end=",")
        print(node.data.bowling_style,end=",")
        print(node.data.runs,end=",")
        print(node.data.wickets,end=",")
        print(node.data.baseprice,end=",")
        print(node.data.soldprice)
    def print_by_name(self,name):
        n=self.head
        while n:
            if n.data.name==name:
                self.print_node(n)
            n=n.next
    def print_by_batting_style(self,batting_style):
        n=self.head
        while n:
            if n.data.batting_style==batting_style:
                self.print_node(n)
            n=n.next
    def print_by_bowling_style(self,bowling_style):
        n=self.head
        while n:
            if n.data.bowling_style==bowling_style:
                self.print_node(n)
            n=n.next
    def print_by_runs(self,runs):
        n=self.head
        while n:
            if n.data.runs==runs:
                self.print_node(n)
            n=n.next
    def insert_Players(self, id, n, nt, ct, rl, ba, bw, nm, r, w, bsp, sp):
        player = Players(id, n, nt, ct, rl, ba, bw, nm, r, w, bsp, sp)
        self.insert(player)



    
'''play=[]
play.append(Players('eswar',0,0,0,0,0))
play.append(Players('eswar',0,0,0,0,0))'''
nl=List()
nl.insert_Players('1', 'Joe Root', 'foreign', 'England', 'Batsman', 'Right-handed', 'Right-arm off-spin', '20', '520', '7', 5000, 0)
nl.insert_Players('2', 'Kane Williamson', 'foreign', 'New Zealand', 'Batsman', 'Right-handed', 'Right-arm off-spin', '25', '690', '12', 6000, 0)
nl.insert_Players('3', 'David Warner', 'foreign', 'Australia', 'Batsman', 'Left-handed', 'Right-arm leg-spin', '28', '820', '5', 7000, 0)
nl.insert_Players('4', 'AB de Villiers', 'foreign', 'South Africa', 'Batsman', 'Right-handed', 'Right-arm medium', '23', '960', '0', 8000, 0)
nl.insert_Players('5', 'Glenn Maxwell', 'foreign', 'Australia', 'All-Rounder', 'Right-handed', 'Right-arm off-spin', '21', '480', '9', 5500, 0)
nl.insert_Players('6', 'Rashid Khan', 'foreign', 'Afghanistan', 'All-Rounder', 'Right-handed', 'Right-arm leg-spin', '19', '220', '15', 4000, 0)
nl.insert_Players('7', 'Trent Boult', 'foreign', 'New Zealand', 'Bowler', 'Left-handed', 'Left-arm fast', '18', '0', '18', 4500, 0)
nl.insert_Players('8', 'Kagiso Rabada', 'foreign', 'South Africa', 'Bowler', 'Right-handed', 'Right-arm fast', '20', '0', '20', 5000, 0)
nl.insert_Players('9', 'Pat Cummins', 'foreign', 'Australia', 'Bowler', 'Right-handed', 'Right-arm fast', '25', '0', '25', 6000, 0)
nl.insert_Players('10', 'Steve Smith', 'foreign', 'Australia', 'Batsman', 'Right-handed', 'Right-arm leg-spin', '23', '720', '3', 6500, 0)
nl.insert_Players('11', 'Eoin Morgan', 'foreign', 'England', 'Batsman', 'Left-handed', 'Right-arm medium', '20', '840', '0', 7000, 0)
nl.insert_Players('12', 'Quinton de Kock', 'foreign', 'South Africa', 'Wicketkeeper', 'Left-handed', '', '19', '780', '0', 6000, 0)
nl.insert_Players('13', 'Chris Gayle', 'foreign', 'West Indies', 'Batsman', 'Left-handed', 'Right-arm off-spin', '28', '1020', '2', 7500, 0)
nl.insert_Players('14', 'Andre Russell', 'foreign', 'West Indies', 'All-Rounder', 'Right-handed', 'Right-arm fast', '21', '520', '12', 7000, 0)
nl.insert_Players('15', 'Sunil Narine', 'foreign', 'West Indies', 'All-Rounder', 'Left-handed', 'Right-arm off-spin', '25', '340', '15', 5500, 0)
nl.insert_Players('16', 'Ben Stokes', 'foreign', 'England', 'All-Rounder', 'Left-handed', 'Right-arm fast-medium', '22', '610', '8', 6500, 0)
nl.insert_Players('17', 'Rashid Khan', 'foreign', 'Afghanistan', 'Bowler', 'Right-handed', 'Right-arm leg-spin', '24', '260', '18', 5000, 0)
nl.insert_Players('18', 'Adil rashid', 'foreign', 'England', 'All-Rounder', 'Right-handed', 'Right-arm leg-spin', '27', '480', '10', 5500, 0)
nl.insert_Players('19', 'Faf du Plessis', 'foreign', 'South Africa', 'Batsman', 'Right-handed', 'Right-arm leg-spin', '22', '820', '2', 6000, 0)
nl.insert_Players('20', 'Shai hope', 'foreign', 'West Indies', 'Batsman', 'Right-handed', 'Right-arm off-spin', '26', '790', '0', 5500, 0)
nl.insert_Players('21', 'Jason Holder', 'foreign', 'West Indies', 'All-Rounder', 'Right-handed', 'Right-arm fast', '20', '430', '13', 6500, 0)
nl.insert_Players('22', 'Kagiso Rabada', 'foreign', 'South Africa', 'Bowler', 'Right-handed', 'Right-arm fast', '28', '0', '28', 7000, 0)
nl.insert_Players('23', 'Omarzai', 'foreign', 'Afghanistan', 'Bowler', 'Right-handed', 'Right-arm medium fast', '19', '290', '20', 5500, 0)
nl.insert_Players('24', 'Mitchell Starc', 'foreign', 'Australia', 'Bowler', 'Left-handed', 'Left-arm fast', '30', '0', '30', 7000, 0)
nl.insert_Players('25', 'Kieron Pollard', 'foreign', 'West Indies', 'All-Rounder', 'Right-handed', 'Right-arm medium-fast', '25', '560', '15', 6500, 0)
nl.insert_Players('26', 'Trent Boult', 'foreign', 'New Zealand', 'Bowler', 'Left-handed', 'Left-arm fast', '24', '0', '24', 5000, 0)
nl.insert_Players('27', 'Adam Zampa', 'foreign', 'Australia', 'Bowler', 'Right-handed', 'Right-arm leg-spin', '26', '0', '22', 6000, 0)
nl.insert_Players('28', 'Jonny Bairstow', 'foreign', 'England', 'Wicketkeeper', 'Right-handed', '', '27', '750', '0', 6000, 0)
nl.insert_Players('29', 'Nicholas Pooran', 'foreign', 'West Indies', 'Wicketkeeper', 'Left-handed', '', '20', '580', '0', 5500, 0)
nl.insert_Players('30', 'Virat Kohli', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm medium', '92', '7490', '4', 5000, 0)
nl.insert_Players('31', 'Rohit Sharma', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm off-spin', '108', '9205', '8', 6000, 0)
nl.insert_Players('32', 'Jasprit Bumrah', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm fast', '64', '145', '106', 7000, 0)
nl.insert_Players('33', 'Ravindra Jadeja', 'Indian', 'India', 'All-Rounder', 'Left-handed', 'Left-arm orthodox', '51', '1954', '220', 8000, 0)
nl.insert_Players('34', 'Bhuvneshwar Kumar', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm medium-fast', '61', '550', '118', 7500, 0)
nl.insert_Players('35', 'KL Rahul', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm medium', '38', '2006', '0', 6000, 0)
nl.insert_Players('36', 'Shikhar Dhawan', 'Indian', 'India', 'Batsman', 'Left-handed', 'Right-arm off-spin', '34', '2315', '2', 7000, 0)
nl.insert_Players('37', 'Hardik Pandya', 'Indian', 'India', 'All-Rounder', 'Right-handed', 'Right-arm fast-medium', '14', '532', '18', 5500, 0)
nl.insert_Players('38', 'Rishabh Pant', 'Indian', 'India', 'Wicketkeeper', 'Left-handed', '', '21', '754', '0', 6500, 0)
nl.insert_Players('39', 'Ravichandran Ashwin', 'Indian', 'India', 'All-Rounder', 'Right-handed', 'Right-arm off-spin', '78', '2552', '409', 7000, 0)
nl.insert_Players('40', 'Mohammed Shami', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '71', '116', '182', 6500, 0)
nl.insert_Players('41', 'Ishant Sharma', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '101', '371', '297', 6000, 0)
nl.insert_Players('42', 'Ajinkya Rahane', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm medium', '69', '4479', '0', 5500, 0)
nl.insert_Players('43', 'Cheteshwar Pujara', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm leg-spin', '86', '6267', '0', 6000, 0)
nl.insert_Players('44', 'Wriddhiman Saha', 'Indian', 'India', 'Wicketkeeper', 'Right-handed', '', '38', '1353', '0', 5500, 0)
nl.insert_Players('45', 'Umesh Yadav', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '48', '167', '148', 6500, 0)
nl.insert_Players('46', 'Yuzvendra Chahal', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm leg-spin', '56', '83', '92', 7000, 0)
nl.insert_Players('47', 'Kuldeep Yadav', 'Indian', 'India', 'Bowler', 'Left-handed', 'Left-arm chinaman', '21', '24', '42', 7500, 0)
nl.insert_Players('48', 'Washington Sundar', 'Indian', 'India', 'All-Rounder', 'Left-handed', 'Right-arm off-spin', '6', '110', '5', 5000, 0)
nl.insert_Players('49', 'Shardul Thakur', 'Indian', 'India', 'All-Rounder', 'Right-handed', 'Right-arm medium-fast', '14', '206', '34', 5500, 0)
nl.insert_Players('50', 'Shreyas Iyer', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm off-spin', '23', '813', '0', 6000, 0)
nl.insert_Players('51', 'Mayank Agarwal', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm off-spin', '14', '974', '0', 6500, 0)
nl.insert_Players('52', 'Suryakumar Yadav', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm medium', '5', '154', '0', 7000, 0)
nl.insert_Players('53', 'Deepak Chahar', 'Indian', 'India', 'Bowler', 'Right-handed', 'Right-arm medium-fast', '14', '54', '33', 6000, 0)
nl.insert_Players('54', 'Prithvi Shaw', 'Indian', 'India', 'Batsman', 'Right-handed', 'Right-arm off-spin', '5', '335', '0', 5500, 0)
nl.insert_Players('55', 'Axar Patel', 'Indian', 'India', 'All-Rounder', 'Left-handed', 'Left-arm orthodox', '12', '550', '27', 6500, 0)
nl.insert_Players('56', 'Sanju Samson', 'Indian', 'India', 'Wicketkeeper', 'Right-handed', '', '11', '326', '0', 7000, 0)
nl.insert_Players('57', 'Hardus Viljoen', 'foreign', 'South Africa', 'Bowler', 'Right-handed', 'Right-arm fast', '10', '15', '9', 6000, 0)
nl.insert_Players('58', 'Mohammad Nabi', 'foreign', 'Afghanistan', 'All-Rounder', 'Right-handed', 'Right-arm off-spin', '15', '255', '9', 7000, 0)
nl.insert_Players('59', 'Chris Lynn', 'foreign', 'Australia', 'Batsman', 'Right-handed', 'Right-arm off-spin', '4', '128', '0', 8000, 0)
nl.insert_Players('60', 'Nathan Coulter-Nile', 'foreign', 'Australia', 'All-Rounder', 'Right-handed', 'Right-arm fast-medium', '7', '92', '8', 7500, 0)
nl.insert_Players('61', 'Kusal Perera', 'foreign', 'Sri Lanka', 'Wicketkeeper', 'Left-handed', '', '10', '228', '0', 6000, 0)
nl.insert_Players('62', 'Dushmantha Chameera', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '4', '8', '5', 5500, 0)
nl.insert_Players('63', 'Lahiru Kumara', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm fast', '3', '2', '1', 5000, 0)
nl.insert_Players('64', 'Wanindu Hasaranga', 'foreign', 'Sri Lanka', 'All-Rounder', 'Right-handed', 'Right-arm leg-spin', '4', '33', '4', 4500, 0)
nl.insert_Players('65', 'Dasun Shanaka', 'foreign', 'Sri Lanka', 'All-Rounder', 'Right-handed', 'Right-arm medium-fast', '7', '79', '5', 4000, 0)
nl.insert_Players('66', 'Isuru Udana', 'foreign', 'Sri Lanka', 'All-Rounder', 'Right-handed', 'Left-arm medium-fast', '2', '16', '0', 3500, 0)
nl.insert_Players('67', 'Akila Dananjaya', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm off-spin', '1', '0', '1', 3000, 0)
nl.insert_Players('68', 'Dinesh Chandimal', 'foreign', 'Sri Lanka', 'Wicketkeeper', 'Right-handed', '', '3', '66', '0', 2500, 0)
nl.insert_Players('69', 'Suranga Lakmal', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '2', '1', '2', 2000, 0)
nl.insert_Players('70', 'Nuwan Pradeep', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '1', '0', '1', 1500, 0)
nl.insert_Players('71', 'Dhananjaya de Silva', 'foreign', 'Sri Lanka', 'All-Rounder', 'Right-handed', 'Right-arm off-spin', '1', '1', '0', 1000, 0)
nl.insert_Players('72', 'Minod Bhanuka', 'foreign', 'Sri Lanka', 'Wicketkeeper', 'Left-handed', '', '1', '0', '1', 500, 0)
nl.insert_Players('73', 'Dimuth Karunaratne', 'foreign', 'Sri Lanka', 'Batsman', 'Left-handed', 'Right-arm medium', '2', '15', '0', 400, 0)
nl.insert_Players('74', 'Pathum Nissanka', 'foreign', 'Sri Lanka', 'Batsman', 'Right-handed', 'Right-arm off-spin', '1', '34', '0', 300, 0)
nl.insert_Players('75', 'Ashen Bandara', 'foreign', 'Sri Lanka', 'Batsman', 'Right-handed', 'Right-arm off-spin', '1', '1', '0', 200, 0)
nl.insert_Players('76', 'Lahiru Madushanka', 'foreign', 'Sri Lanka', 'Bowler', 'Right-handed', 'Right-arm fast-medium', '1', '0', '1', 100, 0)
nl.insert_Players('77', 'Liam Livingstone', 'foreign', 'England', 'All-Rounder', 'Right-handed', 'Right-arm leg-spin', '3', '47', '1', 500, 0)
