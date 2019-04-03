from os import getenv
import pymssql
from operator import itemgetter
import random

server = "sqlserv.ischool.drexel.edu"
user = "bouncertest"
password ="justtesting"

def GetAllDevices():
    conn = pymssql.connect(server, user, password, "DevLoanShark")
    cursor = conn.cursor()


    cursor.execute("""
    SELECT 
        DevLoanShark.dbo.devices.name,
        DevLoanShark.dbo.locations.locationName,
        DevLoanShark.dbo.statusTypes.statusName,
        DevLoanShark.dbo.deviceTypes.typeName,
        DevLoanShark.dbo.devices.statusID

    FROM DevLoanShark.dbo.devices
    INNER JOIN deviceTypes ON devices.typeID=deviceTypes.typeID
    INNER JOIN statusTypes ON devices.statusID=statusTypes.statusID
    INNER JOIN locations ON devices.locationID=locations.locationID
    ;
    """)


    for row in cursor:
        print(row)
    conn.close()

GetAllDevices()