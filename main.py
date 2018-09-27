from entities.employee import *
from entities.department import *
from entities.company import *

hartono = employee("Hartono", '1980-01-01', "M", "+62-123-456-789", "hartono@test.com")

finance_department = department("finance", "Finance Department", 5)

hartono.save()

print(finance_department.id)
print(finance_department.name)
print(finance_department.floor)
