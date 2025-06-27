#include <bits/stdc++.h>
using namespace std;

void nhapso(int n) {
    int max = 0;
    long long nhap;
    int so;
    for (int i=1; i<=n; i++) {
        cin>>nhap;
        long long goc=nhap;
        int dem=0;
        while(goc>0) {
            goc/=10;
            dem++;
        }
        int ans=0; 
        
        if (dem%2 == 1) {
            long long giua=nhap;
            for (int j=0; j<dem/2;j++) {
                giua/=10;
            }
            ans=giua % 10;
        }
        else {
            long long giua=nhap;
            for (int j=0; j<dem/2-1;j++) {
                giua/=10;
            }
            ans=giua%100;
        }
    if (ans>max) {
            max=ans;
            so=nhap;  
        }
    else if (ans==max) {
            so=nhap;  
        }
    }
    cout<<so;
}

int main() {
    int n;
    cin >> n;  
    nhapso(n);  
    return 0;
}
