[![Build Status](https://travis-ci.org/iramshiv/ase_scraper.svg?branch=master)](https://travis-ci.org/iramshiv/ase_scraper)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=iramshiv_ase_scraper&metric=alert_status)](https://sonarcloud.io/dashboard?id=iramshiv_ase_scraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f83a1ffaa6964bfaa4d52be6cf2e1245)](https://www.codacy.com/manual/iramshiv/ase_scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=iramshiv/ase_scraper&amp;utm_campaign=Badge_Grade)

### Introduction
This is a web scraping project, scrapping stepstones.de using python and beautiful soup. This scraps only for jobs posted newer than 24 hours or seven days, which can be chose by user.

Run *scraper.py* to initiate the scrapper.

### UML DIAGRAM

**Activity Diagram**
![alt_tex](https://github.com/iramshiv/ase_scraping/blob/master/activity.jpg)

**Sequence Diagram**
![alt_text](https://github.com/iramshiv/ase_scraping/blob/master/Sequence.jpg)

**Use case Diagram**
![alt-text](https://github.com/iramshiv/ase_scraper/blob/master/usecase.jpg)

### Metrics
**Sonarcube**
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=iramshiv_ase_scraper&metric=alert_status)](https://sonarcloud.io/dashboard?id=iramshiv_ase_scraper)

**Codacy**
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f83a1ffaa6964bfaa4d52be6cf2e1245)](https://www.codacy.com/manual/iramshiv/ase_scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=iramshiv/ase_scraper&amp;utm_campaign=Badge_Grade)

### Clean Code Development

**Naming Rules**
- Descriptive and Intention revealing variable names. 
- Pronounceable and Searchable names.
*Both the points has been covered in the project like as (eg.,) job_title, job_destination.*

**Data Structures**
- exposes data and have no behaviours.
*This point has been covered under final data structures*

**Objects**
- expose behaviour and exposes no data.

**Functions**
- should be small and concentrate on only one job.
- should have few arguments. (less than 3)
- should have no side effects.
- should also have decriptive names.
*all these points have been covered. (eg.,) duration_check(duration_value) which is covered under 'side effect free function'*

**Tests**
- only one assert per test.
- should be as clean as production code.
- should be easy to run.
* all the points have been covered for the url_session_tests.*

**Error Handling**
- Never mix error handling and the code.
- use exceptions instead of returning error codes.
- first code "try catch finally" -> Structured code.
- Always throws exceptions with constants.

### Build Management
*pybuilder* has been used as build management tool. <https://pybuilder.github.io/>

Commands:

```sudo apt-get install pybuilder```

Inside the project directory:

```pyb --start-project```
````pyb verify```
```pyb-publish```
```pip install target/dist/myproject-1.0.dev0/dist/*.tar.gz```
```cd target/dist/*/```
```python setup.py upload```

for pychram Ide integration: 

add ```use_plugin('python.pycharm')``` in build.py
run ```pyb pycharm_generate```

These are the basic initiation commands.
build.py file is as below.
![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/pybuilder.jpg)

### IDE
PyCharm shortcuts

- double ```shift``` search
- ```alt+enter``` Show intention actions and quick-fixes
- ```F2``` Navigate between code issues
- ```shift+F2``` Jump to the next or previous highlighted error.
- ```ctrl+/``` line comment
- ```shift+F10``` run current file
- ```shift+F9``` debug current file
- ```ctrl+f8``` toogle line breakpoint
- ```ctrl+alt+shift+f8``` toogle temporary line breakpoint
- ```ctrl+shift+f8``` View Breakpoint

### Functional Programming

1. Final Data structure:

In src/main/userfunctions/job_scraper.py

'Dict' is used as below code,

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

2. side effect free function

The concepts behind functional programming requires functions to be stateless, and rely only on their given inputs to produce an output. The functions that meet the criteria are also called pure functions. The benefit of using pure functions over impure (non-pure) functions is the reduction of side effects.

In src/main/userfunctions/duration_check.py
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/freefunction.jpg)

Result:
![alt-text](https://github.com/iramshiv/ase_scraping/blob/master/resultfreefunction.jpg)

It is an exapmle of side-effect free function.

3. as parameter and return value:
![alt-text](https://github.com/iramshiv/ase_scraper/blob/master/images/funParVal.jpg)

```duration_check()``` fucntion is used as a parameter in ```duration_url_checker()```.

```page_incrementer()``` is used as a return value.

Higher order fuction:
![alt-text](https://github.com/iramshiv/ase_scraper/blob/master/images/higher.jpg)

Anonymous functions:
![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/anonymous.jpg)

### Continous Integration
Travis - CI
[![Build Status](https://travis-ci.org/iramshiv/ase_scraper.svg?branch=master)](https://travis-ci.org/iramshiv/ase_scraper)

### Unit Tests

example unit test for url checking is coded and test results are,
![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/utest.jpg)
![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/testresult.jpg)

### DSL

An example of dsl is implemented in the project, eventhough it doesn't contribute to the project.
This is DSL for adding two numbers.

*Source dsl script*

![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/srcdsl.jpg)

*Module file*

![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/moduledsl.jpg)

*DSL python file*

![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/dslpy.jpg)

*DSL result*

![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/resultdsl.jpg)

### Alternative

Data are scrapped in this project by the "class name" of the "div" element. 

"stepstones.de" usually changes the class names frequently but the structure of the html page remains same through my observation. 

So, I also propose an alternate way to scrape the data by scrapping the "class name of div elements first", then the data is scrapped.

example of the code is in file ```tag_scraper.py```

![alt_text](https://github.com/iramshiv/ase_scraper/blob/master/images/altscrape.jpg)

This file also saves the data scrapped as ```jobs.csv``` format apart from the terminal output.

I will continue updating the project with following functions in future,
    - including scrapping other wesites.
    - hosting this project as a web application.
    - forwarding automatic email about job offers.
    

