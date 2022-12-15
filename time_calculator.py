import re
import Math

def add_time(start, duration, startDOW=None):
  dows = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
  new_time = ""  
  print(start,duration,startDOW)
  startRE = re.split(r"(\d+):(\d+) (\S+)", start)
  #print(startRE)
  origP = startRE[3]
  startHr = int(startRE[1])
  if origP == "PM":
    startHr += 12
  startMin = int(startRE[2])
    
  durationRE = re.split(r"(\d+):(\d+)", duration)
  #print(durationRE)
  durHrs = int(durationRE[1])
  durMins = int(durationRE[2])

  minutes = (startMin + durMins) % 60
  #print(minutes)
  tmpHrs = startHr + durHrs + ((startMin + durMins) // 60)
  hours = tmpHrs % 24
  days  = tmpHrs // 24
  
  if ( hours >= 12):
    hours -= 12
    newP = "PM"
  else:
    newP = "AM"
    
  if hours == 0:
    hours = 12
  
  if startDOW == None:
    new_time = f"{hours}:{minutes:0>2} {newP}"
  else:
    index = dows.index(startDOW.capitalize())
    newDow = (index + days) % 7
    new_time = f"{hours}:{minutes:0>2} {newP}, {dows[newDow]}"
  if days > 1:
    new_time += f" ({days} days later)"
  elif days == 1:
    new_time += f" (next day)"
  print (new_time)
  return new_time
