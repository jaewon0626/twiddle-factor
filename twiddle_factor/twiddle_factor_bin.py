import csv
import os
import numpy as np
from rounding import *

# csv 파일을 읽어들여서 텍스트 파일로 변환하는 함수
def csv_to_txt(number_csv, twiddle_factor):
    with open(number_csv, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(twiddle_factor, 'w') as txt_file:
            for row in csv_reader:
                # 각 행의 데이터를 탭으로 구분하여 텍스트 파일에 쓰기
                txt_file.write('\t'.join(row) + '\n')

# 디렉토리 및 파일 경로 설정
csv_file_name = 'real.csv'
csv_file_name = 'imag.csv'

txt_file_name = 'real.txt'
txt_file_name = 'imag.txt'

# 함수 호출로 CSV 파일을 텍스트 파일로 변환
real_csv_file_path = os.path.join('twiddle_factor', 'number_csv', 'real.csv')
real_txt_file_path = os.path.join('twiddle_factor', 'number_txt', 'real.txt')
csv_to_txt(real_csv_file_path, real_txt_file_path)

imag_csv_file_path = os.path.join('twiddle_factor', 'number_csv', 'imag.csv')
imag_txt_file_path = os.path.join('twiddle_factor', 'number_txt', 'imag.txt')
csv_to_txt(imag_csv_file_path, imag_txt_file_path)

# real.txt 이진수 변환
def bin_real_to_file(file_path, output_file_path, b_sign, b_int, b_fr):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        with open(output_file_path, 'w') as output_file:
            for number in numbers:
                number = float(number.strip()) # 파일에서 숫자 읽어오기
                result = q_truncate(number, b_sign, b_int, b_fr) # 고정 소수점으로 변환
                output_file.write(f"input num : {number}, bin_tran num : {result}\n")

file_path = 'C:/python_project/twiddle_factor/number_txt/real.txt' # 입력 파일 경로
output_file_path = 'C:/python_project/twiddle_factor/bin_number_txt/real_bin.txt' # 출력 파일 경로

b_sign = 0 # 부호 비트 크기 설정 (부호 O : 1, 부호 X : 0)
b_int = 1 # 정수 부분 비트 수
b_fr = 5 # 소수 부분 비트 수
bin_real_to_file(file_path, output_file_path, b_sign, b_int, b_fr) # 함수 호출


# imag.txt 이진수 변환
def bin_imag_to_file(file_path, output_file_path, b_sign, b_int, b_fr):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        with open(output_file_path, 'w') as output_file:
            for number in numbers:
                number = float(number.strip()) # 파일에서 숫자 읽어오기
                result = q_truncate(number, b_sign, b_int, b_fr) # 고정 소수점으로 변환
                output_file.write(f"input num : {number}, bin_tran num : {result}\n")

file_path = 'C:/python_project/twiddle_factor/number_txt/imag.txt' # 입력 파일 경로
output_file_path = 'C:/python_project/twiddle_factor/bin_number_txt/imag_bin.txt' # 출력 파일 경로

b_sign = 1 # 부호 비트 크기 설정 (부호 O : 1, 부호 X : 0)
b_int = 1 # 정수 부분 비트 수
b_fr = 5 # 소수 부분 비트 수
bin_imag_to_file(file_path, output_file_path, b_sign, b_int, b_fr) # 함수 호출