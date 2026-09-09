class Solution {
    public boolean isPalindrome(String s) {

        String w = s.toLowerCase();
        int stringLength = w.length() - 1;
        int j = w.length() - 1;

        if (j <= 0) {
            return true;
        }

        while (!Character.isLetter(w.charAt(j)) && !Character.isDigit(w.charAt(j))) {
            j--;
            stringLength--;
            if (j <= 0) {
                return true;
            }
        }

        System.out.println(j);

        for (int i = 0; i <= stringLength / 2; i++) {
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

            System.out.println("i: " + iChar + " j: " + jChar);

            if (iChar != jChar) {
                return false;
            }
            j--;
        }
        return true;
    }
}
