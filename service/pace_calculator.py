import math

def secs_to_time(seconds: int): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hour, minutes, seconds)

def hms_to_seconds(hours: int, minutes: int, seconds: int):
    return (hours*60*60)+(minutes*60)+seconds


class Pacer():
    def __init__(self):
        pass

    def paceCalc(self, distance, paceM, paceS):
        #print(float(distance))
        #print(float(paceM))
        #print(float(paceS))
        results = []
        for i in range(0, int(distance)+1):
            total_seconds = (int(paceM) * (i*60)) + int((int(paceS) *i))
            time = secs_to_time(total_seconds)
            timestring = "{}{}{}{}".format("Mile: ", i, " Time: ", time)
            #"Mile: " + i + " Time: " + time
            results.append(timestring)
        
        return results
