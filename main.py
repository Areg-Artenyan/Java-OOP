from calculator import ComplexCalculator, Addition, Multiplication, Division
from logging_utils import setup_logger, get_logger


def input_complex_number():
    real = float(input("Введите действительную часть: "))
    imag = float(input("Введите мнимую часть: "))
    return complex(real, imag)


def main():
    setup_logger()
    logger = get_logger("complex_calculator")

    logger.info("Калькулятор комплексных чисел запущен.")

    logger.info("Введите первое комплексное число:")
    num1 = input_complex_number()

    logger.info("Введите второе комплексное число:")
    num2 = input_complex_number()

   
    operation = Addition()

    calculator = ComplexCalculator(operation)

    result = calculator.calculate(num1, num2)

    logger.info(f"Результат {calculator}: {result}")


if __name__ == "__main__":
    main()