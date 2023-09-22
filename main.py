def divider(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You can't divide by zero")
        return
    except TypeError:
        print("You can't divide non-numeric values")
        return
    except ValueError:
        print("You can't divide non-numeric values")
        return
data = {10: 2, 2: 5, "123": 4, 15: 15, 18: 0, 8: 4}
result = []
for key in data:
    res = divider(key, data[key])
    result.append(res)
print(result)