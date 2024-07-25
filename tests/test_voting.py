import pytest

from voting import vote_counting


class TestVoting:

    @pytest.mark.parametrize(
        "votes, expected",
        [
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
        ]
    )
    def test_vote_counting(self, votes, expected):
        assert vote_counting(votes) == expected

    @pytest.mark.parametrize(
        "value",
        [
            1,
            "1",
        ]
    )
    def test_vote_counting_exception(self, value):
        with pytest.raises(ValueError):
            vote_counting(value)
