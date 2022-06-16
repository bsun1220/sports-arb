# Everything will be converted to decimal odds

def american_to_dec(bet):
    if bet > 0:
        return bet/100 + 1
    elif bet < 0:
        return - 100/bet +1

def frac_to_dec(bet):
    return bet + 1

def calculate_prob(odds):
    return 1/odds

def calculate_profit(bet, stake):
    return (bet - 1) * stake