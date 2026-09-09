class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set numbers = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            if (!numbers.add(nums[i]))
                return true;
        }
        return false;
        
    }
}
