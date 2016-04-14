x = '2014-01-09 20:45:25'
t = time.strptime(x, "%Y-%m-%d %H:%M:%S")

print (t)
# time.struct_time(tm_year=2014, tm_mon=1, tm_mday=9, tm_hour=20, tm_min=45, tm_se
# c=25, tm_wday=3, tm_yday=9, tm_isdst=-1)

print(t.tm_hour)