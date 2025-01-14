def ft_tqdm(lst: range):
    """
    A custom progress bar generator that mimics the behavior of tqdm.

    This function iterates over a range (`lst`) and yields each element while
    displaying a progress bar in the terminal. The progress bar updates in
    real-time to reflect the progress of the iteration.

    Args:
        lst (range): A range object representing the sequence to iterate over.

    Yields:
        int: The current element from the range.
    """
    total = len(lst)
    for i in lst:
        c = i + 1
        percent = (c / total) * 100
        bar = "█" * int(percent)
        spaces = " " * (100 - len(bar))
        if not c % 10 or c == total:
            print(f"\r{percent:3.0f}%|{bar}{spaces}| {c}/{total}", end="")
        yield i
