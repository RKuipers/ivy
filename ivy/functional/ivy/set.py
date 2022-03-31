# global
from typing import Union, Tuple, Optional

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework


# Array API Standard #
# -------------------#

def unique_inverse(x: Union[ivy.Array, ivy.NativeArray]) \
        -> Tuple[ivy.Array, ivy.Array]:
    """
    Returns a tuple of two arrays, one being the unique elements of an input array x and the other one the indices from
    the set of uniques elements that reconstruct x.

    :param x: input array.
    :return: tuple of two arrays (values, inverse_indices)
    """
    return _cur_framework.unique_inverse(x)


def unique_values(x: Union[ivy.Array, ivy.NativeArray])\
        -> ivy.Array:
    """
    Returns the unique elements of an input array ``x``.
    .. admonition:: Data-dependent output shape
        :class: important
        The shapes of two of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.
    .. note::
       Uniqueness should be determined based on value equality (i.e., ``x_i == x_j``). For input arrays having floating-point data types, value-based equality implies the following behavior.
       -   As ``nan`` values compare as ``False``, ``nan`` values should be considered distinct.
       -   As ``-0`` and ``+0`` compare as ``True``, signed zeros should not be considered distinct, and the corresponding unique element will be implementation-dependent (e.g., an implementation could choose to return ``-0`` if ``-0`` occurs before ``+0``).
    Parameters
    ----------
    x: array
        input array. If ``x`` has more than one dimension, the function must flatten ``x`` and return the unique elements of the flattened array.
    Returns
    -------
    out: array
        an array containing the set of unique elements in ``x``. The returned array must have the same data type as ``x``.
        .. note::
           The order of unique elements is not specified and may vary between implementations.
    """
    return _cur_framework(x).unique_values(x)


def unique_counts(x: Union[ivy.Array, ivy.NativeArray])\
                -> Tuple[ivy.Array, ivy.Array]:
    """
    Returns the unique elements of an input array x and the corresponding counts for each unique element in x.

    :param x: input array. If x has more than one dimension, the function must flatten x and return the unique elements of the flattened array.
    :return: a namedtuple (values, counts) whose
            -first element must have the field name values and must be an array containing the unique elements of x. The array must have the same data type as x.
            -second element must have the field name counts and must be an array containing the number of times each unique element occurs in x. The returned array must have same shape as values and must have the default array index data type.
    """
    return _cur_framework(x).unique_counts(x)
