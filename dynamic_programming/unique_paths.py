class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Constraints: 1 <= m, n <= 100
        unique_paths = [[1] * n] * m

        for row in range(1, m):
            for col in range(1, n):
                unique_paths[row][col] = unique_paths[row - 1][col] + unique_paths[row][col - 1]

        return unique_paths[-1][-1]


if __name__ == '__main__':
    m, n = 2, 3
    sol_obj = Solution()
    paths = sol_obj.uniquePaths(m, n)
    print(paths)