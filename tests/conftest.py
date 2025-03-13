import pytest
from faker import Faker

def pytest_addoption(parser):
    parser.addoption(
        "--num_records", 
        action="store",
        default="10",
        help="Number of records to generate for tests"
    )

@pytest.fixture(scope="session")
def fake():
    """Fixture to provide a Faker instance."""
    return Faker()

@pytest.fixture
def generated_records(request, fake):
    """
    Fixture to generate a list of test records.
    Each record is a tuple: (a, b, operation, expected_result)
    """
    num_records = int(request.config.getoption("--num_records"))
    records = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=["add", "subtract", "multiply", "divide"])
        if operation == "add":
            expected = a + b
        elif operation == "subtract":
            expected = a - b
        elif operation == "multiply":
            expected = a * b
        elif operation == "divide":
            if b == 0:
                b = 1  # Avoid division by zero.
            expected = a / b
        else:
            # Fallback if operation is unexpected (should not happen)
            expected = None
        records.append((a, b, operation, expected))
    return records
