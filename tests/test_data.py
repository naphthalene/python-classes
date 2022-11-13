# ----------------------------------
# Tests
# ----------------------------------

import pytest

from homework.data import (
    Point,
    Segment,
    Square,
    Triangle,
)

# --------------------------------------------------
# Point class
@pytest.fixture
def point_origin():
    return Point(0, 0)

@pytest.fixture
def point_3_4():
    return Point(3, 4)

@pytest.fixture
def point_3_0():
    return Point(3, 0)

@pytest.fixture
def point_1_2():
    return Point(1, 2)

# --------------------------------------------------
def test_point(point_origin):
    assert point_origin.x == 0
    assert point_origin.y == 0

# --------------------------------------------------
# Segment class
@pytest.fixture
def segment_a(point_origin, point_3_0):
    return Segment(point_origin, point_3_0)

@pytest.fixture
def segment_b(point_3_4, point_3_0):
    return Segment(point_3_4, point_3_0)

# --------------------------------------------------
def test_segment(segment_a, segment_b):
    assert segment_a.length == 3
    assert segment_b.length == 4

# --------------------------------------------------
# Square class
@pytest.fixture
def square_unit(point_origin):
    return Square(point_origin, 1)

@pytest.fixture
def square_a(point_3_0):
    return Square(point_3_0, 5)

# --------------------------------------------------
def test_square(square_unit, square_a):
    assert square_unit.scale == 1
    assert square_unit.area == 1

    assert square_a.scale == 5
    assert square_a.area == 25

# --------------------------------------------------
# Triangle class
@pytest.fixture
def triangle_a(point_origin, point_3_0, point_3_4):
    return Triangle(
        point_origin,
        point_3_0,
        point_3_4
    )

# --------------------------------------------------
def test_triangle(triangle_a):
    assert triangle_a.area == (3 * 4) / 2
