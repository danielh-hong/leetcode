#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++) {
            auto pt = mp.find(target - nums[i]);
            if (pt != mp.end()) return {i, pt->second};
            mp.emplace(nums[i], i);
        }

        return {};
    }
};

/* 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        unordered_map<int, int> seen;
        for(int i = 0; i < nums.size(); i++) {
            auto found = seen.find(target - nums[i]);
            if (found != seen.end()) {
                // ret.push_back(i);
                // ret.push_back((*found).second);
                return {found->second, i};
            }
            // seen[nums[i]] = i;
            seen.emplace(nums[i], i);	
        }
        return {}; // Return empty vector if no solution is found

    }
};
*/