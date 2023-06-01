# def announce(f):
#     def wrappper():
#         print('about to run the function')
#         f()
#         print('done with the function')
#     return wrappper


# @announce
# def hello():
#     print('hello pyinc heros')

# hello()

#EXCEPTIONS
import sys
class all():
    def system(self):
        erro1 = sys.exit(1)

    try:
        x = int(input('x: '))
        y = int(input('y: '))
    except ValueError:
        print('valueerrro wrong input')
        sys.exit(1)

    try:
        result =  x / y
    except ZeroDivisionError:
        print("erro can not divide by 0.")
        sys.exit()
    print(f'{x} / {y} is eaual to {result}')