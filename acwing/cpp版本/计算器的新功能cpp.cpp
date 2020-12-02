#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

/***************************计算器的新功能问题求解（赛码网）******************************/
void printWord(char ch,string* res)
{
	//初始化
	switch(ch){
	case '0':
		res[0]=" - ";
		res[1]="| |";
		res[2]="   ";
		res[3]="| |";
		res[4]=" - ";
		break;
	case '1':
		res[0]="   ";
		res[1]="  |";
		res[2]="   ";
		res[3]="  |";
		res[4]="   ";
		break;
	case '2':
		res[0]=" - ";
		res[1]="  |";
		res[2]=" - ";
		res[3]="|  ";
		res[4]=" - ";
		break;
	case '3':
		res[0]=" - ";
		res[1]="  |";
		res[2]=" - ";
		res[3]="  |";
		res[4]=" - ";
		break;
	case '4':
		res[0]="   ";
		res[1]="| |";
		res[2]=" - ";
		res[3]="  |";
		res[4]="   ";
		break;
	case '5':
		res[0]=" - ";
		res[1]="|  ";
		res[2]=" - ";
		res[3]="  |";
		res[4]=" - ";
		break;
	case '6':
		res[0]=" - ";
		res[1]="|  ";
		res[2]=" - ";
		res[3]="| |";
		res[4]=" - ";
		break;
	case '7':
		res[0]=" - ";
		res[1]="  |";
		res[2]="   ";
		res[3]="  |";
		res[4]="   ";
		break;
	case '8':
		res[0]=" - ";
		res[1]="| |";
		res[2]=" - ";
		res[3]="| |";
		res[4]=" - ";
		break;
	case '9':
		res[0]=" - ";
		res[1]="| |";
		res[2]=" - ";
		res[3]="  |";
		res[4]=" - ";
		break;
	case '*':
		res[0]="   ";
		res[1]="   ";
		res[2]=" * ";
		res[3]="   ";
		res[4]="   ";
		break;
	}

}

void DisplayString(string str)
{
	string output[5],tmpStr[5];
	for(int i=0;i<str.size();i++){
		printWord(str[i],tmpStr);
		for(int i =0;i<5;i++){
			output[i]+=tmpStr[i];
		}
	}
	for(int i=0;i<5;i++){
		cout<<output[i]<<endl;
	}
}
int main()
{
	int input=0;
	while(cin>>input){
		vector<int> primVal;
		//先求解素数
		int val = input;
		while(val>1){
			int sqrt_val = (int)sqrt(val*1.0)+1;
			for(int i=2;;i++){
				if(val%i==0){
					primVal.push_back(i);
					val = val/i;
					break;
				}
			}
		}

		sort(primVal.begin(),primVal.end());
		string myResult;
		for(int i=0;i<primVal.size();i++){
			myResult+=to_string((long long)primVal[i]);
			myResult+='*';
		}
		DisplayString(myResult.substr(0,myResult.size()-1));
	}
	return 0;
}
//g++ 计算器的新功能cpp.cpp -std=c++11
