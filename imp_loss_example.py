import math

##################################
### CALCULATE IMPERMANENT LOSS ###
##################################

def calcQuantities(priceConstant, priceRatio):
    """
    Calculate quantity of assets in the pool at any price point.
    Doesn't work with the imp loss function yet, not sure why.
    """
    print('calculate the base and token quantities for the pool.')
    print(f'price constant = {priceConstant}')
    print(f'price ratio = {priceRatio}')
    
    baseQty = int(math.sqrt(priceConstant / priceRatio))
    print(f'base quantity: {baseQty}')

    tokenQty = int(math.sqrt(priceConstant * priceRatio))
    print(f'token quantity: {tokenQty}')
    
    return baseQty, tokenQty

def calcImpermanentLoss(baseQty, tokenQty, futurePriceRatio):
    """
    Calculate impermanent loss.
    Adapted from javascript example listed online.
    Need to look up what hodl strat, lp strat & FPR mean.
    """
    productConstant = baseQty * tokenQty
    print(f'product constant = baseQty {baseQty} * token Qty {tokenQty} = {productConstant}')
    
    # hoddling strategy
    hodlStrategy = ((tokenQty * futurePriceRatio) + baseQty)
    print(f'hodl strategy = {hodlStrategy}')
    
    # liquidity provider strategy
    lpStrategy = ((math.sqrt(productConstant / futurePriceRatio)) * futurePriceRatio) + \
                 (math.sqrt(productConstant * futurePriceRatio))
    print(f'lp strategy = {lpStrategy}')
    
    impermanentLoss = (hodlStrategy - lpStrategy) / hodlStrategy * 100
    
    print(f'impermanent loss = {round(impermanentLoss, 1)}%')
    return impermanentLoss

def test():
    
    print('* Example: UNI/ETH pool contains 12605 ETH and 1459747 UNI tokens *\n')
    print('assume Uniswap doubles in value relative to ETH')
    priceRatio = 0.01727
    print(f'so price ratio will be {priceRatio}\n')
    imp_loss = calcImpermanentLoss(12605, 1459747, priceRatio)

test()
