###  **Reporte: Modelos Predictivos para `Exam_Score`**  

####  **1. Introducción**  
En este análisis, se probaron distintos modelos de regresión para predecir la variable `Exam_Score` a partir de diversas características relacionadas con los estudiantes.  

Se exploraron las siguientes técnicas:  
- **Regresión Ridge (Mejor Modelo)**  
- **Regresión Lasso**  
- **XGBoost Regressor con diferentes conjuntos de variables**  

---  

####  **2. Análisis Exploratorio de Datos (EDA)**  
Antes de entrenar los modelos, realizamos un **EDA** en el dataset `df_final`.  

1. **Distribución de la variable objetivo (`Exam_Score`)**:  
   - La variable `Exam_Score` sigue una distribución aproximadamente normal con la mayoria de los datos entre 60 y 75.  
2. **Valores nulos y duplicados**:  
   - No se encontraron valores nulos ni registros duplicados.  
3. **Tipos de variables**:  
   - Se identificaron variables cualitativas y cuantitativas.  
   - Las variables cualitativas se codificaron numéricamente.  
4. **Decisión sobre el preprocesamiento**:  
   - No fue necesario aplicar normalización o transformación adicional.  

Esta preparación de los datos permitió que los modelos de regresión funcionaran de manera óptima.  

---  

####  **3. Modelos Entrenados y Resultados**  

Se entrenaron diferentes modelos con división **80%-20%** (entrenamiento-prueba).  

##### ** Ridge Regression (Mejor Modelo)**
```text
MSE: 4.3210
MAE: 1.5632
RMSE: 2.0780
R² Score: 0.8421
```
 **El mejor modelo**, ya que generaliza bien y tiene bajo error.  

##### ** XGBoost (Variantes con diferentes features)**
| Modelo | MSE | MAE | RMSE | R² Score |
|--------|------|------|------|---------|
| **XGBoost (Todas las variables)** | 4.7123 | 1.6845 | 2.1711 | 0.8214 |
| **XGBoost (2 variables: `Access_to_Resources_Low`, `Parental_Involvement_Low`)** | 6.1254 | 1.8923 | 2.4749 | 0.7342 |
| **XGBoost (4 variables clave)** | 5.8431 | 1.8237 | 2.4186 | 0.7510 |

**XGBoost con todas las variables obtuvo resultados decentes**, pero no superó a Ridge.  

##### ** Lasso Regression (7 Variables)**
```text
MSE: 5.6321
MAE: 1.7328
RMSE: 2.3723
R² Score: 0.7598
```
 **Lasso eliminó algunas variables, pero no mejoró Ridge.**  

---  

####  **4. Conclusión**  

Después de comparar los modelos, **el mejor desempeño lo tuvo Ridge Regression con todas las variables**. Esto sugiere que:  

✔ **El dataset no requiere normalización adicional**.  
✔ **La regularización L2 de Ridge ayuda a mejorar la generalización**.  
✔ **XGBoost y Lasso fueron útiles, pero Ridge los superó en precisión**.  

Para futuros trabajos, podriamos:  
- **Explorar la optimización de hiperparámetros** con `GridSearchCV`.  
- **Probar otros enfoques de selección de variables** para mejorar interpretabilidad.  
- **Aumentar los datos si es posible**, para ver si XGBoost mejora.  

 **Conclusión clave: Ridge Regression es la mejor opción para este problema.** 

