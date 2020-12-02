#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
string a,b;
bool isAlph(char &c) {
  return ((c>='a'&&c<='z')||(c>='A'&&c<='Z'));
}
bool isNum(char &c) {
  return (c>='0'&&c<='9');
}
bool isOne(char &c) {
  return (isAlph(c)||isNum(c));
}
int main () {
  cin>>a>>b;
  int l = a.length();
  int cnt = 0;
  for(int i=0;i<l;++i) {
    if(isOne(a[i])^(b[i]=='1'))
      continue;
    ++cnt;
  }
  double ans = cnt*100.0/l;
  printf("%.2lf%%\n", ans);
}