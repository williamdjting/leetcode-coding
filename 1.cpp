// 1.cpp
// Remove Duplicates from Sorted Array

#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>

// std::pair<int, int[]>removeDuplicates(int * nums ){
int removeDuplicates(int * nums ){

  int size = sizeof(nums)/sizeof(nums[0]) +1;
  // int * newNums = new int[size]; not dynamic array
  std::vector<int> myVector;
  int count = 0;
  int flag = 0;
  // std::cout << size << std::endl;
  for (int i = 0; i < size; i++) {
      // std::cout << nums[i] << std::endl;
      for (int j = 0; j < myVector.size(); j++) {
          // std::cout << myVector[j] << std::endl;
          if (nums[i] == myVector[j]) {
          std::cout << "found" << std::endl;
          flag = 1;
          break;
          } 
      }

      if (flag == 0) {
      std::cout << "not found added" << std::endl;
      //  std::cout << nums[i] << std::endl;
          myVector.push_back(nums[i]);
          count++;
      }
      flag = 0;
  }

   // Print all elements using a loop
    std::cout << "Vector elements: ";
    for (int i = 0; i < myVector.size(); ++i) {
        std::cout << myVector[i] << " ";
    }
    std::cout << std::endl;

    // Copy the contents of the vector to the integer array using std::copy
    // std::copy(vectorArray.begin(), vectorArray.end(), std::begin(intArray));

  return count;
  // return std::make_pair(count, myVector);
}


int main() {
    int nums[3] = {1,1,2};

    int value = removeDuplicates(nums);
    // print value
    std::cout << "Count result: " << value << std::endl;
    
    // auto value = removeDuplicates(nums);
  

    // int countPair = value.first;
    // int * newNums = value.second;

    // // Now you can use the integer and the array as needed
    // std::cout << "Integer result: " << countPair << std::endl;
    // std::cout << "Array elements: ";
    // for (int i = 0; i < 5; ++i) {
    //     std::cout << newNums[i] << " ";
    // }
    // std::cout << std::endl;

    return 0;
}