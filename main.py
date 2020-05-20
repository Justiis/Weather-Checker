from tkinter import *
import requests

api = "http://api.openweathermap.org/data/2.5/weather?appid=b108bf1ed6f2c40be2ea5a4c0e0f375c&q="

'''WINDOW'''
window = Tk(); window.title('Weather Checker'); window.geometry('400x200+650+300'); window.resizable(0, 0);
city = StringVar()
'''window'''

lab = Label(window, text = 'Enter the name of the city: ', font = 'CGTimes', fg = 'BLACK').grid(row=1, column = 0)
entry = Entry(window, textvariable = city).grid(row=1, column= 3)
labelCity = Label(window, )
def createWeather():
    '''API'''
    json_data = requests.get(api + str(city.get())).json()
    temp = "{0:.2f}".format(json_data['main']['temp'] - 273.15)
    statement = str(json_data['weather'][0]['main'])
    humidity = str(json_data['main']['humidity'])
    '''api'''
    labelCity = Label(window, text = '\n\nCity: ' + city.get(),font = 'Charter', fg = 'BROWN').grid(row = 2, column = 0)
    labelTemp = Label(window, text='Temperature: ' + str(temp), font = 'Charter', fg = 'red').grid(row=3, column=0)
    labelSatement = Label(window, text = 'Statement: ' + statement ,font = 'Charter', fg = 'green').grid(row = 4, column = 0)
    labelHumidity = Label(window, text='Humidity: ' + humidity  + '%',font = 'Charter', fg = 'blue').grid(row=5, column=0)
    resetButton = Button(window, text='EXIT', width=6, height=1, font='Courier', command=exit, fg='RED').grid(row=5,
                                                                                                              column=4)
submitButton = Button(window, text = 'SUBMIT', width= 6, height = 1, font = 'Courier', command = createWeather, fg = 'BLUE').grid(row = 1, column = 4)



window.mainloop()
