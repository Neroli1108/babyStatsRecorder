import os, sys
import datetime

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
    if(ops == 1):
        breastfeeding = input("what is the  amount of the breastfeeding milk this time? \n")
        breastfeedingTime = input("how long have you fed your baby (min) ? \n")
        formula = input("what is the amount of the formula this time? \n")
        total = formula + breastfeeding
        msg = "{date}: baby is fed: breastfeeding: {breastfeeding} oz; formula: {formula} oz; total: {total} oz; breastfeeding(time): {time} mins \n".format(date = dates, breastfeeding=breastfeeding, formula=formula, total=total, time=breastfeedingTime)
    if(ops == 2):
        msg = "{date}: baby pees. \n".format(date = dates)
    if(ops == 3):
        msg = "{date}: baby poops. \n".format(date = dates)
    if(ops == 4):
        done = input("what happened to baby?\n")
        msg = "{date}: {done}\n".format(date=dates, done=done)
    if msg != None:
        return msg

def recorder(ops):
    checkBabystatsLog();
    msg = generateMsg(ops)
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
