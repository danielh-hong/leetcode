#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
  public:
      bool containsNearbyDuplicate(vector<int>& nums, int k) {
          unordered_map<int, int> seen; // value, index
          for (int i = 0; i < nums.size(); i++) {
              if (seen.count(nums[i]) && (i - seen[nums[i]]) <= k) {
                  cout << "indices " << seen[nums[i]] << " AND " << i << "\n"; // new line is that way because it's like n is SLIDING down! Also cout is << since we're putting it
                                                                         // into character out!
                  cout << "(i - seen[i]) " << (i - seen[i]);
                  return true;
              }
              seen[nums[i]] = i;
          }
  
          return false;
      }
  };

class Solution2 {
  public:
  bool containsNearbyDuplicate(vector<int>& nums, int k) {
      unordered_set<int> seen;
      if (k == 1 && nums.size() == 1) return false;
      int max_end = min((int)k, (int)nums.size() - 1);
      for(int i = 0; i <= max_end; i++) {
          if (seen.find(nums[i]) != seen.end()) return true;
          seen.insert(nums[i]);
      }

      for(int i = k + 1; i < nums.size(); i++) {
          seen.erase(nums[i - (k + 1)]);
          if(seen.find(nums[i]) != seen.end()) return true;
          seen.insert(nums[i]);
      }

      return false;
  }
};