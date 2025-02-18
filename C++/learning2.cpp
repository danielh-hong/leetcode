/******************************************************************************/
// C++ Crash Course + 40 LeetCode-Style Problems & Solutions
// All in ONE code block, with brief explanations.
// NOTE: In actual practice, you'd typically keep each solution in a separate file
// or use different functions/classes. Here, everything is combined for illustration.
//
// Basic C++ Syntax Overview:
// 1. #include <iostream> (or other headers like vector, algorithm, etc.) is used to
//    include standard libraries.
// 2. using namespace std; to avoid typing std:: repeatedly (though in production
//    code, using namespace std; is often discouraged).
// 3. int main() { ... } is the entry point of a C++ program.
// 4. We can define functions outside main() or inside classes.
// 5. Common data structures in <vector>, <string>, <algorithm> etc.
// 6. For loops: for(int i = 0; i < n; i++) { ... }
// 7. While loops: while(condition) { ... }
// 8. Two-pointer approach: often used when array/list is sorted or partially sorted.
// 9. Recursion: a function calling itself, watch for base conditions.
// 10. Sorting: #include <algorithm> => sort(vec.begin(), vec.end());
//
// We'll demonstrate a variety of solutions below. 
// Each solution is placed in a function for clarity.
// You can call these functions in main() as needed.
//
// This code is for demonstration/learning purposes and may not be 
// individually runnable all at once without adjustments.
// We'll keep each solution's code minimal and provide a short explanation.
//
// Let's begin!
/******************************************************************************/

#include <bits/stdc++.h> // For convenience, though <bits/stdc++.h> is non-standard
using namespace std;

/******************************************************************************/
/* 1) Two Sum
   Given an array of integers nums and an integer target, return indices of the
   two numbers such that they add up to target.
   Approach:
   - We can use a hash map that stores value -> index.
   - While iterating, check if (target - current_value) is in the map.
   - If yes, we found our solution.
   - Time complexity: O(n) */
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int,int> mp;
    for(int i = 0; i < (int)nums.size(); i++){
        int complement = target - nums[i];
        if(mp.find(complement) != mp.end()){
            return {mp[complement], i};
        }
        mp[nums[i]] = i;
    }
    return {}; // No valid answer
}

/******************************************************************************/
/* 2) Reverse Integer
   Given a signed 32-bit integer x, return x with its digits reversed. 
   If reversing x causes overflow, return 0.
   Approach:
   - Pop digits from x and build the reversed number, checking for overflow.
   - Time complexity: O(log(x)) */
int reverseInteger(int x) {
    long rev = 0;
    while(x != 0) {
        int digit = x % 10;
        x /= 10;
        rev = rev * 10 + digit;
        if(rev > INT_MAX || rev < INT_MIN) return 0; // Overflow check
    }
    return (int)rev;
}

/******************************************************************************/
/* 3) Palindrome Number
   Check if an integer is a palindrome.
   Approach:
   - Convert to string, or reverse half. We'll do the string approach.
   - Time complexity: O(log(n)) or O(n) for string length. */
bool isPalindromeNumber(int x) {
    if(x < 0) return false;
    string s = to_string(x);
    int l = 0, r = s.size() - 1;
    while(l < r) {
        if(s[l++] != s[r--]) return false;
    }
    return true;
}

/******************************************************************************/
/* 4) Valid Parentheses
   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
   determine if the input string is valid.
   Approach:
   - Use a stack: push opening brackets, pop and check for matching closing bracket.
   - Time complexity: O(n) */
bool isValidParentheses(string s) {
    stack<char> st;
    for(char c: s){
        if(c == '(' || c == '{' || c == '['){
            st.push(c);
        } else {
            if(st.empty()) return false;
            char top = st.top(); 
            st.pop();
            if((c == ')' && top != '(') ||
               (c == '}' && top != '{') ||
               (c == ']' && top != '[')) {
                return false;
            }
        }
    }
    return st.empty();
}

/******************************************************************************/
/* 5) Merge Two Sorted Lists
   Merge two sorted linked lists and return it as a sorted list.
   Basic singly-linked list structure: */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while(l1 && l2){
        if(l1->val < l2->val){
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    if(l1) tail->next = l1;
    if(l2) tail->next = l2;
    return dummy.next;
}

/******************************************************************************/
/* 6) Maximum Subarray (Kadane's Algorithm)
   Find the contiguous subarray which has the largest sum.
   Approach:
   - Keep track of current sum and max sum, reset if current sum < 0.
   - Time complexity: O(n) */
int maxSubArray(vector<int>& nums) {
    int currSum = 0, maxSum = INT_MIN;
    for(int n: nums){
        currSum += n;
        maxSum = max(maxSum, currSum);
        if(currSum < 0) currSum = 0;
    }
    return maxSum;
}

/******************************************************************************/
/* 7) Climbing Stairs
   You can climb 1 or 2 steps at a time. How many distinct ways to climb n steps?
   Approach: 
   - Fib-like dynamic programming: ways[n] = ways[n-1] + ways[n-2].
   - Time complexity: O(n) */
int climbStairs(int n) {
    if(n <= 2) return n;
    int a = 1, b = 2;
    for(int i=3; i<=n; i++){
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}

/******************************************************************************/
/* 8) Maximum Depth of Binary Tree
   Given a binary tree, find its maximum depth.
   Approach:
   - Recursively find max depth: 1 + max(depth(left), depth(right)). */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int maxDepth(TreeNode* root) {
    if(!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

/******************************************************************************/
/* 9) Same Tree
   Given two binary trees, check if they are the same (identical structure & values).
   Approach:
   - Recursively check if p->val == q->val and subtrees are same. */
bool isSameTree(TreeNode* p, TreeNode* q) {
    if(!p && !q) return true;
    if(!p || !q) return false;
    if(p->val != q->val) return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

/******************************************************************************/
/* 10) Symmetric Tree
   Check if a binary tree is symmetric around its center.
   Approach:
   - Check mirror of left & right subtrees recursively. */
bool isMirror(TreeNode* left, TreeNode* right){
    if(!left && !right) return true;
    if(!left || !right) return false;
    return (left->val == right->val) 
           && isMirror(left->left, right->right)
           && isMirror(left->right, right->left);
}

bool isSymmetric(TreeNode* root) {
    if(!root) return true;
    return isMirror(root->left, root->right);
}

/******************************************************************************/
/* 11) Best Time to Buy and Sell Stock
   Find max profit given an array prices, you can only hold one share at a time.
   Approach:
   - Track min price and compute profit for each day, keep track of max profit. */
int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX;
    int maxP = 0;
    for(int p: prices){
        minPrice = min(minPrice, p);
        maxP = max(maxP, p - minPrice);
    }
    return maxP;
}

/******************************************************************************/
/* 12) Invert Binary Tree
   Invert a binary tree (mirror it).
   Approach:
   - Swap left and right recursively. */
TreeNode* invertTree(TreeNode* root) {
    if(!root) return NULL;
    TreeNode* temp = root->left;
    root->left = invertTree(root->right);
    root->right = invertTree(temp);
    return root;
}

/******************************************************************************/
/* 13) Merge Sorted Array
   Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
   Approach:
   - Start from the end of both arrays, place the largest at the end of nums1. */
void mergeSortedArray(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m-1, j = n-1, k = m+n-1;
    while(i >= 0 && j >= 0){
        if(nums1[i] > nums2[j]){
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
    while(j >= 0){
        nums1[k--] = nums2[j--];
    }
}

/******************************************************************************/
/* 14) Pascal's Triangle
   Generate the first numRows of Pascal's triangle.
   Approach:
   - Each cell = sum of the two above. */
vector<vector<int>> generate(int numRows) {
    vector<vector<int>> res(numRows);
    for(int i=0; i<numRows; i++){
        res[i].resize(i+1);
        res[i][0] = res[i][i] = 1;
        for(int j=1; j<i; j++){
            res[i][j] = res[i-1][j-1] + res[i-1][j];
        }
    }
    return res;
}

/******************************************************************************/
/* 15) Pascal's Triangle II
   Given rowIndex, return the row of Pascal's triangle.
   Approach:
   - Same idea, or do it in O(rowIndex) space. */
vector<int> getRow(int rowIndex) {
    vector<int> row(rowIndex+1,0);
    row[0] = 1;
    for(int i=1; i<=rowIndex; i++){
        for(int j=i; j>0; j--){
            row[j] += row[j-1];
        }
    }
    return row;
}

/******************************************************************************/
/* 16) Move Zeroes
   Given an array nums, move all 0's to the end while maintaining the relative order.
   Approach:
   - Use two-pointer: one pointer to place non-zero elements. */
void moveZeroes(vector<int>& nums) {
    int pos = 0;
    for(int i=0; i<(int)nums.size(); i++){
        if(nums[i] != 0){
            nums[pos++] = nums[i];
        }
    }
    while(pos < (int)nums.size()){
        nums[pos++] = 0;
    }
}

/******************************************************************************/
/* 17) Linked List Cycle
   Detect if a linked list has a cycle.
   Approach:
   - Use fast/slow pointer. If fast == slow at some point, there's a cycle. */
bool hasCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast) return true;
    }
    return false;
}

/******************************************************************************/
/* 18) Reverse Linked List
   Reverse a singly linked list.
   Approach:
   - Iterative: keep track of prev, curr, next. */
ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* curr = head;
    while(curr){
        ListNode* nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}

/******************************************************************************/
/* 19) Intersection of Two Linked Lists
   Find the node at which the two lists intersect, or null if they don't intersect.
   Approach:
   - Two pointers: pA on headA, pB on headB, switch to other head when reaching end. */
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if(!headA || !headB) return NULL;
    ListNode* pA = headA;
    ListNode* pB = headB;
    while(pA != pB){
        pA = pA ? pA->next : headB;
        pB = pB ? pB->next : headA;
    }
    return pA;
}

/******************************************************************************/
/* 20) Happy Number
   A happy number is a number defined by repeatedly replacing it with the sum of
   the squares of its digits, until it equals 1 or loops endlessly.
   Approach:
   - Use a set to detect loops. */
int sumOfSquares(int n){
    int sum = 0;
    while(n){
        int d = n % 10;
        sum += d*d;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    unordered_set<int> st;
    while(n != 1 && !st.count(n)){
        st.insert(n);
        n = sumOfSquares(n);
    }
    return n == 1;
}

/******************************************************************************/
/* 21) Fizz Buzz
   Print numbers from 1 to n, but multiples of 3 => "Fizz", 5 => "Buzz", 3&5 => "FizzBuzz". */
vector<string> fizzBuzz(int n) {
    vector<string> ans(n);
    for(int i=1; i<=n; i++){
        if(i%15 == 0) ans[i-1] = "FizzBuzz";
        else if(i%3 == 0) ans[i-1] = "Fizz";
        else if(i%5 == 0) ans[i-1] = "Buzz";
        else ans[i-1] = to_string(i);
    }
    return ans;
}

/******************************************************************************/
/* 22) Count Primes
   Return the number of prime numbers less than a given n.
   Approach:
   - Sieve of Eratosthenes. O(n log log n). */
int countPrimes(int n) {
    if(n < 2) return 0;
    vector<bool> prime(n, true);
    prime[0] = prime[1] = false;
    for(int i=2; i*i<n; i++){
        if(prime[i]){
            for(int j=i*i; j<n; j+=i){
                prime[j] = false;
            }
        }
    }
    return count(prime.begin(), prime.end(), true);
}

/******************************************************************************/
/* 23) Roman to Integer
   Convert a Roman numeral to an integer.
   Approach:
   - Map each symbol to value, add or subtract depending on whether next value is larger. */
int romanToInt(string s) {
    unordered_map<char,int> mp = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
    int result = 0;
    for(int i=0; i<(int)s.size(); i++){
        if(i+1 < (int)s.size() && mp[s[i]] < mp[s[i+1]]){
            result -= mp[s[i]];
        } else {
            result += mp[s[i]];
        }
    }
    return result;
}

/******************************************************************************/
/* 24) Longest Common Prefix
   Write a function to find the longest common prefix string among an array of strings.
   Approach:
   - Compare characters of the first string with all others. */
string longestCommonPrefix(vector<string>& strs) {
    if(strs.empty()) return "";
    for(int i=0; i<(int)strs[0].size(); i++){
        char c = strs[0][i];
        for(int j=1; j<(int)strs.size(); j++){
            if(i >= (int)strs[j].size() || strs[j][i] != c){
                return strs[0].substr(0,i);
            }
        }
    }
    return strs[0];
}

/******************************************************************************/
/* 25) Contains Duplicate
   Given an integer array nums, return true if any value appears at least twice.
   Approach:
   - Use a set or sort. O(n). */
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> s;
    for(int n: nums){
        if(s.find(n) != s.end()) return true;
        s.insert(n);
    }
    return false;
}

/******************************************************************************/
/* 26) Missing Number
   Given an array nums containing n distinct numbers in [0, n], return the only number missing.
   Approach:
   - Sum from 0..n minus sum of array, or XOR approach. */
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int sumExpected = n*(n+1)/2;
    int sumActual = 0;
    for(int x: nums) sumActual += x;
    return sumExpected - sumActual;
}

/******************************************************************************/
/* 27) Power of Two
   Given an integer, return true if it is a power of two.
   Approach:
   - Repeatedly divide by 2 or use n & (n-1) trick. */
bool isPowerOfTwo(int n) {
    if(n <= 0) return false;
    return (n & (n-1)) == 0;
}

/******************************************************************************/
/* 28) Number of 1 Bits
   Return the number of 1 bits in the binary representation of a given integer (unsigned).
   Approach:
   - Brian Kernighan’s Algorithm: n &= (n-1) drops one set bit at a time. */
int hammingWeight(uint32_t n) {
    int count = 0;
    while(n){
        n &= (n-1);
        count++;
    }
    return count;
}

/******************************************************************************/
/* 29) Hamming Distance
   The Hamming distance between two integers is the number of positions at which 
   the corresponding bits are different. */
int hammingDistance(int x, int y) {
    int z = x ^ y, count = 0;
    while(z){
        z &= (z-1);
        count++;
    }
    return count;
}

/******************************************************************************/
/* 30) Reverse Bits
   Reverse the bits of a given 32-bit unsigned integer. */
uint32_t reverseBits(uint32_t n) {
    uint32_t rev = 0;
    for(int i=0; i<32; i++){
        rev <<= 1;
        rev |= (n & 1);
        n >>= 1;
    }
    return rev;
}

/******************************************************************************/
/* 31) Single Number
   Every element appears twice except for one. Find that single one.
   Approach:
   - XOR all elements => result is the unique. */
int singleNumber(vector<int>& nums) {
    int result = 0;
    for(int n: nums){
        result ^= n;
    }
    return result;
}

/******************************************************************************/
/* 32) Excel Sheet Column Number
   Given a column title as appear in an Excel sheet, return its corresponding column number.
   e.g. "A" -> 1, "AB" -> 28.
   Approach:
   - It's essentially a base-26 number system. */
int titleToNumber(string s) {
    long result = 0;
    for(char c: s){
        result = result*26 + (c - 'A' + 1);
    }
    return (int)result;
}

/******************************************************************************/
/* 33) Excel Sheet Column Title
   Given a positive integer, return its corresponding column title as in Excel.
   e.g. 1 -> "A", 28 -> "AB".
   Approach:
   - Repeatedly mod by 26, build from right to left. */
string convertToTitle(int n) {
    string res;
    while(n){
        int r = (n-1) % 26;
        res.push_back(char('A' + r));
        n = (n-1)/26;
    }
    reverse(res.begin(), res.end());
    return res;
}

/******************************************************************************/
/* 34) House Robber
   You cannot rob two adjacent houses. Max amount you can rob.
   Approach:
   - DP: rob[i] = max( rob[i-1], rob[i-2] + nums[i] ). */
int rob(vector<int>& nums) {
    if(nums.empty()) return 0;
    if(nums.size() == 1) return nums[0];
    vector<int> dp(nums.size()+1,0);
    dp[0] = 0;
    dp[1] = nums[0];
    for(int i=2; i<= (int)nums.size(); i++){
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
    }
    return dp[nums.size()];
}

/******************************************************************************/
/* 35) House Robber II
   House in a circle, can't rob the first & last together. 
   Approach:
   - Run house robber twice: once ignoring the first, once ignoring the last, take max. */
int robLine(vector<int>& nums, int start, int end){
    int prev = 0, curr = 0;
    for(int i=start; i<=end; i++){
        int temp = max(curr, prev + nums[i]);
        prev = curr;
        curr = temp;
    }
    return curr;
}
int rob2(vector<int>& nums) {
    int n = nums.size();
    if(n == 1) return nums[0];
    return max(robLine(nums, 0, n-2), robLine(nums, 1, n-1));
}

/******************************************************************************/
/* 36) Majority Element
   Find the majority element that appears more than n/2 times.
   Approach:
   - Boyer-Moore Voting Algorithm. */
int majorityElement(vector<int>& nums) {
    int count=0, candidate=0;
    for(int num: nums){
        if(count == 0) candidate = num;
        count += (num == candidate) ? 1 : -1;
    }
    return candidate;
}

/******************************************************************************/
/* 37) Isomorphic Strings
   Two strings are isomorphic if the characters in s can be replaced to get t.
   Approach:
   - Use two maps or array of size 256, track mapping. */
bool isIsomorphic(string s, string t) {
    if(s.size() != t.size()) return false;
    vector<int> m1(256, -1), m2(256, -1);
    for(int i=0; i<(int)s.size(); i++){
        if(m1[s[i]] != m2[t[i]]) return false;
        m1[s[i]] = i; 
        m2[t[i]] = i;
    }
    return true;
}

/******************************************************************************/
/* 38) Two Sum II - Input Array Is Sorted
   Return indices of the two numbers, array is 1-indexed and sorted.
   Approach:
   - Two pointer from left and right. */
vector<int> twoSum2(vector<int>& numbers, int target) {
    int left = 0, right = numbers.size()-1;
    while(left < right){
        int sum = numbers[left] + numbers[right];
        if(sum == target) return {left+1, right+1};
        else if(sum < target) left++;
        else right--;
    }
    return {};
}

/******************************************************************************/
/* 39) Reverse String
   Write a function that reverses a string in-place.
   Approach:
   - Two pointers, swap. */
void reverseString(vector<char>& s) {
    int left=0, right=s.size()-1;
    while(left<right){
        char tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        left++; right--;
    }
}

/******************************************************************************/
/* 40) Valid Anagram
   Given two strings s and t, write a function to determine if t is an anagram of s.
   Approach:
   - Sort them or count frequency. */
bool isAnagram(string s, string t) {
    if(s.size() != t.size()) return false;
    vector<int> freq(26,0);
    for(char c: s) freq[c - 'a']++;
    for(char c: t){
        freq[c - 'a']--;
        if(freq[c - 'a'] < 0) return false;
    }
    return true;
}

/******************************************************************************/
/* MAIN FUNCTION (for demonstration) */
int main() {
    // You can test the above functions here. For example:
    // 1) Two Sum example
    vector<int> nums = {2,7,11,15};
    int target = 9;
    vector<int> ans = twoSum(nums, target);
    cout << "Two Sum: [" << ans[0] << ", " << ans[1] << "]\n";

    // 2) Reverse Integer example
    cout << "Reverse of 123 is: " << reverseInteger(123) << "\n";

    // 3) Palindrome Number
    cout << "Is 121 a palindrome? " << (isPalindromeNumber(121) ? "Yes":"No") << "\n";

    // ... etc. You can similarly test other functions.

    return 0;
}
