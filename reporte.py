import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/Afgcc132/An-lisis-de-datos-con-Python/refs/heads/main/Notas%20y%20Horas%20de%20estudio.csv')
data.head()

data.info()

#### Podemos ver que el conjunto de datos contiene 6607 registros y 20 columnas, de las cuales:

# 7 son variables numéricas.

# 13 son variables categóricas.

# Algunas variables presentan valores nulos: Teacher_Quality, Parental_Education_Level y Distance_from_Home.

# Configurar estilo de visualización
sns.set(style="whitegrid")

## Vamos a visualizar algunas características interesantes de este conjunto de datos de los estudiantes:
# Histograma de puntajes de exámenes
plt.figure(figsize=(8, 5))
sns.histplot(data['Exam_Score'], bins=30, kde=True, color='blue')
plt.title('Distribución de Puntajes en Exámenes')
plt.xlabel('Puntaje')
plt.ylabel('Frecuencia')
plt.show()

## La media está por el 66 y casi por 70 también la mayoría, muy pocos reprobados y casi nada llegando al 80

# Boxplot de horas de estudio vs. puntaje de examen
plt.figure(figsize=(8, 5))
sns.boxplot(x='Hours_Studied', y='Exam_Score', data=data, palette='Blues')
plt.title('Horas de Estudio vs. Puntaje de Examen')
plt.xlabel('Horas de Estudio')
plt.ylabel('Puntaje de Examen')
plt.xticks(rotation=45)
plt.show()

## Ligera tendencia hacía más hora de estudio mejor calificación pero es poco el cambio y hay algunos outliers que entre tantos datos es normal ver esos cambios

# Comparación de puntajes según el nivel de motivación
plt.figure(figsize=(8, 5))
sns.boxplot(x='Motivation_Level', y='Exam_Score', data=data, palette='Set2')
plt.title('Motivación vs. Puntaje en Examen')
plt.xlabel('Nivel de Motivación')
plt.ylabel('Puntaje de Examen')
plt.xticks(rotation=45)
plt.show()

## Las 3 muy similares pero creo que la motivación media es la que mejores resultados tiene en conjunto, como media está bien

# Relación entre asistencia y puntaje de examen
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Attendance', y='Exam_Score', data=data, alpha=0.5)
plt.title('Asistencia vs. Puntaje de Examen')
plt.xlabel('Asistencia (%)')
plt.ylabel('Puntaje de Examen')
plt.show()

## Me hace sentido porque se relaciona mucho con las horas de estudio y creo que en cierta parte es normal porque los alumnos que mas van tientan a irles mejor

# Gráfico de conteo: distribución de la calidad del profesor según el tipo de escuela
plt.figure(figsize=(8, 5))
sns.countplot(x='Teacher_Quality', hue='School_Type', data=data, palette='coolwarm')
plt.title('Distribución de Calidad del Profesor por Tipo de Escuela')
plt.xlabel('Calidad del Profesor')
plt.ylabel('Cantidad de Estudiantes')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Escuela')
plt.show()

# Boxplot: comparación del puntaje en exámenes por Teacher_Quality y School_Type
plt.figure(figsize=(10, 5))
sns.boxplot(x='Teacher_Quality', y='Exam_Score', hue='School_Type', data=data, palette='Set2')
plt.title('Puntaje en Exámenes según Calidad del Profesor y Tipo de Escuela')
plt.xlabel('Calidad del Profesor')
plt.ylabel('Puntaje de Examen')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Escuela')
plt.show()

## Podemos ver que igual la mayoría son de escuelas públicas y que la calidad de los profesores es mayormente media,ni muy bueno ni malo, también creo que son califiaciones dadas por los alumnos, eso también puede influir.
