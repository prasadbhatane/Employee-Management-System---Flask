import sqlalchemy as sal
from sqlalchemy.ext.declarative import declarative_base
from db import engine

# for creating a table
metadata = sal.MetaData()
Base = declarative_base()


class Details(Base):
    __tablename__ = 'details'

    # primary key
    Email = sal.Column(sal.String(255), primary_key=True, nullable=False)

    # composite keys
    FirstName = sal.Column(sal.String(255), nullable=False)
    LastName = sal.Column(sal.String(255), nullable=False)
    DateOfBirth = sal.Column(sal.DATE(), nullable=False)
    Mobile = sal.Column(sal.BigInteger, nullable=False)
    Address = sal.Column(sal.String(255), nullable=False)

    def __init__(self, FirstName, LastName, Email, DateOfBirth, Mobile, Address):
        self.FirstName = FirstName
        self.DateOfBirth = DateOfBirth
        self.LastName = LastName
        self.Email = Email
        self.Mobile = Mobile
        self.Address = Address


class Credentials(Base):
    __tablename__ = 'credentials'

    # primary key
    Email = sal.Column(sal.String(255), sal.ForeignKey('details.Email'), primary_key=True, nullable=False)

    # composite keys
    Password = sal.Column(sal.String(255), nullable=False)

    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password


class Role(Base):
    __tablename__ = 'role'

    # primary key
    Email = sal.Column(sal.String(255), sal.ForeignKey('credentials.Email'), primary_key=True, nullable=False)

    # composite keys
    Is_Admin = sal.Column(sal.BOOLEAN(), nullable=False, default=False)

    def __init__(self, Email, Is_Admin):
        self.Email = Email
        self.Is_Admin = Is_Admin


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
