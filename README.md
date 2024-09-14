# 2024softeng
hw02/odd_even.py/ 짝수를 판별해주는 함수를 이용하여 n 값에 구하고자 하는 숫자를 입력하면 짝수 or 홀수인지 판단해주는 프로그램.  

hw02/prime_number.py/ (is_prime) 함수를 만들어 0과 1은 소수가 아니기 때문에 (if n<2) 수식으로 0과 1이 소수가 아니라고 구분할 수 있는 경우를 만들어주고, 남은 수식으로는 (if n % 1 == 0) 나누기 연산자를 사용해 2로 나누어 떨어진다면 바로 false로 나오게 되고 작동을 중지합니다.  

hw02/prime_50.py/ (from lec01.prime_number import is_prime) 첫 번째로 from, import 기능을 이용해 prime number를 구해주는 함수를 가져옵니다. 
그 다음 (for i in range(2, 50)) 에서 구하고자 하는 소수의 범위를 50까지로 설정하고 작동시키는0 프로그램입니다.  

hw02/sum100.py/ (from lec01.odd_even import is_even) 위와 동일한 기능으로 from, import 기능을 통해 짝수-홀수를 구별해주는 함수를 가져옵니다. 
이 프로그래밍 코드에선 두 가지가 작동하는데 첫 째는   for i in range(1,101): /// if is_even(i): ///  total += i 구문을 이용해 100까지 짝수 판별 함수를 통해 짝수를 찾고 계속해서 더해가는 것과, even_100 = [ i for i in range(1,101) if i % 2 == 0 ]  ///  print(even_100) 을 이용해 100까지의 짝수를 리스트로 나열하는 것이 있습니다.
                             
hw02/temp_f2c.py/ def f2c 함수에선 화씨를 섭씨로 바꿔주는 함수를 작성하고 main()에선 구하고자 하는 화씨 온도 하나를 입력하고 프로그래밍을 실행한다. 
질문을 통해 원하는 숫자를 받아서 돌리는 것이 아닌 프로그래밍을 실행하기 전에 하나의 변수를 입력해야 하기에 번거로움이 있기는 하다. 이 프로그래밍에선 f-string 기능을 이용해 변수 값을 문자열에 쉽게 넣고 formating 할 수 있어, 코드가 좀 더 간단해집니다.                      

hw02/factorial.py/ 이 코드에서는 int(input(...) 기능을 def main() 에 집어넣어 프로그래밍을 실행했을 때 값을 입력받고 작동하도록 시도해봤다. 
def factorial() 에선 0!, 1!은 1로 취급하기에 if n == 0 or n == 1: return  1로 나오는 식을 입력하고 나머지 경우는 1씩 빼가며 곱해가는 팩토리얼 식이 작동하도록 해봤다.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

hw03/gui_odd_even.py/ (odd_even.py) 프로그램에서 사용했던 is_even() 함수를 이용하고, gui 를 사용하기 위해 import tkinter as tk // from tkinter import simpledialog 
패키지를 이용한다. 인터페이스에서 title 과 prompt 에서 각 이름을 설정해주고 입력 받은 값을 num으로 설정해(이 때 실수로 받을 수 있도록 int 기능 첨가) 
f-string 기능과 함께 경우를 설정하고 홀수, 짝수, 0 으로 구분할 수 있도록 한다.    

hw03/gui_prime_number.py/

hw03/gui_prime_x.py/

hw03/gui_sum_even_num/

hw03/gui_temp_f2c/

hw03/gui_factorial/
