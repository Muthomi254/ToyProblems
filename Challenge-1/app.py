# Function to convert 12-hour time format to 24-hour format
def convertTo24Hrs(hours, minutes, period):
    # Check if it's in the evening ("pm") and not 12 o'clock
    if period == "pm" and hours != 12:
        # Add 12 hours to convert to 24-hour format
        hours += 12
    # Check if it's midnight ("am")
    elif period == "am" and hours == 12:
        # Set hours to 0 for 12:xx am
        hours = 0
    # Return the time in 24-hour format as a formatted string
    return f"{hours:02d}{minutes:02d}"

# Example usage
time1 = convertTo24Hrs(8, 10, "pm")
print(time1)

time2 = convertTo24Hrs(1, 10, "pm")
print(time2)
