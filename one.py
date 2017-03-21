import csv
import json
# import two
import sys
x = """[{"hof_Details":{"CATEGORY_DESC_ENG":"SC","AADHAR_ID":"780623649996","STATE":"Rajasthan","MOTHER_NAME_ENG":"hurami ","HOUSE_NUMBER_ENG":null,"RELATION_ENG":"Self","DOB":"01/01/1982","ECONOMIC_GROUP":"APL","BUILDING_NO_ENG":null,"BHAMASHAH_ID":"1428-WKMY-25373","STREET_NAME_ENG":null,"IFSC_CODE":"UCBA0003061","M_ID":"0","FAMILYIDNO":"WDYYYGG","PIN_CODE":"342021","LANDLINE_NO":null,"VILLAGE_NAME":"KALAU","GP_WARD":"KALAU","EMAIL":null,"SPOUCE_NAME_ENG":"kishana ram ","IS_RURAL":"Rural","DISTRICT":"Jodhpur","EDUCATION_DESC_ENG":"Literate","ACC_NO":"30610110005033","ADDRESS":"Nayasra, KALAU, Dechu, Jodhpur","INCOME_DESC_ENG":null,"BANK_NAME":"UCO BANK","LAND_MARK_ENG":null,"RATION_CARD_NO":"008503900036","NAME_ENG":"Seeta","MOBILE_NO":"9549783966","GENDER":"Female","FATHER_NAME_ENG":"SUGANA ram ","FAX_NO":null,"BLOCK_CITY":"Dechu"},"family_Details":[{"CATEGORY_DESC_ENG":"SC","STATE":"Rajasthan","MOTHER_NAME_ENG":"Seeta","HOUSE_NUMBER_ENG":null,"RELATION_ENG":"Daughter","DOB":"27/12/2000","MEMBER_AADHAR_ID":null,"ECONOMIC_GROUP":"APL","BUILDING_NO_ENG":null,"BHAMASHAH_ID":"1428-WKMY-25373","STREET_NAME_ENG":null,"IFSC_CODE":null,"M_ID":"2676697","FAMILYIDNO":"WDYYYGG","PIN_CODE":"342021","LANDLINE_NO":null,"VILLAGE_NAME":"KALAU","GP_WARD":"KALAU","EMAIL":null,"SPOUCE_NAME_ENG":null,"IS_RURAL":"Rural","DISTRICT":"Jodhpur","EDUCATION_DESC_ENG":"10 Pass","ACC_NO":null,"ADDRESS":"Nayasra, KALAU, Dechu, Jodhpur","INCOME_DESC_ENG":null,"BANK_NAME":null,"LAND_MARK_ENG":null,"RATION_CARD_NO":"008503900036","NAME_ENG":"neelam ","MOBILE":null,"GENDER":"Female","FATHER_NAME_ENG":"kishana ram ","FAX_NO":null,"BLOCK_CITY":"Dechu"},{"CATEGORY_DESC_ENG":"SC","STATE":"Rajasthan","MOTHER_NAME_ENG":"sita","HOUSE_NUMBER_ENG":null,"RELATION_ENG":"Son","DOB":"13/11/2006","MEMBER_AADHAR_ID":null,"ECONOMIC_GROUP":"APL","BUILDING_NO_ENG":null,"BHAMASHAH_ID":"1428-WKMY-25373","STREET_NAME_ENG":null,"IFSC_CODE":null,"M_ID":"2676699","FAMILYIDNO":"WDYYYGG","PIN_CODE":"342021","LANDLINE_NO":null,"VILLAGE_NAME":"KALAU","GP_WARD":"KALAU","EMAIL":null,"SPOUCE_NAME_ENG":null,"IS_RURAL":"Rural","DISTRICT":"Jodhpur","EDUCATION_DESC_ENG":"5 Pass","ACC_NO":null,"ADDRESS":"Nayasra, KALAU, Dechu, Jodhpur","INCOME_DESC_ENG":null,"BANK_NAME":null,"LAND_MARK_ENG":null,"RATION_CARD_NO":"008503900036","NAME_ENG":"punam","MOBILE":null,"GENDER":"Male","FATHER_NAME_ENG":"kishana ram ","FAX_NO":null,"BLOCK_CITY":"Dechu"},{"CATEGORY_DESC_ENG":"SC","STATE":"Rajasthan","MOTHER_NAME_ENG":"khetu devi ","HOUSE_NUMBER_ENG":null,"RELATION_ENG":"Husband","DOB":"01/08/1974","MEMBER_AADHAR_ID":"530541094061","ECONOMIC_GROUP":"APL","BUILDING_NO_ENG":null,"BHAMASHAH_ID":"1428-WKMY-25373","STREET_NAME_ENG":null,"IFSC_CODE":null,"M_ID":"2676696","FAMILYIDNO":"WDYYYGG","PIN_CODE":"342021","LANDLINE_NO":null,"VILLAGE_NAME":"KALAU","GP_WARD":"KALAU","EMAIL":null,"SPOUCE_NAME_ENG":"Seeta","IS_RURAL":"Rural","DISTRICT":"Jodhpur","EDUCATION_DESC_ENG":"Graduate","ACC_NO":null,"ADDRESS":"Nayasra, KALAU, Dechu, Jodhpur","INCOME_DESC_ENG":null,"BANK_NAME":null,"LAND_MARK_ENG":null,"RATION_CARD_NO":"008503900036","NAME_ENG":"kishana ram ","MOBILE":null,"GENDER":"Male","FATHER_NAME_ENG":"hamira ram ","FAX_NO":null,"BLOCK_CITY":"Dechu"},{"CATEGORY_DESC_ENG":"SC","STATE":"Rajasthan","MOTHER_NAME_ENG":"SEETA ","HOUSE_NUMBER_ENG":null,"RELATION_ENG":"Son","DOB":"08/10/2002","MEMBER_AADHAR_ID":null,"ECONOMIC_GROUP":"APL","BUILDING_NO_ENG":null,"BHAMASHAH_ID":"1428-WKMY-25373","STREET_NAME_ENG":null,"IFSC_CODE":null,"M_ID":"2676698","FAMILYIDNO":"WDYYYGG","PIN_CODE":"342021","LANDLINE_NO":null,"VILLAGE_NAME":"KALAU","GP_WARD":"KALAU","EMAIL":null,"SPOUCE_NAME_ENG":null,"IS_RURAL":"Rural","DISTRICT":"Jodhpur","EDUCATION_DESC_ENG":"5 Pass","ACC_NO":null,"ADDRESS":"Nayasra, KALAU, Dechu, Jodhpur","INCOME_DESC_ENG":null,"BANK_NAME":null,"LAND_MARK_ENG":null,"RATION_CARD_NO":"008503900036","NAME_ENG":"pravin","MOBILE":null,"GENDER":"Male","FATHER_NAME_ENG":"kishana ram ","FAX_NO":null,"BLOCK_CITY":"Dechu"}]}
]"""

x = json.loads(x)

f = csv.writer(open("test1.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["M_ID", "EDUCATION_DESC_ENG","MOBILE_NO"])

for x in x:
    f.writerow([
        x["hof_Details"]["M_ID"],
                x["hof_Details"]["EDUCATION_DESC_ENG"],
                x["hof_Details"]["MOBILE_NO"]
                ])



f1 = file('test2.csv', 'r')
f2 = file('Oppor.csv', 'r')

# # open('test2.csv', 'rb') as f1:
c1 = csv.reader(f1)
# # open('Oppor.csv', 'rb') as f2:
c2 = csv.reader(f2)


for row in c1:
    if row!=0:
        print row