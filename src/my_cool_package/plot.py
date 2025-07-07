import numpy as np
import matplotlib.pyplot as plt


def cool_plot(x: np.ndarray):
    """
    Look at this cool function.

    Maybe generate some data with :func:`~my_cool_package.calc.some_data`?

    Parameters
    ----------
    x
        The thing we want to plot.

    Examples
    --------
    .. plot::
      :include-source:

        >>> import my_cool_package as mcp
        >>> mcp.plot.cool_plot(mcp.calc.some_data(100))
    """
    plt.plot(x)
