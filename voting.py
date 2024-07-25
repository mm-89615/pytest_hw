"""
Нужно реализовать функцию, принимающую список чисел.
Вывести число, которое встречается чаще всего.
Максимальное число голосов всегда уникально.
"""


def vote_counting(votes: list[int]) -> int:
    if not isinstance(votes, list) or len(votes) == 0:
        raise ValueError('Нужен список чисел')

    set_votes = set(votes)
    max_res = 0
    max_i = votes[0]
    for i in set_votes:
        count = 0
        for vote in votes:
            if vote == i:
                count += 1
            if max_res < count:
                max_res = count
                max_i = i
    return max_i


if __name__ == '__main__':
    print(vote_counting([1, 1, 1, 2, 3]))
    print(vote_counting([1, 2, 3, 2, 2]))
    # print(vote_counting(1))
    # print(vote_counting("1"))
