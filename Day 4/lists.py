states_of_America = [
    "Delaware",        
    "Pennsylvania",    
    "New Jersey",      
    "Georgia",         
    "Connecticut",     
    "Massachusetts",   
    "Maryland",        
    "South Carolina",  
    "New Hampshire",   
    "Virginia",        
    "New York",        
    "North Carolina",  
    "Rhode Island",    
    "Vermont",         
    "Kentucky",        
    "Tennessee",       
    "Ohio",            
    "Louisiana",       
    "Indiana",         
    "Mississippi",     
    "Illinois",        
    "Alabama",         
    "Maine",           
    "Missouri",        
    "Arkansas",        
    "Michigan",        
    "Florida",         
    "Texas",           
    "Iowa",            
    "Wisconsin",       
    "California",      
    "Minnesota",       
    "Oregon",          
    "Kansas",          
    "West Virginia",   
    "Nevada",          
    "Nebraska",        
    "Colorado",        
    "North Dakota",    
    "South Dakota",    
    "Montana",         
    "Washington",      
    "Idaho",           
    "Wyoming",         
    "Utah",            
    "Oklahoma",        
    "New Mexico",      
    "Arizona",         
    "Alaska",          
    "Hawaii"           
]

print(states_of_America[-1])

# Changing the list  items

print(states_of_America[1])

states_of_America[1]="Pencil"

print(states_of_America[1])


# Adding items to the end of lists

states_of_America.append("Angelaland")
print(states_of_America)


# Adding a bunch of items to the end of the list, ie addding another list to the end.

states_of_America.extend(["New State of America", "Another New State of America"])
print(states_of_America)


# Length of the list

print(len(states_of_America))