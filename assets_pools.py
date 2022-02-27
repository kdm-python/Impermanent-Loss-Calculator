import datetime

#########################################
### LIQUIDITY POOL - IMPERMANENT LOSS ###
#########################################

### ASSETS AND POOLS MODULE

class Asset:
    """Abstract class representing Assets in the pool."""
    assetID = 1

    def __init__(self, name, price, date):
        # date is str or datetime object
        self.name = name  # str
        self.price = price  # float, current pool price of this asset
        self.priceHistory = {date: price}  # dict of dates: prices, could be daily or weekly
        self.id = Asset.assetID
        # maybe initialise the total pool values here instead?
        Asset.assetID += 1

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice, date):
        """newPrice is assumed to be a float value. Date a str or datetime object."""
        self.price = newPrice
        self.priceHistory[date] = newPrice

    def getPriceHistory(self):
        """Print history of Asset price: plot on graph later."""
        for k, v in self.priceHistory.items():
            print(f'{k}: £{v}')

    def __gt__(self, other):
        """Returns True if self's price is greater than other's price."""
        return self.price > other.getPrice()

    def __lt__(self, other):
        """Returns True if self's price is less than other's price."""
        return self.price < other.getPrice()

    def __eq__(self, other):
        """Returns True if self's price is equal to other's price."""
        return self.price == other.getPrice()

    def __str__(self):
        s = f'{self.name}: £{self.price}'
        return s

class Coin(Asset):
    """Represents the coin in the pool. Attributes specific to coins?"""
    pass

class Token(Asset):
    """Represents the token in the pool. Attributes specific to tokens?"""
    pass

class Pool:
    """Represents a liquidity pool containing coins as assets."""

    def __init__(self, poolName, coinAsset, tokenAsset, coinQty, tokenQty):
        self.poolName = poolName  # str
        self.coinAsset = coinAsset  # Coin object
        self.coinQty = coinQty  # float
        self.tokenAsset = tokenAsset  # Token object
        self.tokenQty = tokenQty  # float

    def getName(self):
        return self.poolName

    def getCoinAsset(self):
        """Return associated Coin object."""
        return self.coinAsset

    def getTokenAsset(self):
        """Return associated Token object."""
        return self.tokenAsset

    def getCoinQty(self):
        """Return current quantity of coins in pool"""
        return self.coinQty

    def getTokenQty(self):
        """Return current quantity of coins in pool"""
        return self.tokenQty

    def getCoinTotal(self):
        """Return total value of the coins in the pool."""
        return self.coinAsset.getPrice() * self.coinQty

    def getTokenTotal(self):
        """Return total value of the tokens in the pool."""
        return self.tokenAsset.getPrice() * self.tokenQty

    def setCoinQty(self, newQty):
        """Set new quantity of coins in the pool. Assumes newQty is float."""
        self.coinQty = newQty

    def setTokenQty(self, newQty):
        """Set new quantity of tokens in the pool. Assumes newQty is float."""
        self.tokenQty = newQty

    def __str__(self):
        s = f'''
*** {self.poolName} ***

{self.coinAsset.getName()}
Quantity of coins in pool = {self.coinQty}
Current market value: £{self.coinAsset.getPrice()}
Total value of coins in the pool: £{int(self.getCoinTotal())}

{self.tokenAsset.getName()}
Quantity of tokens in pool = {self.tokenQty}
Current market value: £{self.tokenAsset.getPrice()}
Total value of tokens in the pool: £{int(self.getTokenTotal())}
'''
        return s

def createCoin(name, price):
    """Create a new Asset object."""
    return Coin(name, price, '05/03/2022')

def createToken(name, price):
    """Create a new Asset object."""
    return Token(name, price, '05/03/2022')

def createPool(poolName, coinAsset, tokenAsset, coinQty, tokenQty):
    """Create a new Pool object."""
    return Pool(poolName, coinAsset, tokenAsset, coinQty, tokenQty)

def calcLoss(priceHistory, investment):
    """Use the price history (dict) to calculate the expected loss on a
    given investment (float) in the pool. Not sure how yet."""
    pass

def test():
    chCoin = createCoin('Chainge Coin', 45.67)
    print(f'{chCoin.getName()} asset created: £{chCoin.getPrice()}')
    chToken = createToken('Chainge Token', 48.54)
    print(f'{chToken.getName()} asset created: £{chToken.getPrice()}')
    chPool = createPool('Chainge Liquidity Pool', chCoin, chToken, 5000, 4500)
    print(f'{chPool.getName()} created containing the above assets.')
    print(chPool)

    newPrice1 = 52.67
    newDate1 = '12/03/2022'
    newPrice2 = 54.82
    newDate2 = '15/03/2022'
    chCoin.setPrice(newPrice1, newDate1)
    print(f'{chCoin.getName()} price set to £{newPrice1} on {newDate1}')
    chCoin.setPrice(newPrice2, newDate2)
    print(f'{chCoin.getName()} price set to £{newPrice2} on {newDate2}')
    print(f'\nGet price history for {chCoin.getName()}:')
    chCoin.getPriceHistory()

test()
