def key_scheduling(S, key_list):
    j = 0
    N = len(S)
    
    for i in range(0, N):
        j = (j + S[i]+key_list[i]) % N
        S[i], S[j] = S[j], S[i]
        print(i, " ", end ="")
        print(S)
    initial_permutation_array = S
     
    print(" ")
    print("Initial permutation array : ", initial_permutation_array)
    

def pseudo_random_generation(S, pt):
    N = len(S)
    i = j = 0
    key_array = []
    
    for k in range(0, len(pt)):
        i = (i + 1) % N
        j = (j + S[i]) % N
         
        S[i], S[j] = S[j], S[i]
        print(k, " ", end ="")
        print(S)
        t = (S[i]+S[j]) % N
        key_array.append(S[t])

    print("Key array : ", key_array)
    print(" ")
    return key_array


def XOR(pt, key_array):
    cipher_text = []
    for i in range(len(pt)):
        c = key_array[i] ^ pt[i]
        cipher_text.append(c)
    print("Cipher text: " , cipher_text)
    return cipher_text


def RC4_encrypt():
    plain_text = "001010010010"
    key = "101001000001"
    n = 3
    
    S = [i for i in range(0, 2**n)]
    print(S)
    
    #key to decimal
    key_list = [key[i:i + n] for i in range(0, len(key), n)]
    
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)
    print(key_list)
    
    #plain text to decimal
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)
 
    print(pt)
    
    #make length of key_list equal to length of S
    diff = int(len(S)-len(key_list))
    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])
 
    print(key_list)
    
    print("Key Scheduling Algorithm : ")
    key_scheduling(S, key_list)
    
    key_array = pseudo_random_generation(S, pt)
    
    cipher_text = XOR(pt, key_array)
    
    encrypted_text = ""
    for i in cipher_text:
        encrypted_text += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
    print(" ")
    print("Cipher text : ", encrypted_text)


if __name__ == "__main__":
    RC4_encrypt()