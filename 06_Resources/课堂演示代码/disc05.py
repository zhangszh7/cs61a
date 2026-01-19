def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """


def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """



def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """

    if _____________________________:

        return _____________________________

    _____________________________:

        path = _____________________________

        if _____________________________:

            return _____________________________




def prune_binary(t, nums):
  if _________________________:
    if _____________:
      return t
    return None
  else:
    next_valid_nums = __________________________
    new_branches = []
    for ____________________:
      pruned_branch = prune_binary(_____, next_valid_nums)
      if pruned_branch is not None:
        new_branches = new_branches + [__________]
    if not new_branches:
      return None
    return ______________________________


