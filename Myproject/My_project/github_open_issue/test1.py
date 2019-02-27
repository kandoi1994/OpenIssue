import datetime , timedelta
class test1:
    def check_date(self,issue_date):
        #import pdb
        #pdb.set_trace()
        date_time = datetime.datetime.now()
        N = 7
        #date_N_days_ago = datetime.now() - timedelta(days=N)
        date = date_time.date()
        mon = date.month
        yr = date.year
        dd = date.day
        #date_n_time = date_N_days_ago.date()
        #dd7 = date_n_time.day
        #mon7 = date_n_time.month
        #yr7 = date_n_time.year        
        index_comma = issue_date.find(',')
        Issue_Date = issue_date[4:index_comma]
        Issue_year= issue_date[index_comma+2:index_comma+6]
        Issue_Month = issue_date[0:3]
        Month_map = {
		"Jan" : 1,
		"Feb" : 2,
		"Mar" : 3,
		"Apr" : 4,
		"May" : 5,
		"Jun" : 6,
        "Jul" : 7,
        "Aug" : 8,
        "Sep" : 9,
        "Oct" : 10,
        "Nov" : 11,
        "Dec" : 12
		
	}
        #import pdb
        #pdb.set_trace()
        #print(Issue_Date)
        #print(dd)
        #print(mon)
        #print(yr)

        if(Issue_Date == str(dd) and  Issue_year == str(yr) and  Month_map[Issue_Month] == mon ):
            return 1

        elif(int(Issue_year) <= yr-2 ):
            return 2

        elif(Issue_year == str(yr-1) and  (Month_map[Issue_Month] != mon -1 and  Month_map[Issue_Month] -1 != mon) ):
            return 2

        elif(Issue_year == str(yr-1) and  (Month_map[Issue_Month] ==  mon -1 or  Month_map[Issue_Month] -1 == mon) ):
            if(mon == 1 and Month_map[Issue_Month] == 12 and int(Issue_Date)>=24 and dd <= 6):
                diff1 = 31 - int(Issue_Date) + 1 
                diff2 = dd
                if (diff1 + diff2 <= 7):
                    return 3
            return 2

        elif((dd <= 7 or int(Issue_Date) >= dd-7) and  Issue_year == str(yr) and  Month_map[Issue_Month] == mon ):
            return 3

        elif(Issue_year == str(yr) and  (Month_map[Issue_Month] == mon -1 or  Month_map[Issue_Month] -1 == mon)  ):
            if(mon == 2 and int(Issue_Date)>=24 and dd <= 6):
                diff1 = 31 - int(Issue_Date) + 1 
                diff2 = dd
                if (diff1 + diff2 <= 7):
                    return 3
                else:
                    return 2
            elif(mon == 3 and int(Issue_Date)>=24 and dd <= 6):
                if(yr%4 != 0):
                    diff1 = 28 - int(Issue_Date) + 1 
                    diff2 = dd
                    if (diff1 + diff2 <= 7):
                        return 3
                    else:
                        return 2
                else:
                    diff1 = 29 - int(Issue_Date) + 1 
                    diff2 = dd
                    if (diff1 + diff2 <= 7):
                        return 3
                    else:
                        return 2
            elif((mon == 4 or mon == 6 or mon == 9 or mon == 11)and int(Issue_Date)>=24 and dd <= 6):
                diff1 = 31 - int(Issue_Date) + 1 
                diff2 = dd
                if (diff1 + diff2 <= 7):
                    return 3
                else:
                    return 2
            elif(int(Issue_Date)>=24 and dd <= 6):
                diff1 = 30 - int(Issue_Date) + 1 
                diff2 = dd
                if (diff1 + diff2 <= 7):
                    return 3
                else:
                    return 2

            return 2

        elif(Issue_year == str(yr) and  (Month_map[Issue_Month] != mon -1 and  Month_map[Issue_Month] -1 != mon) ):
            return 2
        return 4         
    
