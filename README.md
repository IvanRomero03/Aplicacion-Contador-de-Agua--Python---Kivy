# Aplicacion-Contador-de-Agua- Python/Kivy

Este proyecto tiene como principal propósito permitir al usuario contabilizar y visibilizar la cantidad de agua que el usuario toma al día.

## To run the proyect
*This proyect is running on python 3.9.10*
#### installing the dependencies:
```
pip install -r requirements.txt
```
#### creating the virtual enviroment
```
python -m virtualenv kivy_venv
```
#### activate the venv (on the **CMD**)
```
kivy_venv\Scripts\activate
```
##### installing the dependencies on the venv
```
pip install -r requirements.txt
```
### to run the ui
```
python PantallaContador.py
```

## Parts of the proyect:
The proyect is divided in 3 main parts, **Visual Interfaze**, **web actuator**, **web hosted data base**
### Visual Interfaze
This part of the proyect was made with Kivy and a simple plot with MatPlotLib. It's a simple interfaze just containing the number of times that someone has drinked water in the day and a histogram of frecuencies with time of the same information
### Web Actuator
This part of the proyect was made with Flask. The web actuator was thinked to be used with an NFC, thanks to overwriting the sticker used. this part is contained in the ![Web Actuator repositorie](https://github.com/IvanRomero03/ActuadorWeb.git) 
### AWS/RDS MySQL Data Base
The data base for this proyect was hosted using the AWS/RDS Hosting with MySQL. The setup for the data base used was made thanks to MySQL workbench, and lastly, the API made for this database was made with the Python driver for MySQL (MySQL Connector/Python). This API is held in *ConectorDB.py*


