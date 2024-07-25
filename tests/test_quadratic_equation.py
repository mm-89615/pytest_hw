import pytest

from quadratic_equation import quadratic_equation, discriminant


class TestQuadraticEquation:

    @pytest.mark.parametrize(
        'a,b,c,result',
        (
            [1, 8, 15, 4],
            [1, -13, 12, 121],
            [4, 2, -3, 52],
            [-4, 28, -49, 0],
            [2, 4, 2, 0],
            [1, 1, 1, -3],
            [3, -5, 3, -11],
        )
    )
    def test_discriminant(self, a, b, c, result):
        assert discriminant(a, b, c) == result

    @pytest.mark.parametrize(
        'a,b,c,root1,root2',
        (
                [1, 8, 15, -3.0, -5.0],
                [1, -13, 12, 12.0, 1.0],
                [4, 2, -3, 0.65, -1.15]
        )
    )
    def test_quadratic_equation_two_root(self, a, b, c, root1, root2):
        assert quadratic_equation(a, b, c) == (root1, root2)

    @pytest.mark.parametrize(
        'a,b,c,root',
        (
            [-4, 28, -49, 3.5],
            [2, 4, 2, -1.0],
        )
    )
    def test_quadratic_equation_one_root(self, a, b, c, root):
        assert quadratic_equation(a, b, c) == root

    @pytest.mark.parametrize(
        'a,b,c',
        (
            [1, 1, 1],
            [3, -5, 3],
        )
    )
    def test_quadratic_equation_zero_root(self, a, b, c):
        assert quadratic_equation(a, b, c) == "Корней нет"
