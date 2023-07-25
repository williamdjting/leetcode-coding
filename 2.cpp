// 2. cpp
// Best Time to Buy and Sell Stock II

#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>


int maxProfit(std::vector<int>& prices) {
  // 7, 1, 5, 3, 6, 4 
  int smallerInt; 
  int biggerInt;
  int sum = 0;
  // print prices for loop
  for (int i = 0; i < prices.size(); i++) {
      // std::cout << prices[i] << std::endl;
      if (prices[i+1] != NULL && prices[i] < prices[i+1]) {
          smallerInt = prices[i];
          biggerInt = prices[i+1];
          int addtoSum = biggerInt - smallerInt;
          sum += addtoSum;
          std::cout << "sum: \n" << sum << std::endl;
      }
  }
  // print smallestInt  
  std::cout << "sum: \n" << sum << std::endl;




}

int main () {
  std::vector<int> prices;
  // example 1
  /*
  prices.push_back(7);
  prices.push_back(1);
  prices.push_back(5);
  prices.push_back(3);
  prices.push_back(6);
  prices.push_back(4);
  */
  // example 2
  // /*
  // prices.push_back(1);
  // prices.push_back(2);
  // prices.push_back(3);
  // prices.push_back(4);
  // prices.push_back(5);
  // */
  // example 3
  // /*
  prices.push_back(7);
  prices.push_back(6);
  prices.push_back(4);
  prices.push_back(3);
  prices.push_back(1);
  // */
  maxProfit(prices);

  return 0;
}