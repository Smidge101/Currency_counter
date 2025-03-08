#include "Bank.hpp"

double CurrencyConverter::USDToPesos(double userUSD){

	double pesos = 20.26;
	
	double total = userUSD * pesos;

	return total;

	
}

double CurrencyConverter::USDToEuros(double userUSD){

	//exchange rate 

	double euros = 1.08;

	double total = userUSD / euros;;

	return total;

}


double CurrencyConverter::USDToYen(double userUSD){

	double yen = 148.015;
	
	double total = userUSD * yen;

	return total;
}


