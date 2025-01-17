import pytest
from water_flow import pressure_loss_from_water_flow

# Test Function 1: Test pressure loss from fittings
def test_pressure_loss_from_water_flow():
    # Ensure the function works for different fitting types
    assert abs(pressure_loss_from_fittings(0.00, 3, 'elbow') - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 0, 'elbow') - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 2, 'elbow') - -0.109) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 2, 'elbow') - -0.122) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 5, 'elbow') - -0.306) < 0.001

# Test Function 2: Test Reynolds number calculation
def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 0.00) - 0) < 1
    assert abs(reynolds_number(0.048692, 1.65) - 80069) < 1
    assert abs(reynolds_number(0.048692, 1.75) - 84922) < 1
    assert abs(reynolds_number(0.286870, 1.65) - 471729) < 1
    assert abs(reynolds_number(0.286870, 1.75) - 500318) < 1

# Test Function 3: Test pressure loss from pipe reduction
def test_pressure_loss_from_pipe_reduction():
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 0.00, 0) - 0.000) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729) - -163.744) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318) - -184.182) < 0.001

# Run all tests
if __name__ == "__main__":
    pytest.main()
