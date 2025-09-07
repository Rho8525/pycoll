print('welcome to my simple claculkalrtor')
print('typo, mb\n')

print('lets start...')
num1 = input('enter the first number: ')
try:
    num1 = int(num1)
except ValueError:
    print('i said number dummy')
print('\nnext is... operator')
print('+ - * /')
op = input('choose operator: ')
if (op not in '+-*/'):
    print('choose available operator dum dum')
print('\nfinally... ')
num2 = input('enter the second number: ')
try:
    num2 = int(num2)
except ValueError:
    print('i said number dummy')
print('\nready for the result yet?')
def result(n1, op, n2):
    if op == '+': return n1 + n2
    if op == '-': return n1 - n2
    if op == '*': return n1 * n2
    if op == '/': return n1 / n2
    return 'dum dum, it is your fault if do something wrongly!'
print('its...')
print(result(num1, op, num2))