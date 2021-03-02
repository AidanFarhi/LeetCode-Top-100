public class ReverseString {
    /*
    Write a function that reverses a string. 
    The input string is given as an array of characters char[].
    Do not allocate extra space for another array, 
    you must do this by modifying the input array in-place with O(1) extra memory.
    You may assume all the characters consist of printable ascii characters.
    */
    public static void reverseString(char[] s) {
        int i = 0;              // pointer to front of arr
        int j = s.length - 1;   // pointer to end of arr
        while (i < j) {         // algorithm ends when pointers cross
            char t = s[i];      // store a temp char
            s[i] = s[j];        // swap elements
            s[j] = t;   
            ++i;                // move i > in arr (pre-increment for speed boost)
            --j;                // move j < in arr (pre-increment for speed boost)
        }
    }
}