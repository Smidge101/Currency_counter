#include <iostream>
#include "Bank.hpp"

// double USDToPesos(double userUSD){

// 	double pesos = 20.26;
	
// 	double total = userUSD * pesos;

// 	return total;

	
// }




int main(){

	double userUSD;
    double newPesos;
    double newEuros;
    double newYen;

    std::cout << "How much money: ";

	std::cin >> userUSD;

	newPesos = USDToPesos(userUSD);

    newEuros = USDToEuros(userUSD);

    newYen = USDToYen(userUSD); 

    std::cout << newYen << std::endl;
    std::cout << newEuros << std::endl;
    std::cout << newPesos;


}

//we do the opposite here so like insertStuffToUSF()