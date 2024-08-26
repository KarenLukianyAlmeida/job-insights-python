from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industries = set()
        list = self.jobs_list

        for job in list:
            industries.add(job["industry"])
        return industries
