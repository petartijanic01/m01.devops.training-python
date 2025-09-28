from demo_project import calculator


def test_integration_workflow():
    # Simulate a workflow using multiple operations
    a = 10
    b = 5
    result = calculator.add(a, b)           # 10 + 5 = 15
    result = calculator.multiply(result, 2)   # 15 * 2 = 30
    result = calculator.subtract(result, 10)  # 30 - 10 = 20
    result = calculator.divide(result, 4)     # 20 / 4 = 5
    assert result == 5
