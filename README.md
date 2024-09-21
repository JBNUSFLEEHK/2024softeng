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

hw03/gui_prime_number.py/ def is_prime() 함수 사용. USER_INP 에서 받은 숫자를 num 으로 설정. (if, else) 구문에서 is_prime() 함수를 이용해 구분하고 결과로 나오도록 
한다.

hw03/gui_prime_x.py/ 이 프로그램에서는 (from, import) 기능을 이용해 소수를 구해주는 함수를 가져와서 실행되도록 해봤다. 가져오는 기능을 이용하니 한결 코드가 간결해진 것 같긴 하다. 간결성과 가독성? 이 더 나아진 느낌. 나머지는 위와 동일하게 int 를 이용해 실수로 받고 입력 받은 수까지 범위를 설정해 소수들을 리스트에 계속해서 더해주는 프로그램이다.

hw03/gui_sum_even_num/ 이번에도 함수를 가져오는 기능을 써봤다. 입력받은 숫자까지의 짝수값을 구하는 프로그램이기에 num+1로 범위를 설정한다. is even(i) 함수를 통해 짝수를 구하고 total += i 수식을 이용하여 계속해서 더해간다. print() 값으로는 짝수를 다 더한 결과값과 더해진 짝수의 리스트가 출력되도록 한다. 

hw03/gui_temp_f2c/ (from, import) 기능을 쓰지 않으니 불편한 점을 하나 안 것 같다. USER_INP 에서 실수값을 받을 때, 정해주는 이름을 다르게 설정해야 한다는 점? 
물론 프로그램을 실행할 때 문제는 없었지만 코드가 많아지고 복잡해질 수록 에러가 나올 수 있을 확률이 높아질 것 같다. 확실히 코드를 간소화 시키는 것이 편리하다는 것을 느낀 것 같다.  

hw03/gui_factorial/ factorial 코드에선 다시 함수를 가져오는 기능을 사용해봤다. 결국 함수를 가져오고 함수를 대표하는 이름만 써주니 기능을 대신해줘 훨씬 간단하다. 

hw03 을 마치며,

1) from, import 기능의 편리성을 깨달음. 코드의 가독성, 간편성, 편리성 측면에서.
2) gui 기능을 통해 입력받는 창에 원하는 숫자를 입력하고 결과를 구해봤다. 다만 아쉬운 점은 결과값도 입력받는 창이 계속 유지되면서 나오면 좋겠다는 생각을 해봤다.
   gui 창이 유지되는 코드가 무엇인지 알아보고 스스로 시도해보는 시도를 해야겠다.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------  
hw04/density_calculator.api.py
수업시간에 교수님과 진행했던 gugudan_api.py 와 비슷한 수준의 과제이다. def hello() 함수 부분에서는 큰 차이는 없었다. (밀도 계산하는 데에 필요한 용어만 바꾸고 수식정도만 넣어줬다.) 구구단 코드와의 차이점이라고는 값을 두 개 이상 받아서 진행했어야 한다는 점?이 있겠다. 밀도를 구하기 위해선 질량과 부피. 총 2개의 값이 필요하기 때문에 mass, volume 으로 설정하고 추가했다. 밀도 값은 부피 분의 질량이기 때문에 density = mass / volume 이렇게 수식으로 표현해주고 값을 구해주는 순으로 진행된다. 질량과 부피가 꼭 맞아 떨어지는 수치가 아닐 수도 있기 때문에 float() 함수를 통해 실수를 읽을 수 있도록 하였고, 실수값으로 계산이 이루어진다면 무한대로 나머지가 나올 수 있기 때문에 :.2f 로 소수점 두 번째 숫자까지만 나오도록 설정했다. 

hw04 를 마치며,
아직 적응이 잘 안되는 듯한 느낌이다. 웹으로 표출되어 실행된다는 점이 새롭게 다가오기는 하지만 아직 미숙한 점이 많고 알아야 하는 기능들이 많은 것 같다. 그래서 이번 과제를 하면서 내가 중점적으로 했던 것은 각각의 용어의 사용 이유와 기능을 알아보는 것이었다. 어떠한 부분에서 이게 왜 쓰였는지 알고 있어야 내가 이해하고 활용할 수 있지 않은가. 아직까지 따라가는 데에 있어서 버거운 부분이 크게 있지는 않지만, 앞으로 라즈베리파이와 연결해서 과제를 할 때는 좀 더 어려운 부분들이 있을거라고 생각된다. 웹페이지 세계에 좀 더 친숙해질 수 있도록 스스로 감각을 키워가야겠다. 
