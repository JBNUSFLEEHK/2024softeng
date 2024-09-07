def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    while True:
        try:
            n = int(input("팩토리얼을 계산할 숫자를 입력하세요 (종료하려면 'q' 입력): "))
            if n < 0:
                print("음수는 팩토리얼을 계산할 수 없습니다. 양의 정수를 입력해주세요.")
            else:
                result = factorial(n)
                print(f"{n}의 팩토리얼은 {result}입니다.")
        except ValueError:
            user_input = input("올바른 숫자가 아닙니다. 종료하시겠습니까? (y/n): ")
            if user_input.lower() == 'y':
                break
            else:
                continue

if __name__ == '__main__':
    main()
