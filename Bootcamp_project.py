
import requests
from datetime import datetime

api_key = 'fc5e653143f65694a3b71637ed43e4bd'
#defined the obtained api key from openweathermap.org
location = input("Enter the city name: ")
#for user's input of the intended city name


complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
# creating the variable so that it gives out value in Celcius by converting the Kelvin tempetature given by API data
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")



print("-------------------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :",wind_spd, 'kmph')

print("====================================================")


    # making a list to print the fetched data to text
txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]
#using open() buit-in function to write to a text file
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
                                     #encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------- \n ")   
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
    f.write("{},{} \n".format("Current weather desc  :" ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("====================================================")

  #completed the project by Dhilanmith Perera by rewriting the code with reference to Harsh sir's source code and adding additional comments deriving from the knowledge gathered during the bootcamp
    
