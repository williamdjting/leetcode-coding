// 2. cpp
// Best Time to Buy and Sell Stock II

#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>


int maxProfit(std::vector<int>& prices) {
        
  // print prices for loop
  for (int i = 0; i < prices.size(); i++) {
      std::cout << prices[i] << std::endl;
  }
  std::cout << "print maxProfit()" << std::endl;


}

int main () {
  std::vector<int> prices;
  prices.push_back(7);
  prices.push_back(1);
  prices.push_back(5);
  prices.push_back(3);
  prices.push_back(6);
  prices.push_back(4);
  maxProfit(prices);

  return 0;
}