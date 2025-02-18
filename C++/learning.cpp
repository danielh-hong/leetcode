#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <string>
#include <list>       // for LRUCache list
#include <unordered_map> // for LRUCache unordered_map
using namespace std;

/*
 This file contains 30 small C++ snippets that simulate typical LeetCode-style problems.
 Each function is self-contained and demonstrates different C++ syntax and algorithms.
*/

// 1) Print Hello World: basic syntax and output using cout
void helloWorld() {
  cout << "Hello World\n"; // Output Hello World with newline
}

// 2) Two Sum: find two numbers in a vector that add up to a given target
vector<int> twoSum(vector<int>& nums, int target) {
  vector<int> ans; // To store the indices of the found numbers
  // Check every pair of numbers with nested loops
  for (int i = 0; i < nums.size(); i++) {
    for (int j = i + 1; j < nums.size(); j++) {
      if (nums[i] + nums[j] == target) {
        ans.push_back(i); // found first index
        ans.push_back(j); // found second index
        return ans; // return immediately once found
      }
    }
  }
  return ans; // return empty vector if no pair exists
}

// 3) Reverse a string in-place using the two-pointer technique
void reverseString(vector<char>& s) {
  int left = 0, right = (int)s.size() - 1;
  // Swap characters while moving towards the center
  while (left < right) {
    char temp = s[left];
    s[left++] = s[right];
    s[right--] = temp;
  }
}

// 4) Factorial: calculate factorial recursively
long long factorial(int n) {
  if (n <= 1) return 1;  // Base case: factorial of 0 or 1
  return n * factorial(n - 1);  // Multiply current number with factorial of previous
}

// 5) Fibonacci: calculate Fibonacci number recursively
long long fib(int n) {
  if(n <= 1) return n;  // Base cases: fib(0)=0; fib(1)=1
  return fib(n-1) + fib(n-2);
}

/* 6) Check palindrome (string), using two-pointer */
bool isPalindrome(string s) {
  int left=0, right=(int)s.size()-1;
  while(left<right){
    if(s[left++]!=s[right--]) return false;
  }
  return true;
}

/* 7) Merge two sorted vectors, using pointers */
vector<int> mergeSortedArrays(const vector<int>& a, const vector<int>& b){
  vector<int> ans; 
  int i=0, j=0;
  while(i<a.size() && j<b.size()){
    if(a[i]<b[j]) ans.push_back(a[i++]);
    else ans.push_back(b[j++]);
  }
  while(i<a.size()) ans.push_back(a[i++]);
  while(j<b.size()) ans.push_back(b[j++]);
  return ans;
}

/* 8) Binary Search in sorted vector */
int binarySearch(const vector<int>& arr, int target){
  int left=0, right=(int)arr.size()-1;
  while(left<=right){
    int mid=left+(right-left)/2;
    if(arr[mid]==target) return mid;
    else if(arr[mid]<target) left=mid+1;
    else right=mid-1;
  }
  return -1;
}

/* 9) Sort a vector using std::sort (quick sort internally) */
void sortVector(vector<int>& arr){
  sort(arr.begin(), arr.end());
}

/* 10) Remove duplicates from sorted array, return new length */
int removeDuplicates(vector<int>& nums){
  int n=nums.size();
  if(n<2) return n;
  int j=0;
  for(int i=1;i<n;i++){
    if(nums[i]!=nums[j]){
      j++;
      nums[j]=nums[i];
    }
  }
  return j+1;
}

/* 11) Longest Common Prefix (strings) */
string longestCommonPrefix(vector<string>& strs){
  if(strs.empty()) return "";
  string prefix=strs[0];
  for(int i=1;i<strs.size();i++){
    while(strs[i].find(prefix)!=0){
      prefix=prefix.substr(0,prefix.size()-1);
      if(prefix.empty()) return "";
    }
  }
  return prefix;
}

/* 12) Rotate array k steps to the right */
void rotateArray(vector<int>& nums, int k){
  k %= nums.size();
  reverse(nums.begin(), nums.end());
  reverse(nums.begin(), nums.begin()+k);
  reverse(nums.begin()+k, nums.end());
}

/* 13) Single Number (every element appears twice except one) */
int singleNumber(vector<int>& nums){
  int ans=0; 
  for(int x: nums) ans^=x; 
  return ans;
}

/* 14) Valid Parentheses using stack */
bool isValidParentheses(string s){
  stack<char> st;
  for(char c: s){
    if(c=='(' || c=='{' || c=='[') st.push(c);
    else{
      if(st.empty()) return false;
      if(c==')' && st.top()!='(') return false;
      if(c=='}' && st.top()!='{') return false;
      if(c==']' && st.top()!='[') return false;
      st.pop();
    }
  }
  return st.empty();
}

/* 15) Climbing Stairs (ways to climb, classic DP) */
int climbStairs(int n){
  if(n<=2) return n;
  int a=1,b=2;
  for(int i=3;i<=n;i++){
    int c=a+b;
    a=b; b=c;
  }
  return b;
}

/* 16) Merge Intervals, simplified version */
vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals){
  if(intervals.empty()) return {};
  sort(intervals.begin(), intervals.end());
  vector<vector<int>> ans{intervals[0]};
  for(int i=1;i<intervals.size();i++){
    auto &top=ans.back();
    if(intervals[i][0]<=top[1]){
      top[1]=max(top[1], intervals[i][1]);
    }else{
      ans.push_back(intervals[i]);
    }
  }
  return ans;
}

/* 17) Maximum Subarray (Kadane's) */
int maxSubArray(vector<int>& nums){
  int best=nums[0], curr=nums[0];
  for(int i=1;i<nums.size();i++){
    curr=max(nums[i], curr+nums[i]);
    best=max(best,curr);
  }
  return best;
}

/* 18) Move Zeroes to the end, maintain order */
void moveZeroes(vector<int>& nums){
  int pos=0;
  for(int i=0;i<nums.size();i++){
    if(nums[i]!=0) swap(nums[i], nums[pos++]);
  }
}

/* 19) Reverse Linked List (simple structure) */
struct ListNode {
  int val;
  ListNode* next;
  ListNode(int x):val(x),next(nullptr){}
};
ListNode* reverseList(ListNode* head){
  ListNode* prev=nullptr;
  while(head){
    ListNode* temp=head->next;
    head->next=prev;
    prev=head;
    head=temp;
  }
  return prev;
}

/* 20) Inorder Traversal (binary tree, recursion) */
struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x): val(x), left(nullptr), right(nullptr){}
};
void inorder(TreeNode* root, vector<int>& ans){
  if(!root) return;
  inorder(root->left, ans);
  ans.push_back(root->val);
  inorder(root->right, ans);
}

/* 21) BFS Level Order Traversal (binary tree) */
vector<vector<int>> levelOrder(TreeNode* root){
  vector<vector<int>> ans;
  if(!root) return ans;
  queue<TreeNode*>q; q.push(root);
  while(!q.empty()){
    int sz=q.size();
    vector<int> level;
    while(sz--){
      auto node=q.front(); q.pop();
      level.push_back(node->val);
      if(node->left) q.push(node->left);
      if(node->right) q.push(node->right);
    }
    ans.push_back(level);
  }
  return ans;
}

/* 22) DFS (preorder) on binary tree recursively */
void preorder(TreeNode* root, vector<int>& ans){
  if(!root) return;
  ans.push_back(root->val);
  preorder(root->left, ans);
  preorder(root->right, ans);
}

/* 23) Postorder Traversal (binary tree) */
void postorder(TreeNode* root, vector<int>& ans){
  if(!root) return;
  postorder(root->left, ans);
  postorder(root->right, ans);
  ans.push_back(root->val);
}

/* 24) Search 2D matrix (row/col sorted) */
bool searchMatrix(vector<vector<int>>& matrix, int target){
  if(matrix.empty()) return false;
  int r=0, c=matrix[0].size()-1;
  while(r<matrix.size() && c>=0){
    if(matrix[r][c]==target) return true;
    else if(matrix[r][c]>target) c--;
    else r++;
  }
  return false;
}

/* 25) Two-pointer sum in sorted array (like a pair sum) */
bool pairSumSorted(vector<int>& arr, int target){
  int left=0, right=arr.size()-1;
  while(left<right){
    int sum=arr[left]+arr[right];
    if(sum==target) return true;
    else if(sum<target) left++;
    else right--;
  }
  return false;
}

/* 26) Generate all subsets (backtracking) */
void backtrackSubsets(vector<int>& nums,int start,vector<int>&temp,vector<vector<int>>&ans){
  ans.push_back(temp);
  for(int i=start;i<nums.size();i++){
    temp.push_back(nums[i]);
    backtrackSubsets(nums, i+1, temp, ans);
    temp.pop_back();
  }
}
vector<vector<int>> subsets(vector<int>& nums){
  vector<vector<int>> ans;
  vector<int> temp;
  backtrackSubsets(nums,0,temp,ans);
  return ans;
}

/* 27) Permutations (backtracking) */
void permuteHelper(vector<int>& nums, int idx, vector<vector<int>>& ans){
  if(idx==(int)nums.size()){
    ans.push_back(nums);
    return;
  }
  for(int i=idx;i<nums.size();i++){
    swap(nums[idx], nums[i]);
    permuteHelper(nums, idx+1, ans);
    swap(nums[idx], nums[i]);
  }
}
vector<vector<int>> permute(vector<int>& nums){
  vector<vector<int>> ans;
  permuteHelper(nums,0,ans);
  return ans;
}

/* 28) Combination Sum (backtracking) */
void comboSumHelper(vector<int>& candidates,int target,int start,vector<int>&temp,vector<vector<int>>&ans){
  if(target<0) return;
  if(target==0){ ans.push_back(temp); return; }
  for(int i=start;i<candidates.size();i++){
    temp.push_back(candidates[i]);
    comboSumHelper(candidates,target-candidates[i],i,temp,ans);
    temp.pop_back();
  }
}
vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
  vector<vector<int>> ans; vector<int> temp;
  comboSumHelper(candidates,target,0,temp,ans);
  return ans;
}

/* 29) Kth Largest Element (quickselect simplified) */
int findKthLargest(vector<int>& nums, int k){
  sort(nums.begin(), nums.end());
  return nums[nums.size()-k];
}

/* 30) LRU Cache (basic structure, no advanced library usage) */
class LRUCache {
public:
  int cap;
  list<pair<int,int>> lst; 
  // Key -> pointer
  unordered_map<int, list<pair<int,int>>::iterator> mp;
  LRUCache(int capacity) { cap=capacity; }
  
  int get(int key) {
    if(mp.find(key)==mp.end()) return -1;
    auto it=mp[key];
    int val=it->second;
    lst.erase(it);
    lst.push_front({key,val});
    mp[key]=lst.begin();
    return val;
  }
  
  void put(int key, int value) {
    if(mp.find(key)!=mp.end()){
      auto it=mp[key];
      lst.erase(it);
    } else if(lst.size()==cap){
      auto last=lst.back().first;
      mp.erase(last);
      lst.pop_back();
    }
    lst.push_front({key,value});
    mp[key]=lst.begin();
  }
};

int main(){
  // Minimal demonstration
  helloWorld();
  vector<int> nums = {2,7,11,15};
  auto ans = twoSum(nums, 9);
  if(!ans.empty()) cout << ans[0] << " " << ans[1] << "\n";
  return 0;
}