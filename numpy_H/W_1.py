import numpy as np

days = np.array(["Пн", "Вт",
"Ср", "Чт", "Пт", "Сб", "Вс"])

water_sales = np.array([12, 8,
15, 10, 20, 18, 15])

water_price = 40
print(f"{days[0]}: продано {water_sales[0]} бутылок")
print(f"{days[-1]}: продано {water_sales[-1]} бутылок")

weekdays_sales = water_sales[:5]
print(f"первые пять дней: {water_sales}")

work = np.sum(water_sales)
weekend = np.sum(water_sales[:-2])
print(f"продано всего:{work}")
print(f"продано за выходные: {weekend}")

average_work = np.average(water_sales[0:5])
average_weekend = np.average(water_sales[0:-2])
print(f"среднее за рабочии дни : {average_work}")
print(f"среднее за выходные {average_weekend}")

min_day = np.argmin(water_sales)
max_day = np.argmax(water_sales)
print(f"минимальнок кол-во: {water_sales[min_day]} в день: {days[min_day]}")
print(f"максимальное кол-во: {water_sales[max_day]} в день: {days[max_day]}")

mask = water_sales > 15
print(f"Дни: {days[mask]}")
print(f"Продажи: {water_sales[mask]}")

plan_completed = water_sales >= 15
days_plan_completed = plan_completed.sum()
print(f"Выполнения плана: {days_plan_completed}")


daily_revenue = np.sum(water_sales * water_price)
print(f"Общая выручка: {daily_revenue}")
