def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)


def main():
    
    num = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))

    
    if num < 0:
        print("음수의 팩토리얼은 정의되지 않습니다.")
    else:
        result = factorial(num)
        print(f"{num}! = {result}")


if __name__ == "__main__":
    main()
