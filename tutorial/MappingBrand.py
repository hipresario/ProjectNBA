import re

#define the dictionary: regex object as key
dict={}
dict[re.compile('([^^A-Za-z]+|^)(coke|coca[^^A-Za-z]*cola|coca|cola)([^^A-Za-z]+|$)')]="CocaCola"
dict[re.compile('[^^A-Za-z]*dr[^^A-Za-z]*pepper[^^A-Za-z]*')]="DrPepper"

#function
def mapping_brand_name (str):
    print ('Input is: '+str)
    output="No_match"
    for regex in dict.keys():
        if regex.search(str) is not None: output=dict[regex]
    return output

#read keyboard input
str=input('Enter the brand: ')

while (str!='exit'):
    brand=mapping_brand_name(str) #call the function
    print ('Output is: '+brand)
    str=input('Enter the brand or exit: ')

print ("Good bye!")

