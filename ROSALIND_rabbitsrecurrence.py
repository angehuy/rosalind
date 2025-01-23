# n = number of months
# k = number of rabbit offspring produced by pair of mature adults
# each month, each pair of reproduction-age rabbits produce k pairs of rabbits

# replicate fibonacci which is fn = fn-1 + fn-2; with f1 = f2 to initiate the seqwuence

# assume you're starting with 1 pair of baby rabbits, so it takes 1 month for them to mature
# assume 1 adult pair reproduces once
# (numbers are pairs so 1 = 1 pair) so: 1,1,2,3,5
# or f4 = f3 + f2 = 2+1 = 3

# Sample answer
# 5 3 = 5 months, 3 pairs of rabits produced by 1 adult pair ==> 19
# 1) 1 baby pair **above for loop**
# 2) 1 adult pair
# 3) 1 adult pair + 1(3) baby pair = 4
# 4) 1 adult pair + 1(3) baby pair + 3 adult pair = 7
# 5) 1 adult pair + 3 adult pair + 3 adult pair + 3(3) baby pair = 19


def fibonacci_rabbits(months, rabbits_made_pergen):
    num_baby_pre = 1 # starting out with 1 baby pair
    num_adult_pre = 0 
    num_baby_post = 0 # post means after the month
    num_adult_post = 0 
    num_total = 0

    for i in range(1,months): # only iterating 1,2,3,4 since the first generation is the above and my code progresses a month
        # you cant just do "for i in months" since months (a num is not iterable)
        #print("num_adult_pre:", num_adult_pre)
        #print("num_baby_pre:", num_baby_pre)

        num_adult_post += num_baby_pre # (baby -> adult) + existing adults
        num_baby_post = num_adult_pre * rabbits_made_pergen # times pairs of babies reproduced by number of adult
        
        num_adult_pre = num_adult_post # update the num_pre vars
        num_baby_pre = num_baby_post

        #print("num_adult_post:", num_adult_post)
        #print("num_baby_post:", num_baby_post)
        #print("num_adult_pre_afterrun:", num_adult_pre)
        #print("num_baby_pre_afterrun:", num_baby_pre)

        num_total = num_adult_post + num_baby_post
        #print("num_total:", num_total, "\n")
    print(num_total) # total number of pairs
    #print(num_adult_post)# total number of breeding pairs
    return num_total

# fibonacci_rabbits(2,3) # 5 months; 3 baby pairs per adult pair per month



if __name__ == "__main__" :
    l1 = open("./rosalind_fib.txt", "r") # /Users/ahuynh/Downloads/rosalind_fib.txt
    l2 = l1.readline()
    number = [int(x) for x in l2.split()]
    fibonacci_rabbits(*number) # * unpacks an interable in separate







