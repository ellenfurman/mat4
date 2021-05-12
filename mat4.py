import requests
import urllib   
import json

#read the file
myfile=open("dests.txt",encoding='UTF-8')
myfile=myfile.read()
Lines=myfile.splitlines()
api_key=''

service_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
mydictionary=dict()
mydictionary['origins']='תל אביב'
mydictionary['key'] = api_key
mylist=list()
information=tuple()
i=0
all_dis=list()
all_cities_names=list()

for city in Lines:
    #Request and receive data from web pages
    #Integrity check 
    mydictionary['destinations'] = city
    try:
        url1 = service_url + urllib.parse.urlencode(mydictionary)
        response=requests.get(url1)
        address=city
        url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, api_key)
        response2 = requests.get(url2)
        if response.status_code != 200 or response2.status_code !=200 :
            print("HTTP Error")
        else:
            response=response.json()
            response2=response2.json()
            
            #saving the data in variables
            km=response['rows'][0]['elements'][0]['distance']['text']
            time=response['rows'][0]['elements'][0]['duration']['text']
            latitude=response2['results'][0]['geometry']['location']['lat']
            longitude=response2['results'][0]['geometry']['location']['lng'] 
            
            #make a list with all the cities
            dictionary=dict()
            mylist.append(dictionary)
            information=('distance:'+ km, 'time:' +time, 'longitude:', longitude, 'latitude:' ,latitude)
            dictionary[city]=information
            print("The destination is: " + city)
            print(" the distance is: " + km)
            print( " Duration of arrival to the destination: " + time)
            print( " The meridians are: "+ str(longitude) )
            print(" The latitudes are: "+ str(latitude))
            print()
            
            #make a list with all the distances
            #make a list with all the cities names
            all_dis.append(km)
            all_cities_names.append(city)
            i+=1
    except:
        print("Requests error")
            
#Choose the three cities with the largest distance from Tel Aviv and print them
the_3_Cities=list()   
for km_num in all_dis:
   while len(the_3_Cities)<3 : 
       big_num=max(all_dis) 
       index=all_dis.index(max(all_dis))
       the_3_Cities.append(all_cities_names[index])
       all_dis[index]= '0' 
print("The three cities with the largest distance from Tel Aviv: "+ str(the_3_Cities))   
    


    



    

    
    
