from users import Admin
from users import Privilages

new_admin = Admin('daisha', 'davis', 26, 'NYC', ['add posts', 'delete posts', 'ban users', 'delete users'])
new_admin.privilages.show_privilages()