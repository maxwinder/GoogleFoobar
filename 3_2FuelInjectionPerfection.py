# Built on Python 2.7.13
# Google Foobar Fuel Injection Perfection

def solution(n):
    n = int(n)
    steps = 0 

    if n % 2 == 0: # when even value is entered division is where we start
        power  = 1
        while n / (2 ** power) % 2 == 0:  # number of 2's in prime factorization
            power += 1
        n /= 2 ** power
        steps += power

    while n > 1:  # the proces is redone until we have reduced number of pellets to 1
        power = 1
        while (n-1) / (2 ** power) % 2 == 0:
            power += 1
            
        if ((n+1) / (2 ** power) % 2 == 0) & (n > 3):  # Is n+1 or n-1 more often divisible by 2
            # at n = 3, n+1 has longer path (but inferior choice)
            power += 1
            while (n+1) / (2 ** power) % 2 == 0:
                power += 1
            n += 1
        else:
            n -= 1
        n /= 2 ** power
        steps += power + 1
        
    return steps

# solution(65)

'''
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | 
| | | | | | | | | | | | | | | | | 
| | | | | | | | | | | | | | | | |   
| | | | | | | | | | | | | | | | |   9
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   7
|       |       |       |       |
|       |       |       |       |   5
|               |               |
|               |               |   3
|                               |
|                               |   1

The lines in the graph indicate the path that follows when n / 2. 
The line stops where n/2 is an uneven value (e.g 6/2 = 3).
At that point +1 or -1 has to be added. Note that starting with an uneven value is having to hop directly.
One can hop to a neighbouring path that has not yet stopped. 
Hopping from path to path while choosing the neighbouring path that continues the longest, results in
the lowest number of operations to 1.
''' 