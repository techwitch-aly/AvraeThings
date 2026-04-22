def roll_range(low, high):
    """Roll a number uniformly between low and high (inclusive) using vroll."""
    span = int(high- low)
    if span <= 0:
        return int(low)
    result = vroll(f"1d{span}")
    return int(low) + result.total - 1

def roll_step():
    """Returns a value from -5 to +5 using dice rolls."""
    # 1d11 gives 1-11, subtract 6 to get -5 to +5
    result = vroll("1d11")
    return result.total - 6

def get_trended_temp(low, high, trend, prev_temp=None):
    """Trend temperature in a specific direction, anchored by the previous temperature."""
    mid = (low + high) / 2
    span = high - low

    biased_mid = mid + (trend * span * 0.25)

    if prev_temp is None:
        bias_range = span * 0.2
        base = biased_mid + roll_range(-bias_range, bias_range)
    else:
        step = roll_step()
        pull = (biased_mid - prev_temp) * 0.15
        base = prev_temp + step + pull
    
    return int(max(low, min(high, round(base))))

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return int((fahrenheit - 32) * 5 / 9)

def roll_weather_conditions(table):
    """Roll against a probability table to determine weather conditions. Entries are (condition, percent) and must sum to 100."""
    conditionRoll = vroll("1d100").total
    cumulative = 0
    for condition, weight in table:
        cumulative += weight
        if conditionRoll <= cumulative:
            return condition
    return table[-1][0]  # Fallback to last condition if something goes wrong