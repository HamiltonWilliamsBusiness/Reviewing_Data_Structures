x = [2200,2350,2600,2130,2190]

'''
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

# 1. In Feb, how many dollars you spent extra compare to January?

print(f'In Feb, I spent {(x[1] - x[0])} extra compared to January')

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f'The total expense in the first quarter of the year is  {(x[1] + x[0] + x[2])}')

# 3. Find out if you spent exactly 2000 dollars in any month
def exact200(x):
    g = False
    for y in x:
        if y == 2000:
            g = True
            print('Spent exactly 2000')
            return
    print('Did not spend exactly 2000')
exact200(x)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
x.append(1980)
print(x)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
# based on this

x[3] = x[3] - 200 
print(x)

# Question 2
# You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f'The length of the list is {len(heros)}!')


# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk'
#    so remove it from the list first and then add it after 'hulk'

heros = heros [:-1]
print(heros)
g = []
for x in heros:
    if x == 'hulk':
        g.append('hulk')
        g.append('black panter')
    else:
        g.append(x)
heros = g
print(g)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.


heros = ['doctor strange' if hero == 'thor' or hero == 'hulk' else hero for hero in heros]
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)