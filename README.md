
# What was developed

This project aims to analyze data from a CSV file. Methods were created to filter and return this information. The CSV file contains details about different jobs listed on the Glassdoor platform.

## Technologies

> Back-end: Python, Pytest and VS Code. 

# Skills Developed

- __Interactive Terminal:__ Proficient in using the ***Python*** interactive terminal.
  
- __Control Structures:__ Implemented conditional statements and loops effectively.
  
- __Built-in Functions:__ Utilized Python's built-in functions for efficient coding.
  
- __Exception Handling:__ Managed errors and exceptions gracefully in the code.
  
- __File Manipulation:__ Performed file operations such as reading, writing, and managing files.
  
- __Function Writing:__ Created custom functions to modularize and optimize the code.
  
- __Testing with Pytest:__ Developed and executed tests using ***Pytest*** to ensure code reliability.
  
- __Custom Modules:__ Wrote and imported custom Python modules to enhance code reusability.
  
# Features

<details>
  <summary><strong>On tests/counter/test_counter.py</strong></summary><br />

  > The test verifies if the function correctly returns the number of occurrences of the specified word.
  >
  > - Command to run the test in the terminal:
  >
  > ```bash
  > python3 -m pytest tests/counter/test_counter.py
  > ```

</details>

<details>
  <summary><strong>On src/insights/jobs.py</strong></summary><br />

  > - Method read: Responsible for opening the CSV file and returning the data as a list of dictionaries.
  >     
  > - Method get_unique_job_types: Responsible for returning a list of unique values present in the `job_type` column of the CSV file.
  >     
  > - Method filter_by_multiple_criteria: Allows filtering jobs by job type.

</details>

<details>
  <summary><strong>On src/insights/industries.py</strong></summary><br />

  > Method get_unique_industries: Should return a list of unique values present in the `industry` column.

</details>

<details>
  <summary><strong>On src/insights/salaries.py</strong></summary><br />

  > Method get_max_salary: Should extract the highest salary from the data that has been read and previously stored in the `self.jobs_list` list. The `ProcessSalaries` class inherits functionalities from the `ProcessJobs` class, including the ability to access previously read data without needing to read the file again.
     
  > Method get_min_salary: Should extract the lowest salary from the data that has been read and previously stored in the `self.jobs_list` list.

</details>

# Execute the project

1. __Clone the repository__

```bash
git clone https://github.com/KarenLukianyAlmeida/job-insights-python.git
```

2. __Create the virtual environment__
   
```bash
python3 -m venv .venv
```
3. __Activate the virtual environment__

```bash
source .venv/bin/activate
```

4. __Install the dependencies in the virtual environment__

```bash
python3 -m pip install -r dev-requirements.txt
```
