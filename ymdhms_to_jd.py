# yes.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second.

# Converts year month day hour minute second to juliat date 
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# year integer
# month integer 1-12
# day integer 1-31
# hour integer 1-23
# min integer 0-59
# sec float

# Output:
#  prints julian date of ymdhms
#
# Written by Isha Aurora
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
year = float('nan')  
mon = float('nan')  
day = float('nan')  
hour = float('nan')
min = float('nan')
sec = float('nan')

# parse script arguments (always 1 more than the number of arguments)
if len(sys.argv) == 7:
    try:
        year = float(sys.argv[1])
        mon = float(sys.argv[2])
        day = float(sys.argv[3])
        hour = float(sys.argv[4])
        min = float(sys.argv[5])
        sec = float(sys.argv[6])
    except ValueError:
        print("Error: year, mon, day, hour, min, sec must be numeric.")
        exit()
else:
    print('python3 ymdhms_to_jd.py year, mon, day, hour, min, sec')
    exit()

# write script below this line

jd = day - 32075 + 1461*(year+4800+(mon-14)/12)/4 + 367*(mon-2-(mon-14)/12*12)/12-3*((year+4900+(mon-14)/12)/100)/4
dfrac = (sec + 60*(min+60*hour))/86400
jdmidnight = jd-.5
jdfrac = jdmidnight+dfrac

print(jdfrac)