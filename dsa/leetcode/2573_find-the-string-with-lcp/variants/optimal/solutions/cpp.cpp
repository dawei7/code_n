#include <string>
#include <vector>

class Solution {
public:
std::string solve(std::vector<std::vector<int>> lcp) {
    const int n = static_cast<int>(lcp.size());
    std::string word(n, '\0');
    char next_letter = 'a';

    for (int i = 0; i < n; ++i) {
        if (word[i] != '\0') {
            continue;
        }
        if (next_letter > 'z') {
            return "";
        }
        for (int j = i; j < n; ++j) {
            if (lcp[i][j] > 0) {
                word[j] = next_letter;
            }
        }
        ++next_letter;
    }

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            int expected = 0;
            if (word[i] == word[j]) {
                expected = 1;
                if (i + 1 < n && j + 1 < n) {
                    expected += lcp[i + 1][j + 1];
                }
            }
            if (lcp[i][j] != expected) {
                return "";
            }
        }
    }
    return word;
}
};
