def process_order(order_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    final_amount = total - discount

    print(order_id)
    print(amount)
    print(tax)
    print(discount)
    print(final_amount)
    print("Processing complete")
    print("Order stored in system")

    return final_amount


def process_invoice(invoice_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    final_amount = total - discount

    print(invoice_id)
    print(amount)
    print(tax)
    print(discount)
    print(final_amount)
    print("Processing complete")
    print("Invoice stored in system")

    return final_amount
