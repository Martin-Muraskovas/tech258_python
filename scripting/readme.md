# What is scripting
Scripting is the process of create code to automate a specific task. Scripts are generally reusable.
Scripts are typically a sequence of instructions that is interpreted and carried out by another program
instead of directly by the CPU 

## What are the packages in the standard Python library?
Here are some examples of packages within the standard Python Library:
* random
```python
import random
print(random.random())
print(random.randrange(1, 10))
```
* math
```python
import math
num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
print(f"Remainder from 1/5: {math.remainder(1, 5)}")
```
* os
```python
import os
# returning current working directory
working_dir = os.getcwd()
print(f"Current working directory: {working_dir}")

# get user
username = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"Username is: {username}")

# cpu cores
cpu_cores = os.cpu_count()
print(f"Amount of CPU cores: {cpu_cores}")

# make directory
os.mkdir("test_dir")
```
* datetime
```python
import datetime
print(f"Today's date is: {datetime.datetime.today()}")
```
* builtins
```python
import builtins
for name in dir(builtins):
    if name[0].islower():
        print(name)
```
* requests
```python
import requests
requests_bbc = requests.get("https://www.bbc.co.uk/")
print(requests_bbc.status_code)
print(requests_bbc.content)
```

## 10 Scripts a DevOps Engineer may create
### 1. Notification Scripts

### 2. Security Automation Scripts

### 3. Container Scripts

### 4. Continuous Integration Scripts

### 5. Deployment Automation Scripts

### 6. Security Scripts

### 7. Log Analysis Scripts

### 8. Configuration Scripts

### 9. Infrastructure as Code (IaC) Scripts

### 10. Back-up Scripts


