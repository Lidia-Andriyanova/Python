
import re

input_str = ' - 12x^3 - x^2 + 5x - 3 = 0'.replace(' ', '')
pattern = r'([-+]*\d*)(x\^*\d*)|([-+]\d*)'

# res1 = re.search(pattern, input_str)
# print(res1)
# print(res1.groups())

# res2 = re.match(pattern, input_str)
# print(res2)
# print(res2.groups())

compile_pattern = re.compile(pattern)
# res3 = compile_pattern.match(input_str)
# print(res3)
# print(res3.groups())

res4 = compile_pattern.findall(input_str)
print(res4)


