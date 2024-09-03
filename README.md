
# Skills Developed

- __Interactive Terminal:__ Proficient in using the ***Python*** interactive terminal.
- __Control Structures:__ Implemented conditional statements and loops effectively.
- __Built-in Functions:__ Utilized Python's built-in functions for efficient coding.
- __Exception Handling:__ Managed errors and exceptions gracefully in the code.
- __File Manipulation:__ Performed file operations such as reading, writing, and managing files.
- __Function Writing:__ Created custom functions to modularize and optimize the code.
- __Testing with Pytest:__ Developed and executed tests using ***Pytest*** to ensure code reliability.
- __Custom Modules:__ Wrote and imported custom Python modules to enhance code reusability.
  
# What was developed

This project implemented analyses based on a dataset of jobs contained in a CSV file.

# Features

### On tests/counter/test_counter.py

The test verifies if the function correctly returns the number of occurrences of the specified word.

- Command to run the test in the terminal:

  ```bash
  python3 -m pytest tests/counter/test_counter.py
  ```

### On src/insights/jobs.py

1. __Method read:__ Responsible for opening the CSV file and returning the data as a list of dictionaries.
   
2. __Method get_unique_job_types:__ Responsible for returning a list of unique values present in the `job_type` column of the CSV file.
   
3. __Method filter_by_multiple_criteria:__ Allows filtering jobs by job type.

### On src/insights/industries.py

__Method get_unique_industries:__ Should return a list of unique values present in the `industry` column.

### On src/insights/salaries.py

1. __Method get_max_salary:__ Should extract the highest salary from the data that has been read and previously stored in the `self.jobs_list` list. The `ProcessSalaries` class inherits functionalities from the `ProcessJobs` class, including the ability to access previously read data without needing to read the file again.
   
2. __Method get_min_salary:__ Should extract the lowest salary from the data that has been read and previously stored in the `self.jobs_list` list.

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
