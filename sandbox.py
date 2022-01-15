import json
file = open("bushisms.txt","r")
content = file.readlines()
quote_dict = {}
quote_dict['quotes'] = []
quote_dict['date_location'] = []
i=0
mistakes = []
k=0
for j in content:
    if j.find("Click here") == -1:
        quote = j[(j.find('"')):(j.find('—'))].replace('\"',"")
        date_loc = j[(j.find('—') + 1):].replace("\n","")
        if quote == "" or date_loc == "" or j.find('—') == -1:
            mistakes.append(j)
        else:      
            quote_dict['quotes'].append(quote)
            quote_dict['date_location'].append(date_loc)
                
#with open("bushquotes.json", "w+") as outfile:
#    json.dump(quote_dict,outfile)

print("quotes len", len(quote_dict['quotes']))
print("dates len", len(quote_dict['date_location']))
print("mistakes len", len(mistakes))
for m in mistakes:
    print(m)
