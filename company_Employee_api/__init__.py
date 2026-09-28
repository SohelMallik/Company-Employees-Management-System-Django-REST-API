import pymysql

# Spoof the version so Django 6's mysqlclient >= 2.2.1 check passes
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.__version__ = "2.2.1"

pymysql.install_as_MySQLdb()
