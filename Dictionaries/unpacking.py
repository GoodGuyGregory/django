programmer = {
    'name': 'Greg',
    'job': 'Back-End Dev',
    'topic': 'Python'
}


def print_programmer(name, job, topic):
    print(name)
    print(job)
    print(topic)


#  In order to unpack the programmer object we could use the following syntax
print(print_programmer(**programmer))
