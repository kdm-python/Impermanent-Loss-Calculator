import math

##################################
### CALCULATE IMPERMANENT LOSS ###
##################################

# base expression x * y = k

def calcImpermanentLoss(baseQty, tokenQty, futurePriceRatio):
    """
    Calculate impermanent loss.
    Adapted from javascript example listed online.
    Need to look up what hodl strat, lp strat & FPR mean.
    """
    productConstant = baseQty * tokenQty

    # hoddling strategy
    hodlStrategy = ((tokenQty * futurePriceRatio) + baseQty)

    # liquidity provider strategy
    lpStrategy = ((math.sqrt(productConstant / futurePriceRatio)) * futurePriceRatio) + \
                 (math.sqrt(productConstant * futurePriceRatio))

    impermanentLoss = (hodlStrategy - lpStrategy) / hodlStrategy * 100

    return impermanentLoss

class Asset:
    """Represents a specific asset type i.e. a coin or token."""
    assetID = 10  # hidden from user

    def __init__(self, name, price):
        self.name = name  # str
        self.price = price  # float
        self.assetID = Asset.assetID  # int
        Asset.assetID += 10

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def changePrice(self, new_price):
        """Increase or decrease current market value."""
        self.price = new_price

    def __lt__(self, other):
        """Return True if asset price less than other asset price."""
        return self.price < other.price

    def __gt__(self, other):
        """Return True if asset price greater than other asset price."""
        return self.price > other.price

    def __str__(self):
        s = f'{self.name}\nCurrent market value: £{self.price}'
        return s

# to expand later:
class coin(Asset):
    pass

class token(Asset):
    pass

class Pool:
    """Represent liquidity pool with quantities of supplied assets."""
    poolID = 101  # hidden from user

    def __init__(self, poolName, baseAsset, tokenAsset, baseQty, tokenQty):
        """Initialise pool attributes & calc total liquidity."""
        self.poolName = poolName  # str
        self.baseAsset = baseAsset  # Asset object
        self.tokenAsset = tokenAsset  # Asset object
        self.baseQty = baseQty  # int
        self.tokenQty = tokenQty  # int
        self.poolID = Pool.poolID  # int

        self.baseTotal = baseAsset.getPrice() * baseQty
        self.tokenTotal = tokenAsset.getPrice() * tokenQty

        Pool.poolID += 1

    def getPoolName(self):
        return self.poolName

    def getBaseTotal(self):
        return self.baseTotal

    def getTokenTotal(self):
        return self.tokenTotal

    def getBaseQty(self):
        return self.baseQty

    def getTokenQty(self):
        return self.tokenQty

    def setBaseQty(self, newQuantity):
        self.baseQty = newQuantity

    def setTokenQty(self, newQuantity):
        self.tokenQty = newQuantity

    def __str__(self):
        s = f'''
*** {self.poolName} ***
        
Base Asset: {self.baseAsset}
Quantity in pool: {self.baseQty}
Total liquidity: {self.baseTotal}
        
Token Asset: {self.tokenAsset}
Quantity in pool: {self.tokenQty}
Total liquidity: {self.baseTotal}
'''
        return s

def test():

    chCoin = Asset('Chainge Coin', 0.0043)
    chToken = Asset('Chainge Token', 0.0048)

    testPool = Pool('Test Pool', chCoin, chToken, 12605, 13502)
    print(testPool)

    futurePriceRatio1 = 0.01727  # look this up

    print(f'Future price ratio: {futurePriceRatio1}\n')

    imp_loss = calcImpermanentLoss(testPool.getBaseQty(), testPool.getTokenQty(), futurePriceRatio1)
    print(f'Impermanent loss based on above figures: {imp_loss}')

test()