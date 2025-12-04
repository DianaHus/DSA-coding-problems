package dp.leetcode.medium;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int max_lis = 0;
        int[] lengths = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int max = 0;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[i]) {
                    if (lengths[j] > max) {
                        max = lengths[j];
                    }
                }
            }
            lengths[i] = 1 + max;
            if (lengths[i] > max_lis) {
                max_lis = lengths[i];
            }
        }
        return max_lis;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = { 10, 9, 2, 5, 3, 7, 101, 18 };
        int res = sol.lengthOfLIS(nums);
        System.out.println(res); // Output: 4
    }
}