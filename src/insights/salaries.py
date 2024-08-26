from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary_listed = []

        for job in self.jobs_list:
            salary = job.get("max_salary")
            if salary and salary.isdigit():
                max_salary_listed.append(int(salary))
        return max(max_salary_listed, default=0)

    def get_min_salary(self) -> int:
        min_salary_listed = []

        for job in self.jobs_list:
            salary = job.get("min_salary")
            if salary and salary.isdigit():
                min_salary_listed.append(int(salary))
        return min(min_salary_listed, default=0)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
