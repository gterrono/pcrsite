from api import pcr

class Department(object):
  def __init__(self, raw_dept):
    self.raw = raw_dept
    self.id=raw_dept['id']
    self.name=raw_dept['name']

  @property
  def coursehistories(self):
    return [CourseHistory(pcr(middle=ch['path'])) for ch in self.raw['histories']]

  @property
  def courses(self):
    return [course for ch in self.coursehistories for course in ch.courses]

  @property
  def instructors(self):
    return [instructor for ch in self.coursehistories for instructor in ch.instructors]

class Course(object):
  def __init__(self, raw_course):
    self.raw = raw_course
    self.id=raw_course['id']
    self.name=raw_course['name']
    
  @property
  def instructors(self):
    sections=pcr(middle=''.join(('course/',str(self.id),'/sections')))['values']
    return [instructor['name'] for section in sections for instructor in section['instructors']]


class CourseHistory(object):
  def __init__(self, raw_coursehistory):
    self.raw = raw_coursehistory
    self.id = raw_coursehistory['id']
    self.name = raw_coursehistory['name']
    self.aliases = raw_coursehistory['aliases']

  @property
  def courses(self):
    return [Course(pcr(middle=''.join(('course/',str(rawcourse['id']))))) for rawcourse in self.raw['courses']]

  @property
  def subtitle(self):
    return self.aliases[0]

  def __eq__(self, other):
    return self.id == other.id

  @property
  def instructors(self):
    return set([instructor for course in self.courses for instructor in course.instructors])

  def __hash__(self):
    return hash(self.id)

  def __repr__(self):
    return self.name



