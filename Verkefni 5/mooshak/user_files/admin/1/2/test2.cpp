#include <iostream>

// User input
#include "myclass.h"

using namespace std;

int main() {
	myClass test;
	cout << test.hello() << " " << test.there() << endl;
	cout << test.hello() << " " << test.there() << endl;
	return 0;
}