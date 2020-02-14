
### Introduction
This is a web scraping project, scrapping stepstones.de using python and beautiful soup. This scraps only for jobs posted newer than 24 hours or seven days, which can be chose by user.

Run *scraper.py* for the initiating the scrapper.

### UML DIAGRAM

**Activity Diagram**
![alt_text](https://github.com/iramshiv/ase_scraping/blob/master/activity.jpg)

**Sequence Diagram**
![alt_text](https://github.com/iramshiv/ase_scraping/blob/master/Sequence.jpg)

**Use case Diagram**
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/usecase.jpg)

### Metrics
**Sonarcube**

**Codacy**


### Clean Code Development

**Naming Rules**
1. Descriptive and Intention revealing variable names.
2. Pronounceable and Searchablr names.

**Data Structures**
3. Data Structure exposes data and have no behaviours.

**Objects**
4. Objects expose behaviour and exposes no data.

**Functions**
5. Function should be small and concentrate on only one job.
6. Functions should have few arguments. (<3)
7. Function should have no side effects.
8. Fucntions should also have decriptive names.

**Tests**
9. Only one assert per test.
10. Should be as clean as production code.
11. should be easy to run.

**Error Handling**
12. Never mix erro handling and the code.
13. use exceptions instead of returning error codes.
14. first code "try catch finally" -> Structured code.
15. Always throws exceptions with constants.

### Build Management

*pybuilder* has been used as build management tool.
https://pybuilder.github.io/

Commands:

```sudo apt-get install pybuilder```

Inside the project directory:

```pyb --start-project```

for pychram Ide integration: 

add ```use_plugin('python.pycharm')``` in build.py
run ```pyb pycharm_generate```

These are the basic initiation commands.
build.py file is as below.

### IDE
PyCharm shortcuts

1. double ```shift``` -  search
2. ```alt + enter``` - Show intention actions and quick-fixes
3. ```F2``` - Navigate between code issues
4.```shift + F2``` - Jump to the next or previous highlighted error.
5. ```ctrl + /``` - line comment
6. ```shift + F10``` - run current file
7. ```shift + F9``` - debug current file
8. ```ctrl + f8``` - toogle line breakpoint
9. ```ctrl + alt + shift + f8``` - toogle temporary line breakpoint
10. ```ctrl + shift + f8``` - View Breakpoint

### Functional Programming

1. Final Data structure:

In src/main/userfunctions/job_scraper.py

Dict is used as below code,

```jobs = {} ```
```title_job = job_title.text```
```jobs[title_job] = {}```
    
 ```company_job = company_name.text```
 ```jobs[title_job]['company'] = company_job```
    
```posted_time_job = time_posted.get_text()```
```jobs[title_job]['time_posted'] = posted_time_job```
   
```final_link = "https://www.stepstone.de" + job_link.attrs['href']```
```jobs[title_job]['job_link'] = final_link```

**Output of Final data dtructure**
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/finalDS.jpg)

2. side-effect free function

The concepts behind functional programming requires functions to be stateless, and rely only on their given inputs to produce an output. The functions that meet the criteria are called pure functions. The benefit of using pure functions over impure (non-pure) functions is the reduction of side effects.

In src/main/userfunctions/duration_check.py
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/freefunction.jpg)

Result:
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/resultfreefunction.jpg)

It is an exapmle of side-effect free function.
