from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, sessionmaker

association_table = None
tt_association = None
class_intervenir_association = None

# Initializing variables

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
#
# class_intervenir_association = Table('class_intervenir_association', String, Column('class_id',
#                                                                                     ForeignKey('classrooms.id')),
#                                      Column('intervenir_id', String, ForeignKey('intervenir.class_id')))


def __init__(self):
    pass


class DbClassroom(Base):
    __tablename__ = 'classrooms'
    id = Column(String, primary_key=True)
    nb_students = Column(Integer)
    moy = Column(Float)

    # relationship with students
    children = relationship("DbStudent")
    # relationship with intervenir
    children_1 = relationship("DbIntervenir", secondary=class_intervenir_association)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Classroom(id='%s', nb_students='%s', moy='%s')>" % (self.id, self.nb_students, self.moy)

class DbStudent(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    moy = Column(Float)
    class_id = Column(String, ForeignKey('classrooms.id'))
    birthday = Column(DateTime)
    city = Column(String)
    country = Column(String)

    # relationship with grades
    children = relationship('DbGrade')

    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Student(id='%s', name='%s', surname='%s', moy='%s', class_id='%s', birthday='%s', city='%s', " \
               "country='%s')>" % (self.id, self.name, self.surname, self.moy, self.class_id)


class DbTopic(Base):
    __tablename__ = 'topics'
    name = Column(String, primary_key=True)
    moy_ecole = Column(Float)

    # relationship with 'posseder'
    children = relationship('DbPosseder')
    children_2 = relationship('DbGrade') #, secondary=association_table)
    children_3 = relationship('DbTeacher')# , secondary=tt_association)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Topic(name='%s', moy_ecole='%s')>" % (self.name, self.moy_ecole)


class DbGrade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    std_id = Column(String, ForeignKey('students.id'))
    topic_name = Column(String, ForeignKey('topics.name'))
    int_1 = Column(Float)
    int_2 = Column(Float)
    int_3 = Column(Float)
    int_4 = Column(Float)
    dev_1 = Column(Float)
    dev_2 = Column(Float)
    moy = Column(Float)
    semester = Column(Integer, default=1)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Grade(id='%s', std_id='%s', topic_name='%s', int_1='%s', int_2='%s', int_3='%s', int_4='%s', " \
               "dev_1='%s', dev_2='%s', moy='%s', semester='%s')>" \
               % (self.id, self.std_id, self.topic_name, self.int_1, self.int_2, self.int_3, self.int_4,
                  self.dev_1, self.dev_2, self.moy, self.semester)

class DbTeacher(Base):
    __tablename__= 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    topic_name = Column(String)
    diploma = Column(String)
    Base.metadata.create_all(engine)

    # relationship with intervenir
    child = relationship("DbIntervenir")

    def __repr__(self):
        return "<Teacher(id='%s', name='%s', surname='%s', topic_name='%s', diploma='%s')>" \
               % (self.id, self.name, self.surname, self.topic_name, self.diploma)

class DbIntervenir(Base):
    __tablename__ = 'intervenir'
    class_id = Column(String, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), primary_key=True)
    isPP = Column(Boolean)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Teacher(class_id='%s', teacher_id='%s', isPP='%s')>"%(self.class_id, self.teacher_id, self.isPP)

class DbSchool(Base):
    __tablename__ = 'school'
    name = Column(String, primary_key=True)
    moy = Column(Float)
    moy_bepc = Column(Float)
    moy_bac = Column(Float)
    hi_moy_bac = Column(Float)
    low_moy_bac = Column(Float)
    hi_moy_bepc = Column(Float)
    low_moy_bepc = Column(Float)
    hi_moy_school = Column(Float)
    low_moy_school = Column(Float)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<School(name='%s', moy='%s', moy_bepc='%s', moy_bac='%s', hi_moy_bac='%s', hi_moy_bepc='%s', \
                low_moy_bac='%s', low_moy_bepc='%s', hi_moy_school='%s', low_moy_school='%s') >" \
               % (self.name, self.moy, self.moy_bepc, self.moy_bac, self.hi_moy_bac, self.hi_moy_bepc,
                  self.low_moy_bac, self.low_moy_bepc, self.hi_moy_school, self.low_moy_school)

class DbPosseder(Base):
    __tablename__= 'posseder'
    class_id = Column(String, ForeignKey('classrooms.id'), primary_key=True)
    topic_name = Column(String, ForeignKey('topics.name'), primary_key=True)
    topic_name = Column(String, primary_key=True)
    coeff_classe = Column(Integer)
    moy_classe = Column(Float)
    Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Posseder(class_id='%s', topic_name='%s', coeff_classe='%s', moy_classe='%s')>" \
               % (self.class_id, self.topic_name, self.coeff_classe, self.moy_classe)


def additem(self, item):
    session = self.Session()
    session.add(item)

tt_association = Table('t_t_association', Base.metadata, Column('t_topics_name', String, ForeignKey('topics'
                                                                                                    '.name'))
                       , Column('topics_name', Integer, ForeignKey('teachers.topic_name')))

association_table = Table('association', Base.metadata, Column('posseder_topic_name', String, ForeignKey('topics'
                                                                                                         '.name'))
                          , Column('topics_name', String, ForeignKey('posseder.topic_name')))
