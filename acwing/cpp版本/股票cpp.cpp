#include <iostream>
using namespace std;

int GetValue(int n)
{
	int i = 0;// i统计遇到了多少次下跌
	int j = 2;// 每次下跌之后上涨的天数，包含已经下跌的那天
	int k = n;
	while (k > j) {
		i += 2;
		k -= j;
		++j;
	}
	return n - i;
}

int main()
{
	int n;
	while (cin >> n) {
		cout << GetValue(n) << endl;
	}
	return 0;
}