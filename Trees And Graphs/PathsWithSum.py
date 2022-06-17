# 4.12 - You are given a binary tree in which each node contains an integer value (which might be positive or negative).
# Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end
# at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
import typing
from collections import defaultdict

from utils.collections.tree import BinaryTree

T = typing.TypeVar('T', bound=int)
"""
O(NH) SOLUTION IN TIME AND O(H) IN MEMORY
def _path_sum(root: Optional[TreeNode], target_sum: int, sums: Sequence[int]):
    sums_count = 0
    
    i = 0
    sums.append(0)
    while i < len(sums):
        sums[i] += root.val
        if sums[i] == target_sum:
            sums_count += 1
        i += 1
    
    if root.left is not None:
        sums_count += _path_sum(root.left, target_sum, sums[:]) 
    if root.right is not None:
        sums_count += _path_sum(root.right, target_sum, sums[:]) 
        
    return sums_count 
        

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return _path_sum(root, targetSum, []) if root is not None else 0

"""


# O(n) in time and O(h) in memory
def paths_with_sum(root: BinaryTree[T] | None, target_sum: T, running_sum: T = 0, path_count: typing.Dict[T, int] = None) -> int:
    if root is None:
        return 0

    if path_count is None:
        path_count = defaultdict(int)
        path_count[0] = 1  # the root

    running_sum += root.value
    # How many paths exist that would get to the sum I need?
    start_of_path = running_sum - target_sum
    sums = path_count.get(start_of_path, 0)

    path_count[running_sum] += 1

    sums += paths_with_sum(root.left, target_sum, running_sum, path_count)
    sums += paths_with_sum(root.right, target_sum, running_sum, path_count)

    path_count[running_sum] -= 1
    if path_count[running_sum] == 0:
        del path_count[running_sum]

    return sums

