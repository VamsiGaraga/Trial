#include <iostream>

int gcd(int a, int b) {
  if(b==0){
    return a;
  }
  else{
    return gcd(b,a%b);
  }
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd(std::max(a, b), std::min(a,b)) << std::endl;
  return 0;
}
