# Good Practice in python

# Type annotations 

number: int = 10
print(number)

def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]


loud_list: list[str] = upper_everything(['mario', 'JameS', 'SanDRA'])

print(loud_list)