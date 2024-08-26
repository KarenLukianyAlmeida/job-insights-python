from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary_listed = 0

        for job in self.jobs_list:
            salary = job.get("max_salary")
            if salary and salary.isdigit():
                salary = int(salary)
                if salary > max_salary_listed:
                    max_salary_listed = salary
        return max_salary_listed

    def get_min_salary(self) -> int:
        min_salary_listed = 0

        for job in self.jobs_list:
            salary = job.get("min_salary")
            if salary and salary.isdigit():
                salary = int(salary)
                if salary < min_salary_listed:
                    min_salary_listed = salary
        return min_salary_listed

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
