# Prisoner Dilemma
# 23 Prisoners
# 2 Switches
# Never see eachother
import sys
from random import randint
from statistics import mean

class Prisoner():
    def __init__(self, number, leader, visits, counted):
        self.number = number
        self.leader = leader
        self.visits = visits
        self.counted = counted

def create_prisoner(num):
    p = Prisoner(num, False, 0, False)
    return p

def run():
    prisoners = []
    counted = 0
    leftButton = False
    rightButton = False

    #print("Creating 23 prisoners...")
    try:
        for num in range(23):
            p = create_prisoner(num)
            prisoners.append(p)
    except:
        #print("Failed creating prisoners")
        return 1
    
    #print("Setting first prisoner as leader...")
    try:
        prisoners[0].leader = True
        prisoners[0].counted = True
    except:
        #print("Failed to set prisoner as leader")
        return 2

    while (counted < 22):
        selection = randint(0, 22)
        selected = prisoners[selection]
        selected.visits += 1

        if(selected.leader):
            #print("Leader selected")
            if(leftButton):
                #print("Left switch True. Adding to count ({}).".format(counted))
                leftButton = False
                counted += 1
            else:
                #print("Left switch False. Flipping right switch.")
                rightButton = not rightButton
        else:
            #print("Leader NOT selected")
            if(leftButton == False and selected.counted == False):
                #print("Left switch False. Flipping to True.")
                leftButton = True
                selected.counted = True
            else:
                #print("Left switch is True. Flipping right switch.")
                rightButton = not rightButton

    allVisits = 0
    #mostPrisoner = None
    #print("All prisoners accounted for")
    for p in prisoners:
    #    print("Prisoner #{} visited {} ({})".format(p.number, p.visits, p.counted))
        allVisits += p.visits

    #print("Summary:")
    #print("Number of days: {}".format(allVisits))
    #print("Most visits: Prisoner #{} visited {} times".format(mostPrisoner.number, mostPrisoner.visits))
    #print(allVisits)
    return allVisits

def main():
    days = []
    for _ in range(1000):
        days.append(run())

    high = max(days)
    avg = mean(days)
    low = min(days)
    
    print("Highest: {}".format(high))
    print("Average: {}".format(round(avg)))
    print("Lowest: {}".format(low))


if __name__ == "__main__":
    sys.exit(main())
