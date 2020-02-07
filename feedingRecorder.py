import os, sys
import datetime

totalAmount = [0] * 6 ## 0 for breastfeeding time, 1 for breastfeeding amount, 2 for formula amount, 3 for total amount, 4 for pee amount, 5 for poop amount per day.
recordDate = datetime.date.today().strftime("%Y-%m-%d")

def checkDate():
    global recordDate
    if recordDate != datetime.date.today().strftime("%Y-%m-%d"):
        recordDate = datetime.date.today().strftime("%Y-&m-%d")
        return False
    return True

def recordSummary():
    global recordDate
    global totalAmount
    if not checkDate():
        summaryMsg = """
                    --------------------------------
                    |             Name|      Amount|
                    |             Date|      {date}|
                    |breastFeedingTime|      {time}|
                    |    breastFeeding|  {bfamount}|
                    |    formulaAmount|   {famount}|
                    |            Total|     {total}|
                    |        pee times|       {pee}|
                    |       poop times|      {poop}|
                    --------------------------------
                     """.format(date=recordDate, time=totalAmount[0], bfamount=totalAmount[1], famount=totalAmount[2], total=totalAmount[3], pee=totalAmount[4], poop=totalAmount[5])
        print summaryMsg
        totalAmount = [0] * 6
        return summaryMsg
    return None


def checkBabystatsLog():
    try:
        os.stat('babystats.log')
        open('babystats.log', 'a')
    except:
        open('babystats.log', "w")

def getDates():
    dates = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dates

def generateMsg(ops):
    dates = getDates()
    msg = None
    summaryMsg = recordSummary()
    global totalAmount
    if(ops == 1):
        breastfeeding = input("what is the  amount of the breastfeeding milk this time? \n")
        breastfeedingTime = input("how long have you fed your baby (min) ? \n")
        formula = input("what is the amount of the formula this time? \n")
        total = formula + breastfeeding
        totalAmount[0] += breastfeedingTime
        totalAmount[1] += breastfeeding
        totalAmount[2] += formula
        totalAmount[3] += total
        msg = "{date}: baby is fed: breastfeeding: {breastfeeding} oz; formula: {formula} oz; total: {total} oz; breastfeeding(time): {time} mins \n".format(date = dates, breastfeeding=breastfeeding, formula=formula, total=total, time=breastfeedingTime)
    if(ops == 2):
        totalAmount[4] += 1
        msg = "{date}: baby pees. \n".format(date = dates)
    if(ops == 3):
        totalAmount[5] += 1
        msg = "{date}: baby poops. \n".format(date = dates)
    if(ops == 4):
        done = input("what happened to baby?\n")
        msg = "{date}: {done}\n".format(date=dates, done=done)
    if msg != None:
        return msg, summaryMsg

def recorder(ops):
    checkBabystatsLog();
    msg, summaryMsg = generateMsg(ops)
    print(msg)
    if(ops == 5):
        f = open("babystats.log")
        lines = f.readlines()
        lines = lines[:-1]
        f.close()
        f = open("babystats.log", 'w')
        f.writelines([line for line in lines])
        f.close()
        return
    f = open('babystats.log', 'a')
    if summaryMsg:
        f.write(summaryMsg)
    f.write(msg)
    f.close()

def main():
    while(1):
        ops = input("please input the operation (1 for feeding, 2 for pee, 3 for poop, 4 for customized events, 5 for deleting last stats) : \n")
        if ops in [1, 2, 3, 4, 5] :
            recorder(ops)
        else:
            return

if __name__ == "__main__":
    print("start the babystats :)")
    main()
