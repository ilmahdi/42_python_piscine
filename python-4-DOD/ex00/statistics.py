from typing import Any


def mean(nbs: list) -> float:
    """Calculate the mean (average)"""
    return sum(nbs) / len(nbs)


def median(nbs: list) -> float:
    """Calculate the median (middle value)"""
    if len(nbs) % 2:
        return nbs[int(len(nbs) / 2)]
    else:
        return (nbs[int(len(nbs) / 2)] + nbs[int(len(nbs) / 2) - 1]) / 2


def quartile(nbs: list) -> list:
    """Calculate the first (Q1) and third (Q3) quartiles"""
    return [
        float(median(nbs[0: int(len(nbs) / 2) + len(nbs) % 2])),
        float(median(nbs[int(len(nbs) / 2):])),
    ]


def variance(nbs: list) -> list:
    """Calculate the variance"""
    mn = mean(nbs)
    return sum([(x - mn) ** 2 for x in nbs]) / len(nbs)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Compute and print statistical metrics (mean, median, quartile, var, std).
    """
    numbers = list(args)
    numbers.sort()
    operations = {}
    if len(args):
        operations = {
            "mean": f"mean : {mean(numbers)}",
            "median": f"median : {median(numbers)}",
            "quartile": f"quartile : {quartile(numbers)}",
            "var": f"var : {variance(numbers)}",
            "std": f"std : {variance(numbers) ** (1/2)}",
        }
    for op in kwargs.values():
        if op in operations:
            print(operations[op])
        elif not len(args):
            print("ERROR")
