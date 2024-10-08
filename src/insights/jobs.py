from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, mode="r", encoding="utf8") as file:
            jobs_reader = csv.DictReader(file, delimiter=",")

            for row in jobs_reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_type = set()

        for job in self.jobs_list:
            if "job_type" in job:
                job_type.add(job["job_type"])
        return list(job_type)

    def filter_by_multiple_criteria(
        self,
        list,
        filter_criteria: Dict,
    ) -> List[dict]:
        jobs_list = []

        for job in list:
            if (
                filter_criteria["industry"] == job["industry"]
                and filter_criteria["job_type"] == job["job_type"]
            ):
                jobs_list.append(job)
        return jobs_list
