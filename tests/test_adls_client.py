from src.adls_client import filter_blobs
import pytest


@pytest.mark.parametrize(
    "blob_names, extension, expected",
    [
        pytest.param(
            [
                "file1.csv.gz",
                "file2.txt",
                "file3.csv.gz",
                "file4.doc",
                "file5.domain.test.txt",
            ],
            ".txt",
            ["file2.txt", "file5.domain.test.txt"],
            id="Find .txt files in a list with mixed matching and non-matching",
        ),
        pytest.param([], ".txt", [], id="Empty input returns empty result."),
        pytest.param(
            [
                "file1.csv.gz",
                "file2.txt",
                "file3.csv.gz",
                "file4.doc",
                "file5.domain.test.txt",
            ],
            ".docx",
            [],
            id="List with no matches returns empty result",
        ),
        pytest.param(
            [
                "file1.csv.gz",
                "file2.txt",
                "file3.csv.gz",
                "file4.doc",
                "file5.domain.test.txt",
            ],
            "",
            [],
            id="Input is empty string"
        ),
        pytest.param(
            [
                "Azure Public Dataset - Trace Analysis.ipynb",
                "schema.csv",
                "sosp_data/category.txt",
                "sosp_data/cores.txt",
                "sosp_data/cpu.txt",
                "sosp_data/deployment.txt",
                "sosp_data/lifetime.txt",
                "sosp_data/memory.txt",
                "trace_data/deployment/deployment.csv.gz",
                "trace_data/subscriptions/subscriptions.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-1-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-10-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-100-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-101-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-102-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-103-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-104-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-105-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-106-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-107-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-108-of-125.csv.gz",
            ],
            ".csv.gz",
            [
                "trace_data/deployment/deployment.csv.gz",
                "trace_data/subscriptions/subscriptions.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-1-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-10-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-100-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-101-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-102-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-103-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-104-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-105-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-106-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-107-of-125.csv.gz",
                "trace_data/vm_cpu_readings/vm_cpu_readings-file-108-of-125.csv.gz",
            ],
            id="Find .csv.gz files in data similar to actual dataset",
        ),
    ],
)
def test_filter_blobs(blob_names, extension, expected):
    assert filter_blobs(blob_names, extension) == expected
