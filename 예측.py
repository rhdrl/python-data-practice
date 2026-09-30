months = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
sale_2025 = [120, 125, 130, 128, 140, 145, 150, 155, 160, 168, 175, 180]

def show_data():
    print("\n[2025년 월별 매출]")

    for i in range(len(months)):
        print(f"{months[i]}: {sale_2025[i]}만원")

def show_average():
    average = sum(sale_2025) / len(sale_2025)
    print(f"\n2025년 월별 매출 평균: {average:.2f}만원")

def show_max_min():
    print(f"\n2025년 최고 매출: {max(sale_2025)}만원")
    print(f"2025년 최저 매출: {min(sale_2025)}만원")

def show_change():
    print("\n[2025년 변화량]")
    for i in range(1, len(sale_2025)):
        change = sale_2025[i] - sale_2025[i - 1]
        print(f"{months[i]}: {change}만원"
              f"{change:+}만원")

def show_trend():
    print("\n[월별 증가 / 감소]")
    for i in range(1, len(sale_2025)):
        change = sale_2025[i] - sale_2025[i - 1]
        if change > 0:
            print(f"{months[i]}: 증가")
        elif change < 0:
            print(f"{months[i]}: 감소")
        else:
            print(f"{months[i]}: 변화 없음")

def calculate_average_change():
    changes = []
    for i in range(1, len(sale_2025)):
        change = sale_2025[i] - sale_2025[i - 1]
        changes.append(change)

    average_change = sum(changes) / len(changes)
    return average_change

def predict_2026():
    average_change = calculate_average_change()
    prediction = sale_2025[-1] + average_change
    print(f"\n평균 변화량: {average_change:.2f}만원")
    print(f"2025년 12월 매출: {sale_2025[-1]}만원")
    print(f"2026 예상 매출: {prediction:.2f}만원")

def predict_2026_monthly():
    average_change = calculate_average_change()
    print("\n[2026년 월별 예상 매출]")
    for i in range(len(sale_2025)):
        prediction = sale_2025[i] + average_change
        print(f"{months[i]}: {prediction:.2f}만원")

        
#---------메뉴 프로그램----------
while True:
    print("\n============================")
    print("    2025년 매출 분석 프로그램"    )
    print("============================")
    print("1. 2025년 월별 매출 확인")
    print("2. 평균 매출")
    print("3. 최고/최저 매출")
    print("4. 월별 변화량 확인")
    print("5. 증가/감소 확인")
    print("6. 평균 변화량")
    print("7. 2026년 예상 매출")
    print("8. 2026년 예상 매출 (월별)")
    print("0. 종료")

    try:
        menu = int(input("메뉴 선택: "))
        if menu == 1:
            show_data()
        elif menu == 2:
            show_average()
        elif menu == 3:
            show_max_min()
        elif menu == 4:
            show_change()
        elif menu == 5:
            show_trend()
        elif menu == 6:
            average_change = calculate_average_change()
            print(f"\n평균 변화량: {average_change:.2f}만원")
        elif menu == 7:
            predict_2026()
        elif menu == 8:
            predict_2026_monthly()
        elif menu == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴 선택입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")