#include<bits/stdc++.h>
using namespace std;
int main() {
    int row, col;
    cout << "Enter Row Number:";
    cin >> row;
    cout << "Enter Col Number:";
    cin >> col;
    char plainMatrix[row][col];
    getchar();
    cout << "Enter Your Text According to your format\n";
    for (int i = 0;i < row;i++) {
        string one_row;
        getline(cin, one_row);
        for (int j = 0;j < col;j++)plainMatrix[i][j] = one_row[j];
    }
    char cipherMatrix[col][row];
    for (int j = 0;j < col;j++) {
        for (int i = 0;i < row;i++) {
            cipherMatrix[j][i] = plainMatrix[i][j];
        }
    }
    cout << "Plain Matrix\n\n";
    for (int i = 0;i < row;i++) {
        for (int j = 0;j < col;j++) {
            cout << plainMatrix[i][j];
        }
        cout << endl;
    }
    cout << "\n\nCipher Matrix\n\n";
    for (int i = 0;i < col;i++) {
        for (int j = 0;j < row;j++) {
            cout << cipherMatrix[i][j];
        }
        cout << endl;
    }

}