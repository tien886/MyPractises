#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;
int main(){
	int h;cin>>h;
	for(int i=1;i<=h;i++){ 
		for (int j=1;j<=h-i;j++)
			{cout<<"  ";} 
		cout<<'*';
	if(i>1)	{
			for (int j=0;j<=2*(i-1)-2;j++) //csc
				{cout<<" ";}
			cout<<'*';
	} 
		cout<<endl;
	}
	for(int i=h-1;i>=1;i--){
		for (int j=1;j<=h-i;j++){
			{cout<<"  ";} 
	}
		cout<<'*';
	if(i>1)	{
		for (int j=0;j<=2*(i-1)-2;j++) //csc
			{cout<<" ";}
		cout<<'*';
	} 
	cout<<endl;
	}
	return 0;
	}
