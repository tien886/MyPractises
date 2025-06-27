#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;
bool check(int *a, int n, int key)
{
	int left = 0, right = n - 1;
 	while(left <= right)
	{
		int mid = left + (right - left)/2;
		if(a[mid] < key)	left = mid + 1;
		else if (a[mid] > key) 	right = mid - 1;
		else if(a[mid] == key) return true;
	}
	return false;

}
int main()
{
	srand(time(NULL));
	int n; cin>>n;
	int *a = new int[n];
	for(int i = 0; i < n; i++)
	{
		int tmp = rand() % 201 - 100;
		a[i] = tmp;
	}
	sort(a, a+n);
	for(int i = 0; i < n; i++)
        {
               	cout<<a[i]<<" ";
        }
	cout<<endl;
	int key;
	while(1)
	{

		cout<<"Nhap so ban muon tim: "; cin>>key;
        	cout<<endl;
        	bool ok = check(a, n, key);
        	if(ok) cout<<"co so "<<key<<" nha bro";
        	else cout<<key<<" la so gi v bro";	
		char s;
		cout<<"\nNua khong ?"; cin>>s;
		if(s == 'n' || s == 'N') break;

	}
	return 0;
}
