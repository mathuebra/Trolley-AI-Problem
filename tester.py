import final
from agents.trolley import Trolley
from agents.bystander import Bystander

bystanders = final.generate_bystander(n=5)

for person in bystanders:
    print(person.status())