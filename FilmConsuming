#include <bits/stdc++.h>
using namespace std;
int main(){
	int a,b,c;cin>>a>>b>>c;
	int x,y,z;cin>>x>>y>>z;
	int giathuyet=a*3600+b*60+c;
	int tgcoi=x*3600+y*60+z;
	int s=0;
	if(giathuyet>tgcoi){s=tgcoi;}
	else {s=giathuyet;}
    int S=1;
	for(int i=s;i>=2;--i){
	if(giathuyet % i == 0 && tgcoi % i == 0){
	S=i;break;
	}
	}
	int tu=tgcoi/S;
	int mau=giathuyet/S;
	cout<< tu<<endl;
	cout<< mau;
}
