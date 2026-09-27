def deposit(money):
    balance = 1000

    try:
        amount = float(money)

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

        balance = balance + amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        print(f"สิ้นสุดการฝากเงิน ยอดเงินคงเหลือ: {balance:.2f} บาท")


เรียกใช้ function
money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money)
