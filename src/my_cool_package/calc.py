import numpy as np


def some_data(shape: tuple[int]) -> np.ndarray:
    """
    Generate some data.

    This is really just calling :func:`numpy.random.rand`.

    Parameters
    ----------
    shape
        The shape of the data you want.

    Returns
    -------
    data
        Some data.

    Examples
    --------
    >>> import my_cool_package as mcp
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> mcp.calc.some_data(2)
    array([0.5488135 , 0.71518937])
    """
    if not hasattr(shape, "__iter__"):
        shape = (shape, )
    print(shape)
    return np.random.rand(*shape)
