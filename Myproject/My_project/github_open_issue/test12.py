from lxml import html
import requests
import datetime
from github_open_issue.test1 import test1
from prettytable import PrettyTable
class test12:
    def fun1(self,url):
        date_test = test1()
        t = PrettyTable(['Total Open Issues', 'Number of Last 24 hours open Issues', 'Number of Issues beween 24 hours to last 7 days', 'Number of Issues before 7 days'])
        #print(t)
        url = url + '/issues'
        #url = 'https://github.com/facebook/WebDriverAgent/issues'
        #url = 'https://github.com/amitness/dotfiles/issues'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        open_issue = tree.xpath('//span[@class="Counter"]/text()')
        Total_open_issue = open_issue[0]
        #print(open_issue[0])
        #t.add_row(Total_open_issue)
        #print(t)
        buyers = []
        if(int(Total_open_issue)>25):
            val1 = int(int(Total_open_issue)/25)
            if(int(Total_open_issue)%25 != 0):
                val1 = val1 + 1
            for i in range(0,val1):
                #import pdb 
                #pdb.set_trace()
                url1 = url+"?page="+str(i+1)+"&q=is%3Aissue+is%3Aopen"
                page = requests.get(url1)
                tree = html.fromstring(page.content)
                buyers1 = tree.xpath('//span[@class="opened-by"]//relative-time[@datetime]/text()')
                buyers.append(buyers1)
        else:
            buyers = tree.xpath('//span[@class="opened-by"]//relative-time[@datetime]/text()')
        issue_same_day = 0
        issue_till_7day = 0
        issue_after_7day = 0
        #import pdb
        #pdb.set_trace()
        #print(len(buyers))
        #print(buyers)
        if(int(Total_open_issue)>25):
            for x in range(0, len(buyers)):
                for y in range(0,len(buyers[x])):
                    val = date_test.check_date(buyers[x][y])
                    if(val == 1):
                        issue_same_day = issue_same_day + 1
                    elif(val == 2):
                        issue_after_7day = issue_after_7day + 1
                    elif(val == 3):
                        issue_till_7day = issue_till_7day + 1
        else:
            for x in range(0, len(buyers)):
                val = date_test.check_date(buyers[x])
                if(val == 1):
                    issue_same_day = issue_same_day + 1
                elif(val == 2):
                    issue_after_7day = issue_after_7day + 1
                elif(val == 3):
                    issue_till_7day = issue_till_7day + 1
                        

        t.add_row([Total_open_issue,issue_same_day,issue_till_7day,issue_after_7day])
        print(t)
        files = []
        files.append(Total_open_issue)
        files.append(issue_same_day)
        files.append(issue_after_7day)
        files.append(issue_till_7day)

 
        #import pdb
        #pdb.set_trace()
        #print(issue_till_7day)
        #print(issue_after_7day)
        #print(issue_same_day)
        return files
        #date_time = datetime.datetime.now()
        #date = date_time.date()
        #time = date_time.time()
        #mon = date.month
        #yr = date.year
        #url = 'https://github.com/facebook/WebDriverAgent/issues'
    #print(fun1())
        

    
