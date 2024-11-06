#include<bits/stdc++.h>
using namespace std;
bool kiemtraSNT(unsigned long long a){
	if(a<2) return false;
	for(unsigned long long j=2;j*j<=a;j++){
		if(a%j==0) return false;
	}
			return true;
}
unsigned long long UCLN(unsigned long long a, unsigned long long b){
	while(b!=0){
		unsigned long long gcd=b;
		                 	b=a%b;
							a=gcd;
	}
	return a;
}
unsigned long long ketqua(unsigned long long n){
	unsigned long long m=n+1;
	while(true){
		unsigned long long gcd=UCLN(m,n);
		if(kiemtraSNT(gcd)) {return m;}
		m++;
	}
}
int main(){
	unsigned long long x;cin>>x;
	cout<<ketqua(x);
	return 0;
}
