# test_water_flow.py

import pytest
from water_flow import *

# Test for pressure_loss_from_fittings function
def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, abs=0.001)

# Test for reynolds_number function
def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == pytest.approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == pytest.approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == pytest.approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == pytest.approx(500318, abs=1)

# Test for pressure_loss_from_pipe_reduction function
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == pytest.approx(-184.182, abs=0.001)

# Test for kpa_to_psi conversion
def test_kpa_to_psi():
    assert kpa_to_psi(0) == 0
    assert kpa_to_psi(100) == pytest.approx(14.50377, abs=0.0001)
    assert kpa_to_psi(200) == pytest.approx(29.00754, abs=0.0001)

# Test for water_column_height function
def test_water_column_height():
    assert water_column_height(36.6, 9.1) == 27.5

# Test for pressure_gain_from_water_height function
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(27.5) == pytest.approx(271.475, abs=0.001)
