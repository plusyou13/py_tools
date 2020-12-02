/*
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
*/
#include <time.h>
#include <iostream>
#include<stdio.h>
using namespace std;

const int N = 1010;

int n, m;
int v[N], w[N];
int f[N][N];


int main()
{
    //cout << "Hello world!" << endl;
    clock_t t;//定义时钟变量t
	long sum=0;

     cin >> n >> m;
     t = clock();//调用前时间
    for(int i = 1; i <= n; i++) cin >> v[i] >> w[i];
    for(int i = 1; i <= n; i++) {
        for(int j = 0; j <= m; j++) {
            f[i][j] = f[i-1][j];
            if(j>=v[i]) f[i][j] = max(f[i][j], f[i-1][j-v[i]]+w[i]);
        }
    }
    t = clock() - t;//计算函数耗时
	printf("result=%ld,time=%lf s\n", sum,((float) t)/ CLOCKS_PER_SEC);//转化为秒
    cout << f[n][m] << endl;
    return 0;
}
