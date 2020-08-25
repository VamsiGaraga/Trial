#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

long long MaxPairwiseProduct(const std::vector<int>& numbers) {
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                ((long long)numbers[first]) * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProductFast( const std::vector<int>& numbers){
	int max_1 = 0,max_2 = 0;
	int n = numbers.size();
	
	for(int i = 0;i < n; i++){
		if(numbers[i] >max_1){
			max_2 = max_1;
			max_1 = numbers[i];
		}
		else if(numbers[i] > max_2){
			max_2 = numbers[i];
		}
	}
	return ((long long)max_1)*max_2;
}

int main() {
/*	while(true){
		int n = rand()%1000 + 2;
		std::cout<<n<<"\n";
		std::vector<int>a;
		for (int i = 0;i<n;i++){
			a.push_back(rand()%10000);
		}
		for (int i=0;i<n;i++){
			std::cout<<a[i]<<' ';
		}
		std::cout<<"\n";
		long long res1 = MaxPairwiseProduct(a);
		long long res2 = MaxPairwiseProductFast(a);
		
		if(res1!=res2){
			std::cout<<"Wrong "<<res1<<" "<<res2<<"\n";
			break;	
		}
		else{
			std::cout<<"OK\n";
		}
	}*/
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductFast(numbers) << "\n";
    return 0;
}
