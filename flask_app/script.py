import os
# listdir=["CSS","JS","IMG"]
# for i in listdir:
#     os.makedirs(f"static/{i}")


student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes = [open(_file, encoding='utf-8').read() for _file in student_files]

print(student_files)
print(student_notes)

