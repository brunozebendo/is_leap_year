def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# o desafio é retornar os dias do mês, testando antes se o ano é bissexto,
# a função day_in_month faz isso simplesmente testando se a função is_leap é true
# e se o input de month é dois, se for, retorna 29, se não, retorna o mês da lista
# que é determinado pela posição [] – 1, já que a posição começa em zero e o mês começa em 01