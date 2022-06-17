# https://leetcode.com/problems/binary-tree-cameras/


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras, color_last_level, is_root_covered = self._minCameraCover(root)
        if not is_root_covered:
            cameras += 1
        return cameras

    def _minCameraCover(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root is None:
            return 0, False, True

        if root.left is None and root.right is None:
            return 0, False, False

        left, did_left_color_on_last_level, was_left_covered = self._minCameraCover(root.left)
        right, did_right_color_on_last_level, was_right_covered = self._minCameraCover(root.right)

        if not was_left_covered or not was_right_covered:
            return left + right + 1, True, True

        if did_left_color_on_last_level or did_right_color_on_last_level:
            return left + right, False, True

        return left + right, False, False
