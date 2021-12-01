#include <array>
#include <iostream>
#include <utility>

constexpr unsigned long long max_bus_id = 601;
constexpr unsigned long long max_bus_offset = 60;

constexpr std::array<std::pair<unsigned long long, unsigned long long>, 8> bus_list = {
    std::make_pair(521ULL, 29ULL),
    {41ULL, 19ULL}, 
    {37ULL, 66ULL},
    {29ULL, 0ULL},
    {23ULL, 37ULL},
    {19ULL, 79ULL},
    {17ULL, 46ULL},
    {13ULL, 42ULL}
};

int main() {
    std::cout << "start!" << std::endl;
    unsigned long long running_sum = max_bus_id - max_bus_offset;
    while(true) {
        bool found_time = true;
        for (const auto& pair : bus_list) {
            if ((running_sum + pair.second) % pair.first != 0) {
                found_time = false;
                break;
            }
            running_sum += max_bus_id;
        }
        if (found_time) {
            std::cout << running_sum << std::endl;
            return 0;
        }
        if (running_sum < max_bus_id - max_bus_offset) {
            std::cout << "uh fuck" << std::endl;
            return 0;
        }
    }

}