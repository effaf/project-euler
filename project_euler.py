# Problem 2 (Fibonacci)
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with and , the first terms will be:
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonacci(limit):
    first = 0
    second = 1
    sum_even = 0
    current = 0
    while current < limit:
        current = first + second
        if current % 2 == 0:
            sum_even += current

        first = second
        second = current

    return sum_even

print(fibonacci(4 * 10**6))

# Problem 3
'''
The prime factors of 13195 are 5, 7, 13, and 29

What is the largest prime factor of the number 600851475143?

'''

def largestPrime(n):
  if n == 0:
    return 0

  i = 2
  while n % i == 0:
    n = n // 2

  i = 3
  while i * i < n:
    while n % i == 0:
      n = n // i
    i = i + 2
  return n  if n > 1 else i - 2

print(largestPrime(600851475143))

'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 91 * 99 = 9009

Find the largest palindrome made from the product of two 3-digit numbers
'''

def reverseNum(num):
  reverseNum = 0
  while num:
    ones_place = num % 10
    reverseNum = (reverseNum * 10) + ones_place
    num = num // 10
  return reverseNum

def get_largest_three_digit_palindrome():
  max_palindrome = float('-inf')
  for i in range(999, 99, -1):
    for j in range(i, 99, -1):
      product = i * j
      if product < max_palindrome:
        continue
      reverse = reverseNum(product)
      if product == reverse:
        max_palindrome = max(max_palindrome, product)

  return max_palindrome
print(get_largest_three_digit_palindrome())

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
'''

def getPrime_less_than_or_equal_to_n(n):
  arr = [True for _ in range(n + 1)]
  i = 2
  while i * i < n:
    multiple = 2
    while arr[i] and i * multiple <= n:
      arr[i * multiple] = False
      multiple += 1
    i += 1

  ans = []
  for j in range(2, len(arr)):
    if arr[j]:
      ans.append(j)

  return ans

def smallest_positive_number_divisible_by_all_numbers_till_n(n):
  primeFactors = getPrime_less_than_or_equal_to_n(n)
  print(primeFactors)
  ans = 1
  for value in primeFactors:
    power = 1
    while value ** power <= n:
      power += 1
    ans *= value ** (power - 1)

  return ans


print(smallest_positive_number_divisible_by_all_numbers_till_n(20))

'''
Problem 5
Self problem - Get the total number of divisors for a given n
'''

from collections import defaultdict
def get_total_positive_divisors(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  prime_count = defaultdict(int)
  i = 2
  while n % i == 0:
    prime_count[i] = prime_count.get(i, 0) + 1
    n = n // i

  i = 3
  while n > 1:
    while n % i == 0:
      prime_count[i] = prime_count.get(i, 0) + 1
      n = n // i

    i += 2

  divisors = 1
  for prime_factor, count in prime_count.items():
    ways_to_select = count + 1
    divisors = divisors * ways_to_select

  return divisors

print(get_total_positive_divisors(3560))

'''
The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + 3^2..... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
        (1 + 2 + 3 ..... + 10) ^ 2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def square_sum_difference(n):
  sum_of_n = 0
  sum_of_squares = 0
  for i in range(n + 1):
    sum_of_n += i
    sum_of_squares += (i ** 2)

  square_of_sum = sum_of_n ** 2
  return square_of_sum - sum_of_squares


print(square_sum_difference(100))

'''
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def checkPrime(primes, n):
  for i in primes:
    if n % i == 0:
      return False

  return True

def get_nth_prime(n):
  count = 0
  primes = []
  counter = 2
  while count != n:
    if checkPrime(primes, counter):
      primes.append(counter)
      count += 1
    counter += 1
  return counter - 1


print(get_nth_prime(10001))

'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832
.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
''''

number = '''7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

def get_max_product_of_n_adjacent_digits(n, number):

  number = number.replace('\n', '')

  left = 0
  right = 0
  current_product = 1
  max_product = float('-inf')
  while right < len(number):
    char = number[right]

    if char == '0':
      right += 1
      left = right
      current_product = 1
      continue

    current_product *= int(char)
    if n < right - left + 1:
      leftChar = number[left]
      current_product = current_product // int(leftChar)
      left += 1

    max_product = max(max_product, current_product)
    right += 1

  return max_product


print(get_max_product_of_n_adjacent_digits(13, number))

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c , for which,
                a^2 + b^2 = c^2
For example 3^2 + 4^2 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
'''

def search_sum_of_pythogorean_triple(s):
    largest_value_of_a = s // 3
    for a in range(1, largest_value_of_a):
        value_of_b = (s * (s - 2 * a)) // (2 * (s - a))
        c = s - value_of_b - a
        if a**2 + value_of_b**2 == c**2:
            return ((a, value_of_b, c), (a * value_of_b * c))
    return -1



print(search_sum_of_pythogorean_triple(1000))

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def sum_of_primes_until_n(n):

  sieve = [True for _ in range(n)]
  sum_prime = 0
  i = 2
  while i * i < n:
    counter = 2
    while i * counter < n:
      sieve[i * counter] = False
      counter += 1
    i += 1

  for index in range(2, len(sieve)):
    if sieve[index]:
      sum_prime += index

  return sum_prime

print(sum_of_primes_until_n(2000000))

'''
In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the grid?
'''

grid_str = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

grid_line_split = grid_str.split("\n")
grid = []
for line in grid_line_split:
  row = [int(num) for num in line.split()]
  grid.append(row)

def max_product_of_n_adjacent_element_in_grid(grid, n):

  if len(grid) < n:
    return -1

  rows = len(grid)
  cols = len(grid[0])

  max_product = float('-inf')

  # Row Traversal
  for index in range(len(grid)):
    row = grid[index]
    left = 0
    right = 0
    window_product = 1
    while right < len(row):
      if row[right] == 0:
        right += 1
        left = right
        window_product = 1
        continue

      window_product *= row[right]
      if n < right - left + 1:
        window_product = window_product // row[left]
        left += 1
      max_product = max(max_product, window_product)
      right += 1


  # Col Traversal
  for col in range(len(grid[0])):
    left = 0
    right = 0
    window_product = 1
    while right < len(grid):
      if grid[right][col] == 0:
        right += 1
        left = right
        window_product = 1
        continue

      window_product *= grid[right][col]
      if n < right - left + 1:
        window_product = window_product // grid[left][col]
        left += 1

      max_product = max(max_product, window_product)
      right += 1


  # left to right diagonal traversal
  for index in range(len(grid[0])):
    left_row, left_col = 0, index
    right_row, right_col = 0, index
    window_product = 1
    while right_row < rows and right_col < cols:
      if grid[right_row][right_col] == 0:
        right_row += 1
        right_col += 1
        left_row = right_row
        left_col = right_col
        window_product = 1
        continue

      window_product *= grid[right_row][right_col]
      if n < right_row - left_row + 1:
        window_product = window_product // grid[left_row][left_col]
        left_row += 1
        left_col += 1

      max_product = max(max_product, window_product)
      right_row += 1
      right_col += 1


  # right to left diagonal
  for index in range(len(grid[0]) - 1, -1, -1):
    left_row, left_col = 0, index
    right_row, right_col = 0, index
    window_product = 1
    while 0 <= right_row and right_row < len(grid):
      if grid[right_row][right_col] == 0:
        right_row += 1
        right_col -= 1
        left_row = right_row
        left_col = right_col
        window_product = 1
        continue

      window_product *= grid[right_row][right_col]
      if n < right_row - left_row + 1:
        window_product = window_product // grid[left_row][left_col]
        left_row += 1
        left_col -= 1

      max_product = max(max_product, window_product)
      right_row += 1
      right_col -= 1


  # top to bottom first col
  for index in range(1, len(grid)):
    left_row, left_col = index, 0
    right_row, right_col = index, 0
    window_product = 1
    while right_row < rows and right_col < cols:
      if grid[right_row][right_col] == 0:
        right_row += 1
        right_col += 1
        left_row = right_row
        left_col = right_col
        window_product = 1
        continue

      window_product *= grid[right_row][right_col]
      if n < right_row - left_row + 1:
        window_product = window_product // grid[left_row][left_col]
        left_row += 1
        left_col += 1

      max_product = max(max_product, window_product)
      right_row += 1
      right_col += 1

  # bottom to top last col
  for index in range(len(grid) - 1, -1, -1):
    left_row, left_col = index, len(grid[0]) - 1
    right_row, right_col = index, len(grid[0]) - 1
    window_product = 1
    while 0 <= right_row and 0 <= right_col:
      if grid[right_row][right_col] == 0:
        right_row -= 1
        right_col -= 1
        left_row = right_row
        left_col = right_col
        window_product = 1
        continue

      window_product *= grid[right_row][right_col]
      if n < left_row - right_row + 1:
        window_product = window_product // grid[left_row][left_col]
        left_row -= 1
        left_col -= 1

      max_product = max(max_product, window_product)
      right_row -= 1
      right_col -= 1

  return max_product


print(max_product_of_n_adjacent_element_in_grid(grid, 4))

'''
The sequence of triangle numbers is generated by adding the natural numbers. So the
th triangle number would be
. The first ten terms would be:

Let us list the factors of the first seven triangle numbers:


We can see that
 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

def get_nth_triangle_number(n):
  return (n * (n + 1)) // 2

def get_prime_factors(n):

  prime_divisors = {}
  i = 2
  while n % i == 0:
    prime_divisors[i] = prime_divisors.get(i, 0) + 1
    n = n // 2
  i = 3
  while n > 1:
    while n % i == 0:
      prime_divisors[i] = prime_divisors.get(i, 0) + 1
      n = n // i
    i += 2
  return prime_divisors

def get_number_of_divisors(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  prime_factors = get_prime_factors(n)
  divisors = 1
  for factor, value in prime_factors.items():
    divisors = divisors * (value + 1)

  return divisors


def first_triangle_number_to_have_n_divisors(n):

  counter = 1
  while True:
    triangle_number = get_nth_triangle_number(counter)
    current_divisors = get_number_of_divisors(triangle_number)
    if n < current_divisors:
      return triangle_number
    counter += 1


get_number_of_divisors(76576500)
#first_triangle_number_to_have_n_divisors(500)

'''
Find the first 10 digits of the sum of 100 50 digit numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
'''

number ='''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''

def processNumber(number):
  split_number = number.split('\n')
  return split_number

largeNumber = processNumber(number)
print(largeNumber)

def computeSum(largeNumber):
  sum_stack = []
  carry = 0
  for j in range(len(largeNumber[0]) - 1, -1, -1):
    current_sum = carry
    for i in range(len(largeNumber)):
      current_sum += int(largeNumber[i][j])

    sum_stack.append(current_sum % 10)
    carry = current_sum // 10

  while carry:
    ones = carry % 10
    sum_stack.append(ones)
    carry //= 10

  ans = []
  for i in range(10):
    ans.append(sum_stack.pop())
  return ''.join(str(i) for i in ans)


print(computeSum(largeNumber))

largeNumber = processNumber(number)

n = sum(largeNumber)
print(str(n)[:10])

# Collatz number Problem 14
class Collatz:
  def __init__(self):
    self.lengths = {}

  def get_collatz(self, num):

    if num <= 2:
      return num


    if num in self.lengths:
      return self.lengths[num]

    chain_length_at_num = 0

    if num % 2 == 0:
      chain_length_at_num = self.get_collatz(num // 2) + 1
    else:
      chain_length_at_num = self.get_collatz((num * 3) + 1) + 1

    self.lengths[num] = chain_length_at_num

    return self.lengths[num]

collatz = Collatz()

for i in range(1000000, 0, -1):
  current_collatz = collatz.get_collatz(i)

max_chain = float('-inf')
max_chain_number = 0
for num, length in collatz.lengths.items():
  if max_chain < length:
    max_chain = length
    max_chain_number = num

print(max_chain_number)