people_attending = int(input("Enter the number of people attending: "))
hotdog_per_person = int(input("Enter the number of hotdog per person: "))
total = people_attending * hotdog_per_person
mod_hotdog_package = total % 10
mod_buns_package = total % 8
minimum_hotdog_package = int(total/10)
minimum_buns_package = int(total/8)
if mod_hotdog_package == 0:
    print("minimum hotdog package: " + str(minimum_hotdog_package))
    print("no hotdog left over")
else:
    print("minimum hotdog package: " + str(minimum_hotdog_package))
    print("left over hogdogs: " + str(mod_hotdog_package))
if mod_buns_package == 0:
    print("minimum buns package: " + str(minimum_buns_package))
    print("no buns left over")
else:
    print("minimum buns package: " + str(minimum_buns_package))
    print("left over buns: " + str(mod_buns_package))
