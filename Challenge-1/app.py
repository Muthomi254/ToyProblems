def convertTo24Hrs(hours,minutes,period):
  if period == "pm" and hours != 12 : hours += 12
  elif period == "am" and hours == 12 : hours = 0
  return f"{hours:02d}{minutes:02d}"

time = convertTo24Hrs(8,10,"pm")
print(time)

time = convertTo24Hrs(1,10,"pm")
print(time)