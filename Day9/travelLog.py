travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_value,times,city_list):
  new_item= dict()
  new_item["country"]=country_value
  new_item["visited"]=times
  new_item["cities"]=city_list
  travel_log.append(new_item)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
for i in travel_log:
  print(f"{i}\n")
print(travel_log[0]["cities"][0])
