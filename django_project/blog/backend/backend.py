from ..models import Classroom, Forum, Post, Exam


def create_new_classroom(lesson, grade, class_num, teacher, description=None):
    if description:
        classroom = Classroom(lesson=lesson, grade=grade, class_num=class_num, teacher=teacher)
    else:
        classroom = Classroom(lesson=lesson, grade=grade, class_num=class_num, teacher=teacher, description=description)
    classroom.save()


def add_student_to_classroom(classroom, student):
    student.classrooms_as_student.add(classroom)


def create_forum(title, classroom, description=None):
    if description:
        forum = Forum(title=title, classroom=classroom)
    else:
        forum = Forum(title=title, classroom=classroom, description=description)
    forum.save()


def create_post(content, author, forum_id):
    if match(user=author, forum_id=forum_id):
        post = Post(content=content, author=author, forum=Forum.objects.get(id=forum_id))
        post.save()
        print("post created")
    else:
        print("some problem authenticating")


def create_exam(title, exam_file, classroom, description=None):
    if description:
        exam = Exam(title=title, exam_file=exam_file, classroom=classroom, description=description)
    else:
        exam = Exam(title=title, exam_file=exam_file, classroom=classroom)
    exam.save()


# todo implement condition in which user is a teacher or admin. For now we assume user to be a student
def get_classrooms(user):
    return user.classrooms_as_student.all()


def get_forums(classroom):
    return classroom.forum_set.all()


def get_exams(classroom):
    return classroom.exam_set.all()


def get_posts(forum):
    return sorted(forum.post_set.all(), key=lambda x: x.date_posted)


def exam_belongs_to_classroom(classroom_id, exam_id):
    return Exam.objects.get(id=exam_id).classroom.id == classroom_id


def forum_belongs_to_classroom(classroom_id, forum_id):
    return Forum.objects.get(id=forum_id).classroom.id == classroom_id


def is_member_of_classroom(user, classroom_id):
    return classroom_id in [classroom.id for classroom in get_classrooms(user)]


def match(user=None, classroom_id=None, forum_id=None, exam_id=None):
    ans = True
    # return false if given ids are erroneous
    try:
        if classroom_id:
            Classroom.objects.get(id=classroom_id)
        if forum_id:
            Forum.objects.get(id=forum_id)
        if exam_id:
            Exam.objects.get(id=exam_id)
    except:
        return False

    if classroom_id and user:
        ans = ans and is_member_of_classroom(user, classroom_id)
    if classroom_id and forum_id:
        ans = ans and forum_belongs_to_classroom(classroom_id, forum_id)
    if classroom_id and exam_id:
        ans = ans and exam_belongs_to_classroom(classroom_id, exam_id)
    return ans
