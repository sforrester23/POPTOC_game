# Don't forget to import your functions
from POP_TOC_functions import *

# write some test for our POP TOC functions

# As a user I want to pass a number through the function div_3, so that I know if a number is divisible by 3
print('Testing div_3 by passing through the number 3. It should show true.')
print(div_3(3) == True)

print('Testing div_3 by passing through the number 4. It should show false.')
print(div_3(4) == True)

print('Testing div_5 by passing through the number 5. It should show true.')
print(div_5(5) == True)

print('Testing div_5 by passing through the number 6. It should show false.')
print(div_5(6) == True)

print('Testing POPTOC by passing through the number 3. It should show POP because it is divisible by 3.')
print(POPTOC(3) == 'POP')

print('Testing POPTOC by passing through the number 5. It should show TOC because it is divisible by 5.')
print(POPTOC(5) == 'TOC')

print('Testing POPTOC by passing through the number 15. It should show POPTOC because it is divisible by both 3 and 5.')
print(POPTOC(5) == 'TOC')

print('Testing POPTOC by passing through the number 8. It should show "Neither POP nor TOC nor POPTOC".')
print(POPTOC(8) == 'Neither POP nor TOC')
