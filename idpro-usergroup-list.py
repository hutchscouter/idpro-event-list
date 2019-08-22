#!/usr/bin/python

import meetup.api
import datetime
import time
import sys
 
client = meetup.api.Client('265554f470254875442959826920')
 
orglist = ['Hartford-SpringfieldIAM',
           'D-C-Identity-Access-Management-User-Group',
           'BostonIAM',
           'NewYorkIAM',
           'Philadelphia-Identity-and-Access-Management-User-Group',
           'PittsburghIAM',
           'Providence-Identity-Access-Management-Meetup',
#!         'Birmingham-IAM-Meetup',
           'JacksonvilleIAM',
           'Miami-Fort-Lauderdale-Identity-Access-Management-Meetup'
           'TampaIAM',
           'AtlantaIAM',
           'LouisvilleIAM',
           'CharlotteIAM',
           'RaleighIAM',
           'MemphisIAM',
           'nashvilleIAM',
           'AustinIdentity',
           'DallasIAM',
           'HoustonIAM',
           'RichmondIAM',
           'Chicagoland-IAM-User-Group',
           'Indianapolis-IAM-User-Group',
           'Detroit-Area-IAM-User-Group',
           'Western-Michigan-IAM-User-Group',
           'IAM-User-Group-Twin-Cities',
           'KansasCityIAM',
           'St-Louis-Identity-Access-Management-User-Group',
           'CincinnatiIAM',
           'ClevelandIAM',
           'ColumbusIAM',
           'MilwaukeeIAM',
           'Phoenix-Identity-and-Access-Management-User-Group',
           'Cupertino-IAM-User-Group-Meetup',
           'losangelesIAM',
           'Silicon-Valley-IAM-User-Group',
           'OrangeCountyIAM',
           'Sacramento-Identity-and-Access-Management-User-Group',
           'San-Diego-Identity-Access-Management-IAM-User-Group',
           'bayareaIAM',
           'Denver-Identity-and-Access-Management-User-group',
           'LasVegasIAM',
           'PortlandIAM',
           'SaltLakeCityIAM',
           'SeattleIAM',
           'calgaryiam',
           'TorontoIAM',
           'YULIdentity',
           'Vancouver-Digital-Identity-Meetup',
           'Benelux-Identity-Tech-Talks',
           'Identity-Tech-Talks-France',
           'identityculture',
           'Munchen-Identity-Meetup',
           'Identity-Tech-Talks-Oslo',
#!         'Dubai-Identity-and-Access-Management-IAM-Meetup',
           'London-Identity-Tech-Talks',
           'meetup-group-hMgFlrMV',
           'Canberra-Identity-Tech-Talks',
           'DIG-ID-Melbourne-Digital-Identity-Meetup',
           'DIG-ID-Sydney-Digital-Identity-Meetup',
           'Hong-Kong-Identity-Tech-Talks',
#!         'Bangalore-IAM-Meetup',
           'Mumbai-Identity-Access-Management-IAM-IAG-User-Group',
           'Jakarta-Identity-Tech-Talks',
           'Wellington-Identity-Tech-Talks',
           'Singapore-Identity-Tech-Talks',
           'Colombo-Identity-Access-Management-User-Group']
 
event_list = [[0, "January 1, 2018", "Richmond", "VA", "Fake-IDPro-Group", 12345678, "blah blah"]]
 
for idpname in orglist:
    group_info = client.GetGroup({'urlname': idpname})
    time.sleep(0.4)
    if hasattr(group_info, 'next_event'):
        t = group_info.next_event["time"]
        if group_info.country in ("US", "CA"):
            gstate = group_info.state
        else:
            gstate = group_info.country
        event_list.append([time.localtime(t/1000.), time.strftime('%B %d, %Y',  time.localtime(t/1000.)), group_info.city, gstate, idpname, group_info.next_event["id"], group_info.next_event["name"]])
  
event_list = sorted(event_list, key=lambda x: x[0])
 
for i in range(1, len(event_list)):
        print "<tr>"
        print "<td>" + event_list[i][1] + "</td>"
        print "<td><a href=\"https://www.meetup.com/" + event_list[i][4] + "/\">" + event_list[i][2] + ", " + event_list[i][3] + "</a></td>"
        print "<td><a href=\"https://www.meetup.com/" + event_list[i][4] + "/events/" + event_list[i][5] + "/\" target=\"_blank\" rel=\"noopener\">" + event_list[i][6] + "</a></td>"
        print "</tr>"
 
#!        print "<tr>"
#!        print "<td>" + time.strftime('%B %d, %Y',  time.gmtime(t/1000.)) + "</td>"
#!        print "<td>" + group_info.city + ", " + group_info.state + "</td>"
#!        print "<td><a href=\"https://www.meetup.com/" + idpname + "/events/" + group_info.next_event["id"] + "/\" target=\"_blank\" rel=\"noopener\">" + group_info.next_event["name"] + "</a></td>"
#!        print "</tr>"
 
