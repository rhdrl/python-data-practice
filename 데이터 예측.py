from datetime import datetime

sales = [
    [2025, 1, 120],
    [2025, 2, 125],
    [2025, 3, 130],
    [2025, 4, 128],
    [2025, 5, 140],
    [2025, 6, 145],
    [2025, 7, 150],
    [2025, 8, 155],
    [2025, 9, 160],
    [2025, 10, 168],
    [2025, 11, 175],
    [2025, 12, 180]
]

def get_year_sales(year):
    data = []
    for item in sales:
        if item[0] == year:
            data.append(item[2])

    return data

def calculater_average_change(data):
    changes = []
    for i in range(1, len(data)):
        change = data[i] - data[i - 1]
        changes.append(change)

    average_change = sum(changes) / len(changes)
    return average_change

def predict_year(current_year):
    current_sales = get_year_sales(current_year)
    average_change = calculater_average_change(current_sales)
    current = current_sales[-1]
    next_year = current_year + 1
    for month in range(1, 13):
        current = current + average_change
        prediction = round(current)
        sales.append(
            [next_year, month, prediction]
        )
        current = prediction

predict_year(2025)
predict_year(2026)

def search_sales(year, month):
    # 현재 날짜 가져오기
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    for item in sales:
        if item[0] == year and item[1] == month:
            value = item[2]
            if item[0] == year and item[1] == month:
                print(
                    f"{year}년 {month}월 매출은 "
                    f"{value}입니다. "
                )
            elif year == current_year and month <= current_month:
                print(
                    f"{year}년 {month}월 매출은 "
                    f"{value}입니다."
                )
            else:
                print(
                    f"{year}년 {month}월 예상 매출은"
                    f"{value}입니다."
                )
            return
    print("해당 연월의 데이터가 없습니다.")

try:
    year = int(input("연도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))    
    if month < 1 or month > 12:
        print("월은 1~12 사이로 입력하세요.")
    else:
        search_sales(year, month)
except ValueError:
    print("숫자만 입력하세요.")
    