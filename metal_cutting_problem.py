import sys

nums = [int(x.rstrip()) for x in sys.stdin]
pipes = nums[3:]

# finds profit for a pipe of length l cut into target t size pieces
def profit(t,l,pipe_price,cut_price):
    if t > l:
        return 0
    pipes =int(l/t)
    income = t*pipe_price*pipes
    cuts = 0
    if pipes*t != l:
        cuts += 1
    if pipes > 1:
        cuts += pipes - 1
    return (income-(cuts*cut_price))

max_profit = 0
optimal_l = 0

# cycles over each possible size, and stores a max_profit value
for x in range(1,max(pipes)+1):
    p = 0
    for y in pipes:
        p += profit(x,y,nums[1],nums[0])
    if p > max_profit:
        max_profit = p
        optimal_l = x


needless_pipes = False
# checks if any pipe is taking away from profit at optimal_l
for x in set(pipes):
    if profit(optimal_l,x,nums[1],nums[0]) < 0:
        pipes.remove(x)
        needless_pipes = True

#recalculates max_profit if any pipes were just removed
if needless_pipes:
    for x in range(1,max(pipes)+1):
        p = 0
        for y in pipes:
            p += profit(x,y,nums[1],nums[0])
            if p > max_profit:
                max_profit = p
                optimal_l = x


print (max_profit)
