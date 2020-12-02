#include<iostream>
using namespace std;
#include<stdio.h>
#include <math.h>
struct point
{
	float x;
	float y;
	float z;
};
int fun(point k1,point k2)
{
    float x,y,z;
    //计算三阶行列式
    x=k1.y*k2.z-k1.z*k2.y;
    y= k1.z*k2.x-k1.x*k2.z;
    z=k1.x*k2.y-k1.y*k2.x;
    //叉乘为0
    if(x==0&&y==0&&z==0)
    	return 1;
    else return 0;

} 
int main()
{ 
	float x1,x2;
	struct point p[3];
	p[0].x=1,p[0].y=1,p[0].z=1;
	p[1].x=2,p[1].y=2,p[1].z=2;
	p[2].x=5,p[2].y=5,p[2].z=5;
	struct point k1={p[2].x-p[1].x,p[2].y-p[1].y,p[2].z-p[1].z};
	struct point k2={p[0].x-p[1].x,p[0].y-p[1].y,p[0].z-p[1].z};
	if(fun(k1,k2)==1)
		cout<<"3点共线";
	else cout<<"3点不共线";
	return 0;
	} 
