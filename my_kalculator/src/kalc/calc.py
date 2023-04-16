from tqdm import tqdm
import time


def add2numbers(num1=0, num2=0):
    result(num1+num2)


def subtract2numbers(num1=0, num2=0):
    result(num1-num2)


def multiply2numbers(num1=0, num2=0):
    result(num1*num2)


def divide2numbers(num1=1, num2=1):
    result(num1/num2)


def result(value=0):
    for i in tqdm(range(100), desc="Kalculating..."):
        time.sleep(0.01)
    print(f"Result is {value}")
