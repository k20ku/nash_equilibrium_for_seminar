from nashEquilibria import MarketData, Profit, Conditional
OffOn=MarketData(lambda a, b:((-a+b+2)**2)/8,
                'off',
                'on')
p_fn0=OffOn.solveEq()
OffOff=MarketData(lambda a, b:(-a+b+1)/2,
                'off',
                'off')
if __name__=="__main__":

    print(p_fn0)
