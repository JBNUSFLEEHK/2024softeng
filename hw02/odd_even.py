def is_even(n):
    if n % 2 == 0:
        return n

def main():
    n = 83

    if is_even(n): #함수 대입 해서 써보기
        print("짝수입니다.")

    else:
        print("홀수입니다.")

if __name__ == '__main__':
    main()
