/*
 * EulerModule.h
 *
 *  Created on: 5 janv. 2017
 *      Author: hnnguyen
 */

#ifndef EULERMODULECPP_EULERMODULE_H_
#define EULERMODULECPP_EULERMODULE_H_

#include <math.h>
#include <iterator>
#include <algorithm>
#include <iostream>
#include <vector>
#include <exception>
#include <string>

namespace EulerProject {

class NegativeException: public std::exception {
public:
	NegativeException(const char* errMessage):errMessage_(errMessage){}
	virtual const char* what() const throw() {
		return errMessage_;
	}

private:
	const char* errMessage_;
};

class EulerModule {
public:
	static bool checkPrime(const int) throw(NegativeException&);
	static std::vector<int> getDivisors(const int) throw(NegativeException&);
	static std::vector<int> getPrimeDivisors(const int) throw(NegativeException&);
	static std::vector<int> factorize(const int) throw(NegativeException&);
	static std::vector<int> sieveEratosthenes(const int) throw(NegativeException&);

	static long getFibo(const int) throw(NegativeException&);
	static int sumDigits(const int) throw(NegativeException&);
	static bool checkPanlidrome(const int) throw(NegativeException&);

	static void printResult(std::vector<int>);

//	NegativeException negativeException;
};

} /* namespace EulerProject */

#endif /* EULERMODULECPP_EULERMODULE_H_ */
