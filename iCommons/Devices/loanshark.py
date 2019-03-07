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
        DevLoanShark.dbo.devices.comments
    FROM DevLoanShark.dbo.devices
    INNER JOIN deviceTypes ON devices.typeID=deviceTypes.typeID
    INNER JOIN statusTypes ON devices.statusID=statusTypes.statusID
    INNER JOIN locations ON devices.locationID=locations.locationID
    ;
    """)


    devices = []
    for row in cursor:
        print(row)
    conn.close()

    return devices

def GetRandomDeviceOfType(t):
    conn = pymssql.connect(server, user, password, "DevLoanShark")
    cursor = conn.cursor()

    query = """
    SELECT 
        DevLoanShark.dbo.devices.name,
        DevLoanShark.dbo.locations.locationName,
        DevLoanShark.dbo.statusTypes.statusName
    FROM DevLoanShark.dbo.devices
    INNER JOIN deviceTypes ON devices.typeID=deviceTypes.typeID
    INNER JOIN statusTypes ON devices.statusID=statusTypes.statusID
    INNER JOIN locations ON devices.locationID=locations.locationID
    WHERE 
        locations.locationName = '104'
        and statusTypes.statusName = 'In Storage'
        and deviceTypes.typeName = '{}'
        and devices.name Like 'CCI-Rush-L%'
    ;
    """.format(t)

    cursor.execute(query)

    devices = []

    for row in cursor:
        devices.append(row[0])    
    return random.choice(devices)