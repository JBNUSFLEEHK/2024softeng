# 2024softeng
hw02/odd_even.py/ 짝수를 판별해주는 함수를 이용하여 n 값에 구하고자 하는 숫자를 입력하면 짝수 or 홀수인지 판단해주는 프로그램.  

hw02/prime_number.py/ (is_prime) 함수를 만들어 0과 1은 소수가 아니기 때문에 (if n<2) 수식으로 0과 1이 소수가 아니라고 구분할 수 있는 경우를 만들어주고, 남은 수식으로는 (if n % 1 == 0) 나누기 연산자를 사용해 2로 나누어 떨어진다면 바로 false로 나오게 되고 작동을 중지합니다.  

hw02/prime_50.py/ (from lec01.prime_number import is_prime) 첫 번째로 from, import 기능을 이용해 prime number를 구해주는 함수를 가져옵니다. 그 다음 (for i in range(2, 50)) 에서 구하고자 하는 소수의 범위를 50까지로 설정하고 작동시키는0 프로그램입니다.  

hw02/sum100.py/ (from lec01.odd_even import is_even) 위와 동일한 기능으로 from, import 기능을 통해 짝수-홀수를 구별해주는 함수를 가져옵니다. 이 프로그래밍 코드에선 두 가지가 작동하는데 첫 째는   for i in range(1,101): /// if is_even(i): ///  total += i 구문을 이용해 100까지 짝수 판별 함수를 통해 짝수를 찾고 계속해서 더해가는 것과, even_100 = [ i for i in range(1,101) if i % 2 == 0 ]  ///  print(even_100) 을 이용해 100까지의 짝수를 리스트로 나열하는 것이 있습니다.
                             
                           
