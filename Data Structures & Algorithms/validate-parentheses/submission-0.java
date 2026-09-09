class Solution {
    public boolean isValid(String s) {
               Stack characters = new Stack();
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            if (letter == '(' || letter == '{' || letter == '[') {
                characters.push(s.charAt(i));
            } else {
                if (characters.isEmpty()) {
                    return false;
                }
                char compare = (char) characters.peek();
                switch (letter) {
                    case ')':
                        if (compare == '(') {
                            characters.pop();
                        } else {
                            return false;
                        }
                        break;
                    case '}':
                        if (compare == '{') {
                            characters.pop();
                        } else {
                            return false;
                        }
                        break;
                    case ']':
                        if (compare == '[') {
                            characters.pop();
                        } else {
                            return false;
                        }
                        break;
                }
            }
        }

        return characters.isEmpty();    
    }
}
