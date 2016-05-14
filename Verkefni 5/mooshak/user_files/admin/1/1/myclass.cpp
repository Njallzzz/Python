#include "myclass.h"

std::string myClass::hello() {
	return std::string("Hello")
}

std::string myClass::hello(std::string who) {
	return std::string("Hello ") + who
}

std::string myClass::there() {
	return std::string("there")
}