from dataclasses import dataclass
from pathlib import Path


@dataclass
class Job:
    job_id: str
    original_name: str
    work_path: Path

    def __str__(self) -> str:
        return (
            f"Job(job_id={self.job_id}, "
            f"original_name={self.original_name}, "
            f"work_file={self.work_path.name})"
        )