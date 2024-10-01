# ymdhms_to_jd.py

# Usage: py ymdhms_to_jd.py year month day hour minute second

# Output:
#  Converts year, month, day, hour, minute, second to fractional julian date
#
# Written by Jayden Warren
# Other contributors: None

# import Python modules
import sys # argv

# "constants"
w = 7.292115*10**-5

# initialize script arguments
year = float('nan') # year
month = float('nan') # month
day = float('nan') # day
hour = float('nan') # hour
minute = float('nan') # minute
second = float('nan') # second

# parse script arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day  = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(\
     'Usage: '\
     'py ymdhms_to_jd.py year month day hour minute second'\
    )
    exit()

# write script below this line
jd = day - 32075.0 + 1461*(year + 4800 + (month - 14)/12)/4 + 367*(month - 2 - (month - 14)/12*12)/12 - 3*((year + 4900 + (month - 14)/12)/100)/4
jd_midnight = jd - 0.5
d_fractional = (second + 60*(minute + 60*hour))/86400
jd_fractional = jd_midnight + d_fractional
jd_frac = jd_fractional

print(jd_frac)