# {key:value for key,value in dict.items()}

tea_price_inr={
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_price_usd={tea:price/95 for tea,price in tea_price_inr.items()}
print(tea_price_usd)