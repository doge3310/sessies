from peewee import MySQLDatabase, Model, \
    AutoField, CharField, ForeignKeyField, \
    DateField, IntegerField, DateTimeField, SQL
import pymysql
from pymysql import MySQLError
from datetime import datetime, date

password = "1234"
user = "root"
host = "localhost"
port = 3306
db_name = "users_1"


def init():
    try:
        database_connect = pymysql.connect(user=user,
                                        password=password,
                                        host=host)

        with database_connect.cursor() as cursor:
            cursor.execute(f"create database if not exists {db_name}")

    except MySQLError as e:
        print(e)

    finally:
        if "database_connect" in locals() and database_connect:
            database_connect.close()


init()

db_connect = MySQLDatabase(db_name,
                           user=user,
                           password=password,
                           host=host,
                           port=port)


class Table(Model):
    id = AutoField()

    class Meta:
        database = db_connect


class VendModel(Table):
    name = CharField()


class VendStatus(Table):
    name = CharField()


class Role(Table):
    name = CharField()


class Employer(Table):
    first_name = CharField()
    mid_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = CharField()
    role = ForeignKeyField(Role)


class VendMachine(Table):
    adress = CharField()
    model = ForeignKeyField(VendModel)
    name = CharField()
    money = IntegerField()
    ser_num = CharField()
    invent_num = CharField()
    firm = CharField()
    modem = CharField()
    date_expluatation = DateField()
    date_created = DateField()
    date_last_test = DateField()
    test_interval = IntegerField()
    resource = IntegerField()
    next_fix_date = DateField()
    fix_time = IntegerField()
    status = ForeignKeyField(VendStatus)
    create_country = CharField()
    invent_date = DateField()
    employer = ForeignKeyField(Employer)
    date_inserted = DateTimeField(default=date.today().strftime("%d.%m.%Y"))

    class Meta:
        dattim = date.today()
        constraints = [SQL("check (resource >= 0)"),
                       SQL("check (next_fix_date > date_inserted)"),
                       SQL("check (fix_time between 1 and 20)"),
                       SQL(f"check (invent_date between date_created and '{dattim}')")]


class Product(Table):
    name = CharField()
    description = CharField()
    price = IntegerField()
    count = IntegerField()
    min_count = IntegerField()
    sale_tendency = CharField()


class Fix(Table):
    machine = ForeignKeyField(VendMachine)
    fix_date = DateField()
    description = CharField()
    problem = CharField()
    employer = ForeignKeyField(Employer)


def main():
    test, _ = VendModel.get_or_create(
        name="test_model"
    )

    test, _ = VendStatus.get_or_create(
        name="work"
    )

    test, _ = Role.get_or_create(
        name="admin"
    )

    test, _ = Employer.get_or_create(
        email="test@sdfg",
        phone="678905",
        defaults={
            "first_name": "sdfghdd",
            "mid_name": "dfghj",
            "last_name": "dh",
            "role": 1
        }
    )

    test, _ = VendMachine.get_or_create(
        ser_num="8h95743",
        defaults={
            "adress": "sh",
            "model": 1,
            "money": 34567,
            "invent_num": "drgs",
            "firm": "jdfghloni",
            "date_expluatation": "11.11.2000",
            "date_created": "11.11.2001",
            "date_last_test": "11.11.2002",
            "test_interval": 1231,
            "resource": 123,
            "next_fix_date": "11.11.2003",
            "fix_time": 12,
            "status": 1,
            "country": "Russia",
            "invent_date": "12.12.2000",    # yyyy-dd-mm
            "employer": 1,
        }
    )
    test, _ = VendMachine.get_or_create(
        ser_num="8h9574",
        defaults={
            "adress": "sh",
            "model": 1,
            "money": 34567,
            "invent_num": "drgs",
            "firm": "jdfghloni",
            "date_expluatation": "11.11.2000",
            "date_created": "11.11.2001",
            "date_last_test": "11.11.2002",
            "test_interval": 1231,
            "resource": 123,
            "next_fix_date": "11.11.2003",
            "fix_time": 12,
            "status": 1,
            "country": "Russia",
            "invent_date": "12.12.2000",    # yyyy-dd-mm
            "employer": 1,
        }
    )

    test, _ = Product.get_or_create(
        name="dfghs",
        defaults={
            "description": "sdfghsghsghf",
            "price": 12341,
            "count": 123,
            "min_count": 123,
            "sale_tendency": "dfghj"
        }
    )

    test, _ = Fix.get_or_create(
        machine=1,
        defaults={
            "fix_date": "11.11.1111",
            "description": "fghd;dfgh",
            "problem": "sndg",
            "employer": 1
        }
    )


if __name__ == "__main__":
    db_connect.create_tables([VendMachine,
                              VendStatus,
                              Role,
                              Employer,
                              VendModel,
                              Product,
                              Fix])
    main()
