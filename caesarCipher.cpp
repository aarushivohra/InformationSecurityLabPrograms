#include<iostream>

using namespace std;

string caesarCipher(string plainText, int shift){
    string cipherText = "";

    for(int i=0;i<plainText.length();i++){

        if(isupper(plainText[i])){
            cipherText += ((plainText[i] + shift - 65) % 26) + 65;
        }

        if(islower(plainText[i])){
            cipherText += ((plainText[i] + shift -97) % 26) + 97;
        }
    }

    return cipherText;
}


int main(){
    string plainText = "CaEsArCiPhEr";
    cout << "Plain Text: " << plainText << endl;
    int shift = 5;
    cout << "Shift: " << shift << endl;
    string cipherText = caesarCipher(plainText, shift);
    cout << "Cipher Text: " << cipherText << endl;


}