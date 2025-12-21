def dis(price: int, discount: int | float) -> int | float:
    final_price = price - (price * discount / 100)
    if final_price.is_integer():
        return round(final_price, 0)
    else:
        return round(final_price, 2)


print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))
