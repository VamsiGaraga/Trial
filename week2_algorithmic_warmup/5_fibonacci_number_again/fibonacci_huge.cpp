#include <iostream>
#include <vector>
using namespace std;

long long get_fibonacci_huge(long long n, long long m) {
    if (n <= 1){
        return n;
    }

    vector<long long> f;
    f.push_back(0);
    f.push_back(1%m);
    f.push_back(1%m);
    int k=1;
    while(!((f[k]==0) && (f[k+1]==1))){
        f.push_back((f[k] + f[k+1])%m);
        k++;
    }
    return(f[n%k]);
}

int main() {
    long long n, m;
    cin >> n >> m;
    cout << get_fibonacci_huge(n, m) << '\n';
}
