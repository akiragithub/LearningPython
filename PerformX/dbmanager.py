from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, sessionmaker

association_table = None
tt_association = None
class_intervenir_association = None

# Initializing variables

engine = create_engine('sqlite:///school.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
connexion = None


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
    children_1 = relationship("DbIntervenir")  # , secondary=class_intervenir_association)
    # relationship with posseder
    children_2 = relationship("DbPosseder")

    # Base.metadata.create_all(engine)

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

    # Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Student(id='%s', name='%s', surname='%s', moy='%s', class_id='%s', birthday='%s', city='%s', " \
               "country='%s')>" % (self.id, self.name, self.surname, self.moy, self.class_id, self
                                   .birthday, self.city, self.country)


class DbTopic(Base):
    __tablename__ = 'topics'
    name = Column(String, primary_key=True)
    moy_ecole = Column(Float)

    # relationship with 'posseder'
    children = relationship('DbPosseder')
    print("posseder just reffered from DbTopic")
    children_2 = relationship('DbGrade')  # , secondary=association_table)
    children_3 = relationship('DbTeacher')  # , secondary=tt_association)

    # Base.metadata.create_all(engine)

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

    # Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Grade(id='%s', std_id='%s', topic_name='%s', int_1='%s', int_2='%s', int_3='%s', int_4='%s', " \
               "dev_1='%s', dev_2='%s', moy='%s', semester='%s')>" \
               % (self.id, self.std_id, self.topic_name, self.int_1, self.int_2, self.int_3, self.int_4,
                  self.dev_1, self.dev_2, self.moy, self.semester)


class DbTeacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    topic_name = Column(String, ForeignKey('topics.name'))
    diploma = Column(String)
    entry_date = Column(DateTime)
    # Base.metadata.create_all(engine)

    # relationship with intervenir
    child = relationship("DbIntervenir")

    def __repr__(self):
        return "<Teacher(id='%s', name='%s', surname='%s', topic_name='%s', diploma='%s')>" \
               % (self.id, self.name, self.surname, self.topic_name, self.diploma)


class DbIntervenir(Base):
    __tablename__ = 'intervenir'
    class_id = Column(String, ForeignKey('classrooms.id'), primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), primary_key=True)
    isPP = Column(Boolean)

    # Base.metadata.create_all(engine)

    def __repr__(self):
        return "<Intervenir(class_id='%s', teacher_id='%s', isPP='%s')>" % (self.class_id, self.teacher_id, self.isPP)


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

    # Base.metadata.create_all(engine)

    def __repr__(self):
        return "<School(name='%s', moy='%s', moy_bepc='%s', moy_bac='%s', hi_moy_bac='%s', hi_moy_bepc='%s', \
                low_moy_bac='%s', low_moy_bepc='%s', hi_moy_school='%s', low_moy_school='%s') >" \
               % (self.name, self.moy, self.moy_bepc, self.moy_bac, self.hi_moy_bac, self.hi_moy_bepc,
                  self.low_moy_bac, self.low_moy_bepc, self.hi_moy_school, self.low_moy_school)


class DbPosseder(Base):
    __tablename__ = 'posseder'
    class_id = Column(String, ForeignKey('classrooms.id'), primary_key=True)
    topic_name = Column(String, ForeignKey('topics.name'), primary_key=True)
    # topic_name = Column(String, ForeignKey('topics.name'), primary_key=True)
    coeff_classe = Column(Integer)
    moy_classe = Column(Float)

    def __repr__(self):
        return "<Posseder(class_id='%s', topic_name='%s', coeff_classe='%s', moy_classe='%s')>" \
               % (self.class_id, self.topic_name, self.coeff_classe, self.moy_classe)


def additem(item):
    # try:
    session.merge(item)
    session.commit()
    # for re in session.query(DbTeacher):
    #     print("DBTeacher is :", re)
    # except Exception as e:
    #     print("an error occured with database : ", e)
    #     connexion = engine.connect()


def add_all(items=[]):
    for item in items:
        additem(item)
    session.commit()


def get_all(table_name):
    return session.query(table_name).all()


def get_principal_teacher_mle(classname):
    prof = session.query(DbIntervenir.teacher_id).filter_by(class_id=classname, isPP=1).all()  # [0][0]
    if prof:
        prof_1 = prof[0][0]
        print("prof is ", prof_1)
        return prof_1


def get_teacher_by_id(t_id):
    return session.query(DbTeacher).filter_by(id=t_id).all()


def get_all_teachers():
    re = session.query(DbTeacher).order_by(DbTeacher.id).all()
    return re


def get_number_of_students_from_given_class(classname):
    re = session.query(DbStudent.id).filter_by(class_id=classname).count()
    return re


def get_all_students_from_given_classe(classname):
    re = session.query(DbStudent).filter_by(class_id=classname).all()
    return re


def get_all_topics_of_given_classe(classname):
    re = session.query(DbPosseder.topic_name).filter_by(class_id=classname).all()
    return re


def get_number_of_topics_of_given_classe(classname):
    return get_all_topics_of_given_classe(classname).count()


Base.metadata.create_all(engine)
