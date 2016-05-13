#ifndef __MY_CLASS_H_
#define __MY_CLASS_H_

#include <string>

class myClass {
public:
	myClass() {}
	
	std::string hello();
	std::string hello(std::string);
	std::string there();
};

#endif