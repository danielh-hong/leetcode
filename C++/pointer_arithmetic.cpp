#include <iostream>
#include <vector>
#include <map>
#include <list>
using namespace std;

int main() {
    // Regular array pointer arithmetic
    int arr[] = {1, 2, 3, 4};
    int* ptr = arr;
    cout << "Array element: " << *ptr << endl;
    ptr++;
    cout << "After ptr++: " << *ptr << endl;

    // Vector example
    vector<int> vec = {1, 2, 3, 4};
    auto vec_it = vec.begin();
    cout << "Vector element: " << *vec_it << endl;
    vec_it++;
    cout << "After vec_it++: " << *vec_it << endl;

    // Map example
    map<string, int> mp = {{"foo", 1}, {"bar", 2}};
    auto map_it = mp.begin();
    cout << "Map element: " << map_it->first << ":" << map_it->second << endl;

    // List example
    list<int> lst = {1, 2, 3, 4};
    auto list_it = lst.begin();
    cout << "List element: " << *list_it << endl;

    return 0;
}