# Библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем датафрейм Диабет
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")

# Средний возраст больных диабетом (mean_age_diabetes)
mean_age_diabetes = df.query("Outcome == 1").agg({'Age': 'mean'}).round(2)
print(f'Средний возраст больных диабетом составил: {mean_age_diabetes}')

# График распределения возраста через гистограмму
df = df.query("Outcome == 1")
plt.hist(df['Age'], bins=10, edgecolor='black')

# Добавление заголовков и названия осей
plt.title('Гистограмма распределения возраста больных диабетом')
plt.xlabel('Age')
plt.ylabel('Частота')

# Вывод гистограммы на экран
plt.show()
