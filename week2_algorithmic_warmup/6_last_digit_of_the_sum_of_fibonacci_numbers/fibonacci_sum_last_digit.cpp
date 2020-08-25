#include <iostream>
#include<vector>
using namespace std;

int fibonacci_sum_naive(long long n) {
    n = n%60;
    if (n <= 1)
        return n;
    int sum = 1;
    vector<int>f;
    f.push_back(0);
    f.push_back(1);
    for(int i = 2; i<=n;i++){
        f.push_back((f[i-1]+f[i-2])%10);
        sum = (sum+f[i])%10;
    }
    return sum;
}

int main() {
    long long n = 0;
    cin >> n;
    cout << fibonacci_sum_naive(n);
}
