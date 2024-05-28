numerator, denominator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return denominator
    else:
        return denominator / result

print(changed_div(numerator, denominator))