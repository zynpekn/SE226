include <iostream>
using namespace std;
//TASK1 


int main() {
    int num;
    int steps = 0;

    cout << "Enter a positive integer greater than 1: ";
    cin >> num;

    while (num <= 1) {
        cout << "Invalid input. Enter a number greater than 1: ";
        cin >> num;
    }

    cout << num;
    while (num != 1) {
        if (num % 2 == 0) {
            num = num / 2;
        } else {
            num = num * 3 + 1;
        }

        cout << " -> " << num;
        steps++;
    }
    cout << "\nTotal steps: " << steps << endl;

    return 0;


//TASK2

using namespace std;

    int n;
    int fizzCount = 0;
    int buzzCount = 0;
    int fizzBuzzCount = 0;

    cout << "Enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input. Enter a number between 10 and 100: ";
        cin >> n;
    }

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            continue;
        }
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzBuzzCount++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "\nSummary:\n";
    cout << "Fizz: " << fizzCount << endl;
    cout << "Buzz: " << buzzCount << endl;
    cout << "FizzBuzz: " << fizzBuzzCount << endl;

    return 0;


//TASK3
using namespace std;

    int n;
    cout << "Enter a number between 3 and 9: ";
    cin >> n;
    while (n < 3 || n > 9) {
        cout << "Invalid input. Enter a number between 3 and 9: ";
        cin >> n;
    }

    // Top half
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // Bottom half
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}