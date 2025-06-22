class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        
        while (i < j) {
            // Move i to next alphanumeric or beyond
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                i++;
            }
            // Move j to previous alphanumeric or before
            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                j--;
            }
            // Compare characters ignoring case
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
            i++;
            j--;
        }
        
        return true;
    }
}
