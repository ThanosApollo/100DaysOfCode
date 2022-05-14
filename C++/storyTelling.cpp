#include <iostream>

using namespace std;


int main()
{   
    string characterName = "John";
    int characterAge = 35;
    
    std::cout << "There was a man named " << characterName << std::endl;
    std::cout << "He was " << characterAge << " years old" << std::endl;
    std::cout << "He liked the name "<< characterName << std::endl;
    std::cout << "He did not like being"<< characterAge << std::endl;

    return 0;
}