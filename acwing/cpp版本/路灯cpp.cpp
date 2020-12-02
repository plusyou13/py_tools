#include <stdio.h>
//排序后求最大距离max
int main()
{
    int n,l;
    int i,j,temp;
   //为实现精度，定义距离max为双精度，float不行
    double max=0;
    scanf("%d %d",&n,&l);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=n-1;j>0;j--)
        {
            if(a[j]<a[j-1])
            {
                temp = a[j];
                a[j] = a[j-1];
                a[j-1]=temp;
            }
        }
    }
    for(i=0;i<n-1;i++)
    {
        if(a[i+1]-a[i]>max)
            max = a[i+1]-a[i];
    }
    if (a[0]>0&&2*a[0]>max)
        max = 2*a[0];
    if(a[n-1]<l&&(2*(l-a[n-1])>max))
        max = 2*(l-a[n-1]);
    printf("%.2f",max/2);
    return 0;
}
/*
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;
int main()
{
	int l,n;
	double d=0.0;
	scanf("%d%d",&n,&l);
	int led[n];
	for(int i=0;i<n;i++)
	   scanf("%d",&led[i]);
    sort(led,led+n);
	for(int i=1;i<n;i++)
	   d= max(d,(led[i]-led[i-1])/2.0);
	d = max(d,(l-led[n-1])/1.0);
	d = max(d,led[0]/1.0);
	cout <<fixed<< setprecision(2) << d << endl;
	return 0;
}
*/