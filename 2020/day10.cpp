#include <iostream>
#include <iterator>
#include <vector>
#include <cstdlib>
#include <array>

using namespace std;


constexpr std::array<int, 102> data = {1, 2, 3, 4, 7, 10, 11, 12, 15, 16, 17, 18, 19, 22, 25, 26, 27, 28, 31, 32, 35, 38, 39, 40, 41, 44, 45, 46, 47, 48, 51, 54, 55, 56, 57, 60, 63, 64, 65, 66, 69, 70, 71, 72, 75, 78, 79, 82, 83, 84, 85, 86, 89, 90, 91, 92, 95, 98, 99, 100, 103, 104, 105, 108, 109, 110, 113, 114, 115, 118, 119, 120, 121, 122, 125, 126, 127, 128, 129, 132, 133, 134, 135, 138, 139, 142, 143, 144, 147, 150, 151, 152, 153, 154, 157, 158, 159, 160, 161, 164, 167, 168};
constexpr int back_max = 168;

vector<int> combination;
long int total_combinations = 0;
long int new_conbinations = 0;

void go(int offset, int k) {
  if (k == 0) {
    // check the combination
    if (combination[0] > 3)
        return;
    if (combination.back() != back_max)
        return;
    for (size_t i = 1; i < data.size(); i++) {
        if (combination[i] - combination[i-1] > 3)
            return;
    }
    new_conbinations++;
    return;
  }
  // generate the combinations
  for (size_t i = offset; i <= data.size() - k; ++i) {
    combination.push_back(data[i]);
    go(i+1, k-1);
    combination.pop_back();
  }
}


int main(int argc, char **argv)
{
    for (size_t i = data.size() - 1; i > 0; i--) {
        std::cout << i << std::endl;
        go(0, i);
        total_combinations += new_conbinations;
        if (new_conbinations == 0)
            break;
        std::cout << total_combinations << std::endl;
        new_conbinations = 0;
    }
    std::cout << total_combinations << std::endl;
}