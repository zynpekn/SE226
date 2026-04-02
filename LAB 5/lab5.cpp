
#include <iostream>
using namespace std;


double seriesSum(int n) {
    // Base case
    if (n == 1)
        return 1.0;

    if (n % 2 == 0)
        return seriesSum(n - 1) - (1.0 / n);
    else
        return seriesSum(n - 1) + (1.0 / n);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    double result = seriesSum(n);
    cout << "S_" << n << " = " << result << endl;
    return 0;
}