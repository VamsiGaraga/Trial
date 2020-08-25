#include <iostream>
#include <vector>
int get_fibonacci_last_digit_naive(int n) {
    n = n%60;
    if (n <= 1)
        return n;

    std:: vector<int> f;
    f.push_back(0);
    f.push_back(1);

    for (int i = 2; i <= n; ++i) {
        f.push_back((f[i-1]+f[i-2])%10);
    }

    return f[n];
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_naive(n);
    std::cout << c << '\n';
    }
