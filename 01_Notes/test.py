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

