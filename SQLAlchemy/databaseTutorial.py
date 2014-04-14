#using sqlalchemy version 0.9.4
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
ed_user.name
#'ed'
ed_user.password
#'edspassword'
str(ed_user.id)
#'None'

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
our_user
#<User(name='ed', fullname='Ed Jones', password='edspassword')>
ed_user is our_user
#True
session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])

ed_user.password = 'f8s7ccs'
session.dirty
#IdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])
session.new
#IdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>, <User(name='mary', fullname='Mary Contrary', password='xxg527')>, <User(name='fred', fullname='Fred Flinstone', password='blah')>])
session.commit()
ed_user.id
#1
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
#[<User(name='Edwardo', fullname='Ed Jones', password='f8s7ccs')>, <User(name='fakeuser', fullname='Invalid', password='12345')>]
session.rollback()
ed_user.name
#u'ed'
fake_user in session
#False
session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
#[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]

for instance in session.query(User).order_by(User.id):
    print instance.name, instance.fullname
#ed Ed Jones
#wendy Wendy Williams
#mary Mary Contrary
#fred Fred Flinstone

for name, fullname in session.query(User.name, User.fullname): 
    print name, fullname
#ed Ed Jones
#wendy Wendy Williams
#mary Mary Contrary
#fred Fred Flinstone

for row in session.query(User, User.name).all(): 
    print row.User, row.name
#<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
#<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
#<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
#<User(name='fred', fullname='Fred Flinstone', password='blah')> fred

for row in session.query(User.name.label('name_label')).all(): 
    print(row.name_label)
#ed
#wendy
#mary
#fred

from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')

for row in session.query(user_alias, user_alias.name).all(): 
    print row.user_alias
#<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
#<User(name='wendy', fullname='Wendy Williams', password='foobar')>
#<User(name='mary', fullname='Mary Contrary', password='xxg527')>
#<User(name='fred', fullname='Fred Flinstone', password='blah')>

for u in session.query(User).order_by(User.id)[1:3]: 
    print u
#<User(name='wendy', fullname='Wendy Williams', password='foobar')>
#<User(name='mary', fullname='Mary Contrary', password='xxg527')>

for name, in session.query(User.name).filter_by(fullname='Ed Jones'): 
    print name
#ed

for name, in session.query(User.name).filter(User.fullname=='Ed Jones'): 
    print name
#ed

#The Query object is fully generative, meaning that most method calls return a new Query object upon which further criteria may be added.
for user in session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones'): 
    print user
#<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>

#See Site for Query Types and How to return Lists

session.query(User).from_statement(
              "SELECT * FROM users where name=:name").params(name='ed').all()
#[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]

from sqlalchemy import func
session.query(func.count('*')).select_from(User).scalar() 
#4

#BUILDING A RELATIONSHIP
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id)) #address.user will be many to one
    #addresses = relationship("Address", order_by="Address.id", backref="user") if done in the user class instead
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all(engine)
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
jack.addresses
#[]

jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')]

jack.addresses[1]
#<Address(email_address='j25@yahoo.com')>

session.add(jack) #cascades and addes the addresses as well
session.commit()

# DOES NOT ASSUME DELETES CASCADE
