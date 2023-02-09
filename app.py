
#Importacion de librerias necesarias
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import joblib 
import base64
import matplotlib.cm as cm
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow import convert_to_tensor

##Funcion predecir resultado   
def predict_result(pel1, pel2):
    
    if pel1 == pel2:
        st.text('Introduce dos peleadores diferentes')
   
    else:
        stats_prediction = pd.read_csv('./df_prediccion_230207.csv')
        cols = stats_prediction.columns[1:]

        stats1 = np.array(stats_prediction[stats_prediction['Name'] == pel1].iloc[:,1:])
        stats2 = np.array(stats_prediction[stats_prediction['Name'] == pel2].iloc[:,1:])

        pred_stats = stats1 - stats2
        df = pd.DataFrame(pred_stats, columns=cols)
        
        scaler = joblib.load('scaler.joblib')
        df.iloc[:, :-5] = scaler.transform(df.iloc[:, :-5])
        
        model = joblib.load('modelo_random_forest.joblib')
        result = model.predict_proba(df)

        if result[0][0]>result[0][1]:
            st.text(f'El peleador {pel1} ganará con una probabilidad de {round(result[0][0]*100)}%')
        elif result[0][0]<result[0][1]:
            st.text(f'El peleador {pel2} ganará con una probabilidad de {round(result[0][1]*100)}%')
        else:
            at.text('No hay datos suficientes para predecir el resultado')
            
        return
##Funcion para visualizar pdf    
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

        
##Titulo global del app
st.title('Money Fighter')

#Menu del streamlit
menu = ['Home', 'Predictions', 'Top 10 Stats', 'User Manual']

choice = st.sidebar.selectbox('Menu', menu)

#carga de los datos
fighter_stats = pd.read_csv('./df_prediccion_230207.csv')
peleadores = fighter_stats['Name'].unique()

#Imagen logo
image = Image.open('./logo_moneyfighter.png') 

if choice == 'Home':
    st.subheader('Home')
    
    #Se crean 3 columnas para centrar el logo en el centro de la pantalla
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(image = image, width=200)
    
    with open('descripcion.txt', 'r') as file:
        text = file.read()
    
    st.markdown(text)
elif choice == 'Predictions':
    st.subheader('Predictions')
    st.text('Choose 2 fighters:')
    
    col1, col2 = st.columns(2)

    with col1:
        #Se muestra la tabla con los datos del primer pelador
        pel1 = st.selectbox('Fighter 1:', peleadores) 
        table1 = fighter_stats[fighter_stats['Name'] == pel1].iloc[:,1:]
        table1.rename({table1.index[0]: pel1}, inplace = True)
        table1 = table1.transpose()
        st.write(table1, format='pretty')

    with col2:
        #Se muestra la tabla con los datos del segundo pelador
        pel2 = st.selectbox('Fighter 2:', peleadores) 
        table2 = fighter_stats[fighter_stats['Name'] == pel2].iloc[:,1:]
        table2.rename({table2.index[0]: pel2}, inplace = True)
        table2 = table2.transpose()
        st.write(table2, format='pretty')

    
    predict = st.button('Predict result')
    if predict:
        #Al hacer click en el boton se ejecuta esta parte del codigo
        predict_result(pel1, pel2)
        stats_front = np.concatenate([table1, table2], axis = 1)
        stats_front = pd.DataFrame(stats_front, index=table1.index, columns=[table1.columns[0], table2.columns[0]])
        stats_front = stats_front.transpose().reset_index()
        
        #Representacion de las estadisticas de cada peleador
        plt.rcParams['font.size'] = 16
        fig, axes = plt.subplots(5,3, figsize= (20,20))
        cmap = cm.get_cmap('viridis')
        color = cmap(np.arange(len(stats_front)) / len(stats_front))
        plt.suptitle('Comparativa de las estadisticas de ambos peleadores', fontsize = 30)
        sns.barplot(x= 'index', y = 'Height', data=stats_front, ax=axes[0,0])
        sns.barplot(x= 'index', y = 'Weight', data=stats_front, ax=axes[0,1])
        sns.barplot(x= 'index', y = 'Reach', data=stats_front, ax=axes[0,2])
        sns.barplot(x= 'index', y = 'W', data=stats_front, ax=axes[1,0])
        sns.barplot(x= 'index', y = 'L', data=stats_front, ax=axes[1,1])
        sns.barplot(x= 'index', y = 'SLpM', data=stats_front, ax=axes[1,2])
        sns.barplot(x= 'index', y = 'Str. Acc.', data=stats_front, ax=axes[2,0])
        sns.barplot(x= 'index', y = 'SApM', data=stats_front, ax=axes[2,1])
        sns.barplot(x= 'index', y = 'Str. Def', data=stats_front, ax=axes[2,2])
        sns.barplot(x= 'index', y = 'TD Avg.', data=stats_front, ax=axes[3,0])
        sns.barplot(x= 'index', y = 'TD Acc.', data=stats_front, ax=axes[3,1])
        sns.barplot(x= 'index', y = 'TD Def.', data=stats_front, ax=axes[3,2])
        sns.barplot(x= 'index', y = 'Sub. Avg.', data=stats_front, ax=axes[4,0])
        sns.barplot(x= 'index', y = 'ufc_bouts', data=stats_front, ax=axes[4,1])
        sns.barplot(x= 'index', y = 'edad', data=stats_front, ax=axes[4,2])
        for i in range(5):
            for j in range(3):
                axes[i,j].set_xlabel('')
        st.pyplot(fig)
        
elif choice == 'Top 10 Stats':
    st.subheader('Top 10 Stats')
    st.markdown('#### En esta pagina podras visualizar el top 10 peleadores segun cada una de sus estadisticas')
    st.markdown('* Selecciona la estadistica que deseas visualizar')
    stat = st.selectbox('Estadística:', fighter_stats.columns[2:-5])
    
    top_10 = fighter_stats[['Name', stat]].sort_values(by=stat, ascending=False).head(10)
    fig, ax = plt.subplots(figsize= (5,5))
    sns.barplot(data = top_10, x = stat, y = 'Name', orient='h')
    st.pyplot(fig)
    
else:
    st.subheader('User Manual')
    st.markdown('#### Memoria del proyecto Money Fighter. Incluye guia de usuario:')
    show_pdf('TFM moneyfighter.pdf')

