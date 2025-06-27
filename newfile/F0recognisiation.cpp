#include <bits/stdc++.h>
using namespace std;
int main() {
    int N, f0, Dmax;
    cin >> N >> f0 >> Dmax;
    int points[1001][2]; 
    int F1[1001][2];     
    int F[1001];         
    int F0[2];
    for (int i = 1; i <= N; i++) {
        cin >> points[i][0] >> points[i][1];
        if (i == f0) {
            F0[0] = points[i][0];
            F0[1] = points[i][1];
        }
    }
    int countF1 = 0;
    int countF = 0;
    for (int i = 1; i <= N; i++) {
        if (i == f0) continue;
        double D = sqrt(pow(points[i][0] - F0[0], 2) + pow(points[i][1] - F0[1], 2));
        if (D < Dmax) {
            F1[countF1][0] = points[i][0];
            F1[countF1][1] = points[i][1];
            countF1++;
        } else {
            F[countF++] = i;
        }
    }
    int countF2 = 0;
    for (int i = 0; i < countF; i++) {
        for (int j = 0; j < countF1; j++) {
            double D = sqrt(pow(points[F[i]][0] - F1[j][0], 2) + pow(points[F[i]][1] - F1[j][1], 2));
            if (D < Dmax) {
                countF2++;
                break; 
            }
        }
    }
    cout << countF1 << " " << countF2;
    return 0;
}
