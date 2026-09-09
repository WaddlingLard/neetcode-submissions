class Solution {
    public boolean isPalindrome(String s) {

        String w = s.toLowerCase();
        int j = w.length() - 1;
        int i = 0;

        while (!Character.isLetter(w.charAt(j)) && !Character.isDigit(w.charAt(j))) {
            j--;
            if (j <= 0) {
                return true;
            }
        }

        while (i < j) {
            char iChar, jChar;
            iChar = w.charAt(i);
            jChar = w.charAt(j);

            while (!Character.isLetter(iChar) && !Character.isDigit(iChar)) {
                i++;
                iChar = w.charAt(i);
            } 

            while (!Character.isLetter(jChar) && !Character.isDigit(jChar)) {
                j--;
                jChar = w.charAt(j);
            }

            if (iChar != jChar) {
                return false;
            }
            
            j--;
            i++;
        }
        return true;
    }
}
