#Homework9 task1
import time

def find_coins_greedy(coins_diff, coins_list:list):
    coins_dict = {item: 0 for item in coins_list}
    coins_list.sort(reverse=True)
    
    while coins_diff >= coins_list[-1]:
        for item in coins_list:
            if coins_diff >= item:
                coins_diff -= item
                coins_dict[item] += 1
                break

    return coins_dict

def find_min_coins(coins_diff, coins_list):
    # Initialize the dp array with amount + 1 (infinity)
        # Initialize the dp array with amount + 1 (infinity)
    dp = [coins_diff + 1] * (coins_diff + 1)
    dp[0] = 0  # Base case: no coins needed to make amount 0

    # Initialize the coin_count array with empty dictionaries
    coin_count = [{} for _ in range(coins_diff + 1)]
    coin_count[0] = {coin: 0 for coin in coins_list}

    # Fill the dp array and coin_count array
    for coin in coins_list:
        for x in range(coin, coins_diff + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] += 1

    # print(coin_count)
    # print()
    # If dp[amount] is still amount + 1, it means it's not possible to make that amount
    if dp[coins_diff] == coins_diff + 1:
        return "Change cannot be made with the given denominations."

    return coin_count[coins_diff]


coins_list = [50, 25, 10, 5, 2, 1]

start_time = time.time()
print(find_coins_greedy(1234567, coins_list))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time coins_greedy: {elapsed_time} seconds")


start_time = time.time()
print(find_min_coins(1234567, coins_list))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


coins_list = [222, 123, 101, 74, 38]

start_time = time.time()
print(find_coins_greedy(1234567, coins_list))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time coins_greedy: {elapsed_time} seconds")


start_time = time.time()
print(find_min_coins(1234567, coins_list))
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
