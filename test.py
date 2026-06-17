def process_order(order_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    final_amount = total - discount

    print(f"Order ID: {order_id}")
    print(f"Amount: {amount}")
    print(f"Tax: {tax}")
    print(f"Discount: {discount}")
    print(f"Final Amount: {final_amount}")

    return final_amount


def process_invoice(invoice_id, amount):
    tax = amount * 0.05
    total = amount + tax

    if total > 1000:
        discount = total * 0.1
    else:
        discount = 0

    final_amount = total - discount

    print(f"Invoice ID: {invoice_id}")
    print(f"Amount: {amount}")
    print(f"Tax: {tax}")
    print(f"Discount: {discount}")
    print(f"Final Amount: {final_amount}")

    return final_amount
