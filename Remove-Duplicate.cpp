class Solution {
public:
    string removeDuplicateLetters(string s) {
        int len = s.size();
        string result = "";
        vector<int> lastOccurrence(26, -1); // Store the last occurrence index of each character
        vector<bool> inStack(26, false); // Keep track of characters in the stack
        stack<char> charStack; // Stack to build the result

        // Find the last occurrence index of each character in the string
        for (int i = 0; i < len; i++) {
            lastOccurrence[s[i] - 'a'] = i;
        }

        for (int i = 0; i < len; i++) {
            char c = s[i];

            // Skip if the character is already in the stack
            if (inStack[c - 'a']) {
                continue;
            }

            // Pop characters from the stack if:
            // 1. The current character is smaller and there are more occurrences left in the string.
            // 2. The top of the stack is not the last occurrence.
            while (!charStack.empty() && c < charStack.top() && lastOccurrence[charStack.top() - 'a'] > i) {
                inStack[charStack.top() - 'a'] = false;
                charStack.pop();
            }

            // Push the current character onto the stack
            charStack.push(c);
            inStack[c - 'a'] = true;
        }

        // Build the result string from the stack
        while (!charStack.empty()) {
            result = charStack.top() + result;
            charStack.pop();
        }

        return result;
    }
};
