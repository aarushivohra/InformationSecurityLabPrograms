#include<bits/stdc++.h>
using namespace std;

void generateKeyMatrix(string key, char keyMatrix[5][5]){
    int map[26];
    memset(map, sizeof(map), 0);

    int n = key.length();
    int k = 0, i = 0, j = 0;
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            if(key[k] != 'j' && map[key[k] - 97] == 0){
                keyMatrix[i][j] = key[k];
                map[key[k] - 97] = 1;
            }           
            k++;
            if(k >= n){
                break;
            }

        }
        if(k >= n){
            break;
        }
    }

    j++;
    if(j == 5){
        i++;
        j = 0;
    }

    for(int l=0;l<26;l++){
        if(l+97 != 'j' && map[l] == 0){
            keyMatrix[i][j] = l+97;
            map[l] = 1;
            j++;
            if(j == 5){
                j=0;
                i++;
            }
        }
    }
}


void charPairs(string plainText){
    if(plainText.length() % 2 != 0){
        plainText += 'z';
    }
}

void search(char keyT[5][5], char a, char b, int arr[4])
{
    int i, j;
 
    if (a == 'j')
        a = 'i';
    else if (b == 'j')
        b = 'i';
 
    for (i = 0; i < 5; i++) {
 
        for (j = 0; j < 5; j++) {
 
            if (keyT[i][j] == a) {
                arr[0] = i;
                arr[1] = j;
            }
            else if (keyT[i][j] == b) {
                arr[2] = i;
                arr[3] = j;
            }
        }
    }
}

int mod5(int x) { return (x % 5); }

string encrypt(string plainText, char keyMatrix[5][5]){
    int n = plainText.length();
    int i, coords[4];
    string cipher = "";
 
    
    for (i=0;i<n;i+=2) {
 
        search(keyMatrix, plainText[i], plainText[i + 1], coords);
        
        if (coords[0] == coords[2]) {
            cipher += keyMatrix[coords[0]][mod5(coords[1] + 1)];
            cipher += keyMatrix[coords[0]][mod5(coords[3] + 1)];
        }
        else if (coords[1] == coords[3]) {
            cipher += keyMatrix[mod5(coords[0] + 1)][coords[1]];
            cipher += keyMatrix[mod5(coords[2] + 1)][coords[1]];
        }
        else {
            cipher += keyMatrix[coords[0]][coords[3]];
            cipher += keyMatrix[coords[2]][coords[1]];
        }
    }

    return cipher;
}


string playFairCipher(string plainText, string key){

    int n = key.length();
    int m = plainText.length();

    charPairs(plainText);
    char keyMatrix[5][5];
    generateKeyMatrix(key, keyMatrix);

    string cipher = encrypt(plainText, keyMatrix);
    return cipher;
}


int main(){
    string plainText = "abc";
    string key = "defghiklm";

    cout << "Plain Text is: " << plainText << endl;
    cout << "Key is: " << key << endl;

    string cipher = playFairCipher(plainText, key);
    cout << "Play Fair Cipher is: " << cipher << endl;
}