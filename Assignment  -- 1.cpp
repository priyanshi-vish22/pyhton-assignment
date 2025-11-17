// 1. Program to demonstrate class and object

//#include <iostream>
//using namespace std;
//
//class Student {
//public:
//    string name;
//    int roll;
//
//    void display() {
//        cout << "Name: " << name << endl;
//        cout << "Roll No: " << roll << endl;
//    }
//};
//
//int main() {
//    Student s1;
//    s1.name = "Priyanshi";
//    s1.roll = 101;
//    s1.display();
//    return 0;
//}
//

// 2. Program to show data encapsulation using private data members and public methods

//#include <iostream>
//using namespace std;
//
//class Bank {
//private:
//    int balance;
//
//public:
//    void setBalance(int b) {
//        balance = b;
//    }
//    int getBalance() {
//        return balance;
//    }
//};
//
//int main() {
//    Bank account;
//    account.setBalance(5000);
//    cout << "Your Balance is: " << account.getBalance();
//    return 0;
//}
//
//
//// 3. Program to demonstrate constructor and destructor
//
//#include <iostream>
//using namespace std;
//
//class Demo {
//public:
//    Demo() {
//        cout << "Constructor called!" << endl;
//    }
//
//    ~Demo() {
//        cout << "Destructor called!" << endl;
//    }
//};
//
//int main() {
//    Demo obj;
//    return 0;
//}



//// 4. Program to input marks of students using arrays and calculate average
//
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;

    int marks[n];
    int sum = 0;

    cout << "Enter marks: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> marks[i];
        sum += marks[i];
    }

    float average = (float)sum / n;
    cout << "Average marks = " << average;

    return 0;
}

