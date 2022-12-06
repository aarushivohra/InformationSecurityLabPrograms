#include<iostream>
using namespace std;

void generateKeyMatrix(int n, string key, int keyMatrix[][10]){
    int k = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            keyMatrix[i][j] = key[k] % 65;
            k++;
        }
    }

}

void generatePlainTextMatrix(int n, string plainText, int plainTextMatrix[][1]){
    for(int i=0;i<n;i++){
        plainTextMatrix[i][0] = plainText[i] % 65;
    }
}


void getCipherText(int n, int keyMatrix[][10], int plainTextMatrix[][1], int cipherMatrix[][1]){
    for(int i=0;i<n;i++){
        for(int j=0;j<1;j++){
            cipherMatrix[i][j] = 0;
            for(int k=0;k<n;k++){
                cipherMatrix[i][j] += keyMatrix[i][k] * plainTextMatrix[k][j];
            }
            cipherMatrix[i][j] %= 26;
        }
    }

}


string HillCipher(string plainText, string key){
    int n = plainText.length();
    int m = key.length();

    string cipher = "";
    if(m == n*n){
        int keyMatrix[n][10];
        generateKeyMatrix(n, key, keyMatrix);

        int plainTextMatrix[n][1];
        generatePlainTextMatrix(n, plainText, plainTextMatrix);

        int cipherMatrix[n][1];
        getCipherText(n, keyMatrix, plainTextMatrix, cipherMatrix);

        for(int i=0;i<n;i++){
            cipher += cipherMatrix[i][0] + 65;
        }

    }

    return cipher;

}

int main(){
    string plainText = "ABC";
    string key = "DEFGHIJKL";

    cout << "Plain Text is: " << plainText << endl;
    cout << "Key is: " << key << endl;

    string cipher = HillCipher(plainText, key);
    cout << "Hill Cipher is: " << cipher << endl;
}