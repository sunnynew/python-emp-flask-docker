from app import app
from flaskext.mysql import MySQL
import os
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'db_emp'

#We are making /etc/hosts file entry on webservers for MySQL server through Ansible playbook. Please check app_playbook.yml for more details. Better to have a route53 inernal DNS configured.
#app.config['MYSQL_DATABASE_HOST'] = 'mysql_server'
#app.config['MYSQL_DATABASE_HOST'] = '10.31.33.208'

app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')

#For localhost testing.
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
