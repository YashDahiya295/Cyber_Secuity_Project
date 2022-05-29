initial_permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
                             60, 52, 44, 36, 28, 20, 12, 4,
                             62, 54, 46, 38, 30, 22, 14, 6,
                             64, 56, 48, 40, 32, 24, 16, 8,
                             57, 49, 41, 33, 25, 17, 9, 1,
                             59, 51, 43, 35, 27, 19, 11, 3,
                             61, 53, 45, 37, 29, 21, 13, 5,
                             63, 55, 47, 39, 31, 23, 15, 7]


key_permutation_table_one = [57, 49, 41, 33, 25, 17, 9,
                             1, 58, 50, 42, 34, 26, 18,
                             10, 2, 59, 51, 43, 35, 27,
                             19, 11, 3, 60, 52, 44, 36,
                             63, 55, 47, 39, 31, 23, 15,
                             7, 62, 54, 46, 38, 30, 22,
                             14, 6, 61, 53, 45, 37, 29,
                             21, 13, 5, 28, 20, 12, 4]


key_permutation_table_two = [14, 17, 11, 24, 1, 5,
                             3, 28, 15, 6, 21, 10,
                             23, 19, 12, 4, 26, 8,
                             16, 7, 27, 20, 13, 2,
                             41, 52, 31, 37, 47, 55,
                             30, 40, 51, 45, 33, 48,
                             44, 49, 39, 56, 34, 53,
                             46, 42, 50, 36, 29, 32]


left_shift_key = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


e_bit_selection_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12,
                         13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,
                         24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]


sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]


permutation_table = [16, 7, 20, 21,
                     29, 12, 28, 17,
                     1, 15, 23, 26,
                     5, 18, 31, 10,
                     2, 8, 24, 14,
                     32, 27, 3, 9,
                     19, 13, 30, 6,
                     22, 11, 4, 25]


initial_permutation_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
                               39, 7, 47, 15, 55, 23, 63, 31,
                               38, 6, 46, 14, 54, 22, 62, 30,
                               37, 5, 45, 13, 53, 21, 61, 29,
                               36, 4, 44, 12, 52, 20, 60, 28,
                               35, 3, 43, 11, 51, 19, 59, 27,
                               34, 2, 42, 10, 50, 18, 58, 26,
                               33, 1, 41, 9, 49, 17, 57, 25]


def binarytoString(s):
    string_binary = ""
    for i in s:
        string_binary += i
    return string_binary


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def decimalToBinary(n):
    n = format(n, '048b')
    return n.replace("0b", "")


def decimalToBinary2(n):
    n = format(n, '04b')
    return n.replace("0b", "")


def decimalToBinary3(n):
    n = format(n, '032b')
    return n.replace("0b", "")


def decimalToHexadecimal(n):
    return hex(int(n)).replace("0x", "")


def shift_list(left_list, right_list, pos):
    pos %= len(left_list)
    pos *= 1
    shifted_list_left = left_list[pos:] + left_list[:pos]
    shifted_list_right = right_list[pos:] + right_list[:pos]
    return shifted_list_left, shifted_list_right


def hex_to_bin(character):
    int_val = int(character, base=16)
    bin_val = bin(int_val)[2:].zfill(4)
    return bin_val


def initial_permutation(plain_text):
    plain_text_binary = []
    for i in plain_text:
        x = hex_to_bin(i)
        plain_text_binary.append(x)
    plain_text_binary = ''.join([str(i) for i in plain_text_binary])
    plain_text_permute = []
    for i in range(0, len(plain_text_binary)):
        x = initial_permutation_table[i]
        plain_text_permute.append(plain_text_binary[x-1])
    return plain_text_permute


def key_discard_56(key):
    key_binary = []
    for i in key:
        x = hex_to_bin(i)
        key_binary.append(x)
    key_binary = ''.join([str(i) for i in key_binary])
    key_text_permute = []
    for i in range(0, 56):
        x = key_permutation_table_one[i]
        key_text_permute.append(key_binary[x-1])
    return key_text_permute


def key_discard_48(key):
    key_text_48 = []
    for i in range(0, 48):
        x = key_permutation_table_two[i]
        key_text_48.append(key[x-1])
    return key_text_48


def encrypt_rounds(left_pt, right_pt, key):
    right_48 = []
    for i in range(0, 48):
        x = e_bit_selection_table[i]
        right_48.append(right_pt[x-1])
    right_48 = binarytoString(right_48)
    key = binarytoString(key)
    right_48 = binaryToDecimal(int(right_48))
    key = binaryToDecimal(int(key))
    XOR = right_48 ^ key
    XOR = decimalToBinary(XOR)
    parts_6bits = []
    for i in range(0, 48, 6):
        part = XOR[i: i+6]
        parts_6bits.append(part)
    after_sbox = []
    count = 0
    for i in parts_6bits:
        list_of = list(i)
        digit1 = list_of[0]
        digit2 = list_of[5]
        if(digit1 == '0' and digit2 == '0'):
            row_no = 0
        elif(digit1 == '0' and digit2 == '1'):
            row_no = 1
        elif(digit1 == '1' and digit2 == '0'):
            row_no = 2
        else:
            row_no = 3
        sum_of = 0
        for j in range(1, 5):
            sum_of += int(list_of[j])*pow(2, (4-j))
        column_no = sum_of
        number = sbox[count][row_no][column_no]
        count = count+1
        after_sbox.append(decimalToBinary2(number))

    total = []
    for i in after_sbox:
        list_of = list(i)
        for j in list_of:
            total.append(j)

    total_new = []
    for i in range(0, 32):
        x = permutation_table[i]
        total_new.append(total[x-1])

    left_output = right_pt
    left_pt = binarytoString(left_pt)
    total_new = binarytoString(total_new)

    left_pt = binaryToDecimal(int(left_pt))
    total_new = binaryToDecimal(int(total_new))

    XOR = left_pt ^ total_new
    right_output = decimalToBinary3(XOR)
    return left_output, right_output


def final_permutation(text):
    final_text_64 = []
    for i in range(0, 64):
        x = initial_permutation_inverse[i]
        final_text_64.append(text[x-1])
    return final_text_64


def DES_encrypt(plain_text, key):
    plain_text_permute = initial_permutation(plain_text)
    left_plain_text = plain_text_permute[0:32]
    right_plain_text = plain_text_permute[32:64]
    key_56 = key_discard_56(key)
    left_key = key_56[0:28]
    right_key = key_56[28:56]
    for i in range(0, 16):
        left, right = shift_list(left_key, right_key, left_shift_key[i])
        left_key = left
        right_key = right
        key_comb = left_key+right_key
        subkey = key_discard_48(key_comb)
        ltext, rtext = encrypt_rounds(
            left_plain_text, right_plain_text, subkey)
        rtext = list(rtext)
        left_plain_text = ltext
        right_plain_text = rtext
    final_text = rtext+ltext
    final = final_permutation(final_text)
    final = binarytoString(final)
    final = binaryToDecimal(int(final))
    final = decimalToHexadecimal(final)

    return str(final.upper())


def DES_decrypt(cipher_text, key):
    cipher_text_permute = initial_permutation(cipher_text)
    left_cipher_text = cipher_text_permute[0:32]
    right_cipher_text = cipher_text_permute[32:64]
    key_56 = key_discard_56(key)
    left_key = key_56[0:28]
    right_key = key_56[28:56]
    subkeys = []
    for i in range(0, 16):
        left, right = shift_list(left_key, right_key, left_shift_key[i])
        left_key = left
        right_key = right
        key_comb = left_key+right_key
        subkey = key_discard_48(key_comb)
        subkeys.append(subkey)
    for i in range(0, 16):
        ltext, rtext = encrypt_rounds(
            left_cipher_text, right_cipher_text, subkeys[15-i])
        rtext = list(rtext)
        left_cipher_text = ltext
        right_cipher_text = rtext
    plain_text = rtext+ltext
    final = final_permutation(plain_text)
    final = binarytoString(final)
    final = binaryToDecimal(int(final))
    final = decimalToHexadecimal(final)
    if(len(final) != 16):
        final = '0' + final

    return str(final.upper())
