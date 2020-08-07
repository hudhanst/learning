def garis(panjang=10, choiceschar='*'):
    return print(choiceschar*panjang)

def inputlist():
    try:
        n = int(input('masukkan panjang list yang anda inginkan !'))
    except:
        print ('maaf anda salah memasukkan, harus angka!!!')
        inputlist()
    garis()
    
    ainput = []
    q = 0
    while q < n:
        try:
            a = int(input(f'masukkan angka ke {q} pada baris list'))
        except:
            print('maaf anda salah memasukkan, harus angka')
        
        ainput.append(a)
        q = q+1
    
    garis()
    return ainput

def inputB(lengofinputa):
    while True:
        binput = input('silahkan masukkan angka untuk variable B !')
        try:
            binput = int(binput)
            if binput <= lengofinputa:
                break
            else:
                print('input yang anda masukkan lebih besar dari panjang list sebelumnya')
        except ValueError:
            print('maaf anda salah memasukkan, harus angka')
    garis()
    return int(binput)

def find_shortes_Nth(a, b):
    a.sort()
    return print(a[b-1])

def main():
    """
    input:
    a = array/list[int]
    b = int < size a
    TASK:
    find 'b'th smallest elemnet in 'a'
    """
    a = inputlist()
    b = inputB(int(len(a)))
    # b = inputB(10)
    print (a, b)
    find_shortes_Nth(a,b)

if __name__ == "__main__":
    main()