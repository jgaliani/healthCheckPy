from healthCheck.variaveis import var
from healthCheck.func import check
from healthCheck.func import sendmail
import time

tempo = (var.tempo)*60

def timerRun():
    time.sleep(tempo)
    flag = check.checksite()

    print(flag)
    if flag == False :
        print(flag)
        sendmail.reportEmail()
        timerRun()
    else:
        print(flag)
        print('roda denovo2')
        timerRun()



