/*
 * EulerModule.cpp
 *
 *  Created on: 5 janv. 2017
 *      Author: hnnguyen
 */

#include "EulerModule.h"

using namespace EulerProject;

/**
 * @brief check a number is prime or not
 * @param a positive integer number
 * @return true if the number is prime
 * @return false if the number is not prime
 */
bool EulerModule::checkPrime(const int num) throw (NegativeException&) {
	bool retVal;
	if (num < 2)
		return false;
	else if (num == 2)
		return true;
	else {
		for (int i = 3; i < static_cast<int>(num / 2) + 1; ++i) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}
}

/**
 * @brief find all divisors of a number
 * @param a positive integer number
 * @return list of all divisors
 */
std::vector<int> EulerModule::getDivisors(const int num)
		throw (NegativeException&) {
	if (num < 0) {
		throw NegativeException("Negative integer!\n");
	}
	std::vector<int> retVal;
	retVal.push_back(1);
	for (int i = 2; i < num / 2 + 1; ++i) {
		if (num % i == 0) {
			retVal.push_back(i);
		}
	}
	retVal.push_back(num);
	return retVal;
}

/**
 * @brief find all prime divisors of a number
 * @param a positive integer number
 * @return list of all prime divisors
 */
std::vector<int> EulerModule::getPrimeDivisors(const int num)
		throw (NegativeException&) {
	if (num < 0) {
		throw NegativeException("Negative integer!\n");
	}
	std::vector<int> retVal;
	int divisor = 3;
	int iNum = num;
	if (iNum % 2 == 0) {
		retVal.push_back(2);
		while (iNum % 2 == 0) {
			iNum = iNum / 2;
		}
	}

	while (iNum > 1) {
		if (iNum % divisor == 0) {
			retVal.push_back(divisor);
			while (iNum % divisor == 0) {
				iNum = iNum / divisor;
			}
		} else {
			divisor += 2;
			while (not checkPrime(divisor)) {
				divisor += 2;
			}
		}
	}
	return retVal;
}

/**
 * @brief factorize a number
 * @param a positive integer number
 * @return list of divisors
 */
std::vector<int> EulerModule::factorize(const int num)
		throw (NegativeException&) {
	if (num < 0) {
		throw NegativeException("Negative integer!\n");
	}
	std::vector<int> retVal;
	if (num == 1) {
		retVal.push_back(num);
	} else {
		int iNum = num;
		int divisor = 3;
		while (iNum % 2 == 0) {
			retVal.push_back(2);
			iNum = iNum / 2;
		}
		while (iNum > 1) {
			if (iNum % divisor == 0) {

				while ((iNum % divisor) == 0) {
					retVal.push_back(divisor);
					iNum = iNum / divisor;
				}
			} else {
				divisor += 2;
			}
		}
	}
	return retVal;
}

/**
 * @brief print the vector of integers
 * @param vector of integers
 * @return none
 */
void EulerModule::printResult(std::vector<int> vecRes) {
	std::cout << "[";
	for (auto& x : vecRes) {
		std::cout << x << " ";
	}
	std::cout << "]" << std::endl;
}

/**
 * @brief generate list of all prime numbers which is smaller than a given number
 * @param a positive integer number
 * @return list of all prime number
 */
std::vector<int> EulerModule::sieveEratosthenes(const int num)
		throw (NegativeException&) {
	if (num < 0) {
		throw NegativeException("Negative integer!\n");
	}
	std::vector<int> retVal;
	std::vector<int> vecInitial(num, 1);
	int upper = static_cast<int>(sqrt(num));
	for (int i = 2; i < upper; ++i) {
		if (vecInitial.at(i)) {
//			std::cout << i;
			for (int j = i * i; j < num; j += i) {
				vecInitial.at(j) = 0;
			}
		}
	}
	for (int i = 2; i < num; ++i) {
		if (vecInitial.at(i)) {
			retVal.push_back(i);
		}
	}
	return retVal;
}

/**
 * @brief get the n-th Fibonacci number
 * @param order number n
 * @return the n-th Fibonacci number
 */
long EulerModule::getFibo(const int num) throw (NegativeException&) {
	if (num < 0) {
		throw NegativeException("Negative integer!\n");
	}
	int retVal = 0;
	int a = 1, b = 1, i = 0;
	while (i < num-1) {
		b = a + b;
		a = b - a;
		i ++;
	}
	retVal = b;
	return retVal;
}
