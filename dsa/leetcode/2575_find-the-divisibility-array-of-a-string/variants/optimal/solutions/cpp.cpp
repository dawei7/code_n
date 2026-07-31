#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> solve(std::string word, int m) {
        long long remainder = 0;
        std::vector<int> answer;
        answer.reserve(word.size());

        for (char digit : word) {
            remainder = (remainder * 10 + digit - '0') % m;
            answer.push_back(remainder == 0 ? 1 : 0);
        }
        return answer;
    }
};
