# OpenIssue
Find Open issues in GIT URL

problem Statments :-
This will help you to find the number of open issues in any github repo . 
i/p:-
Give the url (Example)
1.  https://github.com/garris/BackstopJS
2.  https://github.com/amitness/dotfiles

   
prerequisite:
1. Python with version >= 3
2. Conda  library

   Follow this Step to run :
1. git clone https://github.com/kandoi1994/OpenIssue.git
2. cd Myproject/My_project (run the command from the directory where you did clone)
3. conda create -n github_issue python (github_issue is name of virtual environment you can give what you want)
4. conda activate github_issue
5. pip install Django==1.9.1
6. pip install requests
7. pip install prettytable
8. pip install lxml
9. pip install timedelta
10. python manage.py runserver 127.0.0.1:8000

 After running all the above command go to   127.0.0.1:8000. and give the url .

O/p :- 
You will able to see the output in console . 
