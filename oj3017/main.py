"""[LEARNING LOGS] Bill"""

def main():
    """[LEARNING LOGS] Bill"""
    total = int(input())
    service_charge = total*0.1
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    vat = (total + service_charge) * 0.07
    print(f"{total+service_charge+vat:.2f}")

main()
