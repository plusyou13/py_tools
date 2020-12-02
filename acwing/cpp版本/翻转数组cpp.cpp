/*
#include<stdio.h>

int main()
{
	int a[100001];
	a[0] = -1000;					 //最小值
	int reverse = 0,p1=0,p2=0,flag = 0,n;//p1翻转位置1，p2翻转位置2，flag=0为升序
	scanf("%d", &n);
	for (int i = 1; i < n + 1; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n ; i++)
	{
		if ((a[i + 1] > a[i] && flag) || (a[i + 1] < a[i] && !flag))
		{//产生反转：当前升序后者比前者小，当前降序后者比前者大
			reverse++;
			flag = 1 - flag;
			if (reverse == 1)
				p1 = i;
			if (reverse == 2)
				p2 = i;
		}
	}
	if (reverse< 2 ||(reverse == 2 && a[p1]<a[p2 + 1] && a[p2]>a[p1-1]))
		//翻转次数小于2必能调，当翻转次数刚好为2则判断边界
		printf("yes");
	else
		printf("no");
	return 0;
}
*/

#include<iostream>
#include<string>

using namespace std;

string func(int* arr, int n)
{
    /* 先找到降序的起始位置start */
	int start = 0;
	for (start = 0; start < n - 1; ++start)
	{
		if (arr[start] > arr[start + 1])
			break;
	}

	/* 先找到降序的末尾位置end */
	int end;
	for (end = start + 1; end < n - 1; ++end)
	{
		if (arr[end] < arr[end + 1])
			break;
	}


	/* 反转 */
	while(start < end)
	{
		int temp = arr[start];
		arr[start] = arr[end];
		arr[end] = temp;
		start++;
		end--;
	}

	for (int i = 0; i < n - 1; ++i)
	{
		if (arr[i] > arr[i + 1])
			return "no";
	}

	return "yes";
}

int main()
{
	int n;
	cin>>n;
	int *arr = new int[n];
	for (int i = 0; i < n; ++i)
	{
		cin>>arr[i];
	}

	string ans = func(arr, n);
	cout<<ans<<endl;

	return 0;
}
