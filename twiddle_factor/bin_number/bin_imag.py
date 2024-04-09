import numpy as np
from rounding import *

def bin_imag(file_path, b_sign, b_int, b_fr):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            number = float(number.strip()) # 파일에서 숫자 읽어오기
            result = q_truncate(number, b_sign, b_int, b_fr) # q_truncate 함수를 이용하여 고정 소수점으로 변환
            print(f"입력 숫자 : {number}, 이진수 변환 결과 : {result}")

file_path = 'C:/python_project/twiddle_factor/number_txt/imag.txt' # 파일 경로 설정
b_sign = 1 # 부호 비트 크기 설정 (부호 O : 1, 부호 X : 0)
b_int = 1 # 정수 부분 비트 수
b_fr = 5 # 소수 부분 비트 수
bin_imag(file_path, b_sign, b_int, b_fr) # 함수 호출
