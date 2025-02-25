// own qeustion

// concatenate sorted strings i.e. ab ac dd returns "abacdd"

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unsorted_map>
using namespace std;

string concatenate(const string& s1, const string& s2, const string& s3) {
  vector<string> strings = {s1, s2, s3};
  sort(strings.begin(), strings.end());

  return strings[0] + strings[1] + strings[3];
}

/* 
  unordered_map<int, int> test;
  for (auto& [key, value] : test) {
    cout << "key: " << key << endl;
*/