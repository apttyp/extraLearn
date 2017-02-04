
##闰年
def count(year):
    if ((year%400==0) or (year%4==0 and year%100!=0)):
        return '%d is runnian' %year
    else:
        return '%d is not runnian'%year

rs = count(2000)
print rs
