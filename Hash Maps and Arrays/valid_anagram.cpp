#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

/* 
class Solution {
  public:
      bool isAnagram(string s, string t) {
          if (s.size() != t.size()) return false;
  
          unordered_map<char, int> letters;
          for (char c : s) {
              if (letters.find(c) == letters.end()) {
                  letters[c] = 0;
              }
              letters[c]++;
          }
          for (char c : t) {
              if (letters.find(c) == letters.end()) {
                  return false;
              }
              else if (--letters[c] < 0) {
                  return false;
              }
              // letters[c]--;
              // --letters[c] already decrements
          }
          return true;
      }
  };
*/


class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> count;
        for (int i = 0; i < s.size(); i++) {
            count[s[i]]++;
            count[t[i]]--;
        }

        // so when we do (iterator : iterable), the iterator holds the ACTUAL thing. It's the ACTUAL object.
        // also the iterator is NOT ACTUALLY an iterator in this case it's just the actual object of the thing each time.
        for (auto& key : count) { // count` stores `{char, int}`, not just `char` so cant do char key
            // if (key.second != 0) return false;
            if (key.second) return false;
          }
        return true;
    }
};