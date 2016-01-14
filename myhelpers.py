from numpy import where


def pos(x):
    """
        Returns (x)_+, i.e.
        pos(x) = x if x > 0, else 0

        Input:
            x: numeric or array_like.

        Output:
            y: arraylike copy of x with negative entries set to 0
    """
    return where(x > 0, x, 0)


def neg(x):
    """
        Returns (x)_-, i.e.
        neg(x) = x if x < 0, else 0

        Input:
            x: numeric or array_like.

        Output:
            y: arraylike copy of x with positive entries set to 0
    """
    return where(x < 0, x, 0)
