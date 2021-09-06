import streamlit as st 
import pandas as pd 
import lasio
st.title("Aplicación para registro de pozos")
st.sidebar.title("Menu")

archivo_las=lasio.read("LGAE-040.las")
df=archivo_las.df()



opciones_inicio=st.sidebar.radio("Seleccione una opción",["Inicio","Datos","Calculos"])
if opciones_inicio=="Inicio":
	st.write("Sección Inicio")
	barra_deslizadora=st.slider("Seleccione un valor",1,100,30)
	st.write(barra_deslizadora)
	ingreso_numero=st.number_input("Ingrese un valor",min_value=0,max_value=1000,value=100)
	st.write(ingreso_numero)
	seleccion=st.selectbox("Seleccione una opción",["a","b","c"])
	st.write(df)
if opciones_inicio=="Datos":
	st.write("Sección Datos")
	st.write(df)
if opciones_inicio=="Calculos":
	st.write("Seccion calculos")


archivo_las2=st.sidebar.file_uploader("Cargar archivo LAS" , type=['.las', '.LAS'], key=None)

age = st.slider('How old are you?', 0, 130, 25)

chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns=['a', 'b', 'c'])
st.area_chart(chart_data)
