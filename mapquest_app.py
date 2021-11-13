import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "9HElgHGmgQM1LDzIA0zvMPojX5fY4XH2"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
       
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
       
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        print("Feature Enhancement:")
        highway = json_data["route"]["hasHighway"]                      #Let the users know if their route has Highway
        if highway == 0:
            print("Highway:                 None")
        else:
            print("Highway:                 Yes")
        seasonalClosure = json_data["route"]["hasSeasonalClosure"]       #Let the users know if there is Seasonal Closure on the route
        if seasonalClosure == 0:
            print("Seasonal Closure:        None")
        else:
            print("Seasonal Closure:        Yes")
        accessRestriction = json_data["route"]["hasAccessRestriction"]   #Let the users know if there is Access Restriction
        if accessRestriction == 0:                  
            print("Access Restriction:      None")
        else:
            print("Access Restriction:      Yes")
        unpaved = json_data["route"]["hasUnpaved"]
        if unpaved == 0:                  
            print("Unpaved Road:            None")
        else:
            print("Unpaved Road:            Yes")
        countryCross = json_data["route"]["hasCountryCross]
        if countryCross == 0:                  
            print("Country Cross:           None")
        else:
            print("Country Cross:           Yes")
        ferry = json_data["route"]["hasFerry"]
        if ferry == 0:                  
            print("Ferry:                   None")
        else:
            print("Ferry:                   Yes")

        print("For more detailed information about ")

   
        print("Destination Latitude:    " +  str(json_data["route"]["boundingBox"]["lr"]["lat"]))    
        print("Destination Longitude:   " +  str(json_data["route"]["boundingBox"]["lr"]["lng"]))
        print("=============================================\n")
        print("Type q if you want to exit.\n")
    elif json_status == 402:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("**********************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
