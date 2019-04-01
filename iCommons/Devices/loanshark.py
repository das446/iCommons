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
        DevLoanShark.dbo.deviceTypes.typeName

    FROM DevLoanShark.dbo.devices
    INNER JOIN deviceTypes ON devices.typeID=deviceTypes.typeID
    INNER JOIN statusTypes ON devices.statusID=statusTypes.statusID
    INNER JOIN locations ON devices.locationID=locations.locationID
    ;
    """)


    for row in cursor:
        print(row)
    conn.close()


def GetRandomDeviceOfType(device_type):
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
    """.format(device_type)

    cursor.execute(query)

    devices = []

    for row in cursor:
        devices.append(row[0]) 
    conn.close()   
    return random.choice(devices)

def ReserveDevice(device):
    conn = pymssql.connect(server, user, password, "DevLoanShark")
    cursor = conn.cursor()

    get_loan_id_query="""
        SELECT DevLoanShark.dbo.statusTypes.statusID
        FROM DevLoanShark.dbo.statusTypes
        WHERE statusTypes.statusName = 'Loaned Out'
    ;
    """

    cursor.execute(get_loan_id_query)
    t=0
    for type_id in cursor:
        t = type_id
    t = t[0]

    set_query = """
        UPDATE DevLoanShark.dbo.devices
        SET devices.typeID = '{}'
        WHERE devices.name = '{}'
    ;
    """.format(t,device)

    print(device)

    cursor.execute(set_query)
    conn.close()