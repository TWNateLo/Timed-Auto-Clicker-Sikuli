from datetime import datetime, date, time
#print datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

#Change to your target starting time!
#default starttime = '05:01:07'
#default endtime = '07:55:00'
starttime = '05:01:07'
endtime = '07:55:00'
#
while 1 == 1:
    currenttime = datetime.strftime(datetime.now(), '%H:%M:%S')
    if currenttime == starttime:
        #print 'Start!'
        for _ in range(8):
            click("1475289044279.png")
            sleep(0.7)
        break
    else:
        pass
#
while 1==1:
    currenttime = datetime.strftime(datetime.now(), '%H:%M:%S')
    if currenttime == endtime:
        for _ in range(8):
            click("1475369596012.png")
            sleep(0.7)
        break
    else:
        pass
#
print 'Todays downloading task, COMPLETED! At'
print datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
