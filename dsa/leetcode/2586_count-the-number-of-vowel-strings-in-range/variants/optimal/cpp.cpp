#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<string> words, int left, int right) {
        int count = 0;
        for (int index = left; index <= right; ++index) {
            const string& word = words[index];
            if (isVowel(word.front()) && isVowel(word.back())) {
                ++count;
            }
        }
        return count;
    }

private:
    static bool isVowel(char value) {
        return value == 'a' || value == 'e' || value == 'i' ||
               value == 'o' || value == 'u';
    }
};
