from user.users import User
from pathlib import Path
print('hello')
u1 = User('samir',12,5,55,'986999999','basic')
u1.to_dict()
u1.ExporttoJSON(Path("/home/samir-dahal/wokout_school/data"))


