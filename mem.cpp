#include <bits/stdc++.h>
using namespace std;
int temp[1000000]={0};
int main() {
    int N,X;cin>>N;
    int a[N],cnt=0;
    for(int i=0;i<N;i++) cin>>a[i];
    cin>>X;
    int count=0;
    for(int i=0;i<N;i++){
		int leftover=X-a[i];
		if(leftover>0&&leftover<200000){
		count+=temp[leftover];
		}
	temp[a[i]]++;
	}
    cout<<count;
	return 0;
}
