# What is scripting
Scripting is the process of create code to automate a specific task. Scripts are generally reusable.
Scripts are typically a sequence of instructions that is interpreted and carried out by another program
instead of directly by the CPU.

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
Develop scripts to send alerts and notifications via email, SMS, or messaging platforms based 
on predefined triggers such as system failures, performance issues, or deployment status updates.
### 2. Security Automation Scripts
Build scripts to automate security checks, vulnerability scanning,
and compliance audits across the infrastructure and application stack.
### 3. Container Scripts
Develop scripts to manage and orchestrate containers 
using Docker or Kubernetes, including deployment, scaling, and monitoring.
### 4. Continuous Integration Scripts
Create scripts to automate the CI process, including running tests,
code quality checks, and triggering builds upon code changes.
### 5. Deployment Automation Scripts
Automate the deployment process of applications by writing scripts that handle 
building, testing, and deploying code to various environments.
### 6. Configuration Management Scripts:
Create scripts to manage and update configuration files
across multiple servers or environments to ensure consistency and scalability
### 7. Log Analysis Scripts
Write scripts to parse and analyze log files for troubleshooting,
performance monitoring, and security auditing purposes.
### 8. Configuration Scripts
Create scripts to manage and update configuration files across multiple servers or 
environments to ensure consistency and scalability.
### 9. Infrastructure as Code (IaC) Scripts
Use Python scripts to define and provision infrastructure resources using tools like
Terraform or AWS CloudFormation for consistency and scalability.
### 10. Back-up Scripts
Write scripts to automate the backup of data, databases,
and configurations, as well as scripts to restore them when needed.
