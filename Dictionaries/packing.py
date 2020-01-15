# Creates a teacher fucntion
def print_teacher(name, job, topic):

    print(name)
    print(job)
    print(topic)


print_teacher(name='Jacob', job='Instructor', topic='Python')

# kwargs: key-word args:
# this example still runs with extra arguments


def print_teacherPack(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacherPack(name='Jacob', job='Instructor',
                  topic='Python', second_topic='javascript')
