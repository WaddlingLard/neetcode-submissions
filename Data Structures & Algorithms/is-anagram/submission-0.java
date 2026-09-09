class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] sAlphabet = new int[26];
        int[] tAlphabet = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sAlphabet[s.charAt(i) - 97]++;
            tAlphabet[t.charAt(i) - 97]++;
        }
        for (int i = 0; i < sAlphabet.length; i++) {
            if (sAlphabet[i] != tAlphabet[i]) {
                return false;
            }

        }

        
        return true;
    }
}
