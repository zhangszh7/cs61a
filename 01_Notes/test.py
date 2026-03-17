# def tree(label, branches=[]):
#     """Construct a tree with the given label value and a list of branches."""
#     if change_abstraction.changed:
#         for branch in branches:
#             assert is_tree(branch), 'branches must be trees'
#         return {'label': label, 'branches': list(branches)}
#     else:
#         for branch in branches:
#             assert is_tree(branch), 'branches must be trees'
#         return [label] + list(branches)

# def label(tree):
#     """Return the label value of a tree."""
#     if change_abstraction.changed:
#         return tree['label']
#     else:
#         return tree[0]

# def branches(tree):
#     """Return the list of branches of the given tree."""
#     if change_abstraction.changed:
#         return tree['branches']
#     else:
#         return tree[1:]

# def is_tree(tree):
#     """Returns True if the given tree is a tree, and False otherwise."""
#     if change_abstraction.changed:
#         if type(tree) != dict or len(tree) != 2:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True
#     else:
#         if type(tree) != list or len(tree) < 1:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True

# def is_leaf(tree):
#     """Returns True if the given tree's list of branches is empty, and False
#     otherwise.
#     """
#     return not branches(tree)

# def change_abstraction(change):
#     change_abstraction.changed = change

# change_abstraction.changed = False




# def prune_binary(t, nums):
#     if is_leaf(t):
#         if True in [label(t) == num for num in nums]:
#             return t
#         return None
#     else:
#         next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
#         new_branches = []
#         for b in branches(t):
#             pruned_branch = prune_binary(b, next_valid_nums)
#             if pruned_branch is not None:
#                 new_branches = new_branches + [pruned_branch]
#         if not new_branches:
#             return None
#         return tree(label(t), new_branches)

# t = tree('1', [tree('0', [tree('0'), tree('1')]), 
#              tree('1', [tree('0')])])
# print(t)
# print(prune_binary(t, ['01', '110', '100']))



# def combo(a, b):
#     """
#     >>> combo(1234, 9123)
#     91234
#     """
#     if a * b == 0:
#         return a + b
#     elif a % 10 == b % 10:
#         return combo(a // 10, b // 10) * 10 + a % 10

#     return min(combo(a//10, b)*10 + a%10, combo(a, b//10 )* 10 + b %10)


from operator import mul

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
            
    def is_leaf(self):
        return not self.branches



def find_paths(t, entry):

    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """

    branches = []
    for b1, b2 in zip(t1.branches, t2.branches): 
        branches.append(combine_tree(b1, b2, combiner) )
    
    return Tree(combiner(t1.label, t2.label), branches)