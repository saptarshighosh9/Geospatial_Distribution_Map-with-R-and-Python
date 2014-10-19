import sys
import urllib
import urllib2
import time
import datetime
import json
import webbrowser
import csv

ACCESS_URL = "https://graph.facebook.com/"

def collect_data():	
    k=0
    print "\n\n"
    print " #############################################_________________Facebook API information access System____________________#############################################"
    print "***********************************************************************************************************************************************************************"
    print "                                                                        Developed by Gooblu"
    webbrowser.open("https://www.facebook.com/dialog/oauth?"
                    "response_type=token&client_id=145634995501895&"
                    "redirect_uri=http://developers.facebook.com/tools/"
                    "explorer/callback&scope=user_birthday,user_friends,publish_actions"
                    ",read_stream")
    
    webbrowser.open("http://developers.facebook.com/tools/explorer")
    ACCESS_TOKEN = raw_input("\nEnter the TOKEN string obtained from API "
                           "explorer page: \n")
   
    print "\n\n\n"
    print "Downloading Users Information"
   	
    while(k<450):  
        datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(hometown)&access_token='+ACCESS_TOKEN)
        df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)  
        pt=""    
        if 'hometown' in json.loads(datafile.read())['friends']['data'][k]:
            	
            datafile.close()
            ud=json.loads(df.read())['friends']['data'][k]['name']
            df.close()
            df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)
            udd=json.loads(df.read())['friends']['data'][k]['id']
            df.close()
            datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(hometown)&access_token='+ACCESS_TOKEN)
            bb=json.loads(datafile.read())['friends']['data'][k]['hometown']['name']
            datafile.close()
            decode_address_to_coordinates(bb)             
        k=k+1
        t=(k/450)
        sys.stdout.write("Download progress: %d /450   \r" % (k) )
        sys.stdout.flush()
        
    print "\nData download completed"
    raw_input()


def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'true',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        log=result['results'][0]['geometry']['location']['lng']
        lat=result['results'][0]['geometry']['location']['lat']
        
        p='%f,%f'%(log,lat)
        myfile=open("test.csv", "a")
        myfile.write(p + "\n")

    
if __name__ == "__main__":
   collect_data()
