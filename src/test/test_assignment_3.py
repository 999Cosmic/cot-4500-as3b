import pytest
from main.assignment_3 import euler_method, runge_kutta, f, gaussian_elimination, determinant, lu_factorization, is_diagonally_dominant, is_positive_definite

def test_euler_method():
    result = euler_method(f, 0, 1, 2, 10)
    assert abs(result - 1.2446380979332121) < 1e-6

def test_runge_kutta():
    result = runge_kutta(f, 0, 1, 2, 10)
    assert abs(result - 1.251316587879806) < 1e-6

def test_gaussian_elimination():
    A = [
        [2, -1, 1, 6],
        [1, 3, 1, 0],
        [-1, 5, 4, -3]
    ]
    result = gaussian_elimination(A)
    assert result == [2.0, -1.0, 1.0]

def test_determinant():
    B = [
        [1, 1, 0, 3],
        [2, 1, -1, 1],
        [3, -1, -1, 2],
        [-1, 2, 3, -1]
    ]
    result = determinant(B)
    assert abs(result - 39.0) < 1e-6

def test_lu_factorization():
    B = [
        [1, 1, 0, 3],
        [2, 1, -1, 1],
        [3, -1, -1, 2],
        [-1, 2, 3, -1]
    ]
    L, U = lu_factorization(B)
    expected_L = [[1, 0, 0, 0], [2.0, 1, 0, 0], [3.0, 4.0, 1, 0], [-1.0, -3.0, 0.0, 1]]
    expected_U = [[1, 1, 0, 3], [0, -1.0, -1.0, -5.0], [0, 0, 3.0, 13.0], [0, 0, 0, -13.0]]
    assert L == expected_L
    assert U == expected_U

def test_diagonal_dominance():
    C = [
        [9, 0, 5, 2, 1],
        [3, 9, 1, 2, 1],
        [0, 1, 7, 2, 3],
        [4, 2, 3, 12, 2],
        [3, 2, 4, 0, 8]
    ]
    result, failing_row = is_diagonally_dominant(C)
    assert result is False
    assert failing_row == 4 # [9, 0, 5, 2, 1] is considered the 0th row

def test_positive_definite():
    D = [
        [2, 2, 1],
        [2, 3, 0],
        [1, 0, 2]
    ]
    assert is_positive_definite(D) is True

pytest.main()