def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

test(10)
test(23)
test(34)
test(64)
test(105)f