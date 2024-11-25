#include <iostream>
#include <vector>
#include <numeric> // accumulate 함수 사용
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> numbers(N);
    for (int i = 0; i < N; ++i) {
        char digit;
        cin >> digit;
        numbers[i] = digit - '0'; // 문자 숫자를 정수로 변환
    }

    int sum = accumulate(numbers.begin(), numbers.end(), 0);
    cout << sum << endl;

    return 0;
}
