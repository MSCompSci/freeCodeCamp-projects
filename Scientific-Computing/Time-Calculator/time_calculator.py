def add_time(start, duration,weekday="day"):
  start = start.split()
  startampm = start[1]
  starthour = start[0].split(':')[0]
  startmin = start[0].split(':')[1]
  dur = duration.split(":")
  durhour = dur[0]
  durmin = dur[1]
  newampm = " "+startampm
  days = 0
  week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
  daynames=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
  weekday = weekday.lower()
  newhr = int(starthour)+int(durhour)
  newmin = int(startmin) + int(durmin)

  if newmin > 60:
    newmin-=60
    newhr +=1
  if newmin < 10:
    newmin = "0"+str(newmin)
  while newhr>24:
    newhr -= 24
    days += 1
  if not newhr<12:
    if newhr>12:
      newhr -= 12
    if startampm == "AM":
      newampm = " PM"
    else:
      newampm = " AM"
      days +=1
  new_time = (str(newhr)+":"+str(newmin)+newampm)
  if weekday in week:
    weekdayindex = (week.index(weekday)+days)
    while weekdayindex>6:
      weekdayindex -=7
    weekday = daynames[weekdayindex]
    new_time = new_time + ","+" "+weekday
  if days == 1:
    new_time = new_time+" (next day)"
  elif days>1:
    new_time = new_time+" ("+str(days)+" days later)"

  return new_time
