from lesson_7.lesson7_cw1 import Matrix
import pytest


@pytest.mark.parametrize("m1, m2, expected_result", [(
        [[-5, -6], [1, 2, 3, 4, 5], []],
                         [[5, 6], [1, 2, 3, 4, -5], [], [1, 1, 1, 1, 1], []],
                         [[0, 0, 0, 0, 0],
                          [2, 4, 6, 8, 0],
                          [0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1]]),

])
def test_matrix_adding_eq(m1, m2, expected_result):
    matr1 = Matrix(m1)
    matr2 = Matrix(m2)
    assert matr1+matr2 == Matrix(expected_result)


@pytest.mark.parametrize("m1, m2, expected_result", [(
            [[-5, -7], [1, 2, 3, 4, 5], []],
            [[5, 6], [1, 2, 3, 4, -5], [], [1, 1, 1, 1, 1], []],
            [[0, 0, 0, 0, 0],
             [2, 4, 6, 8, 0],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1]])])
def test_matrix_adding_neq(m1, m2, expected_result):
    matr1 = Matrix(m1)
    matr2 = Matrix(m2)
    with pytest.raises(AssertionError):
        assert matr1+matr2 == Matrix(expected_result)
