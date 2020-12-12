# class SomeClassWithContext:
#     def __enter__(self):
#         print("менеджер контекста хабдыщ")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("менеджер контекста всё")
#
# c = SomeClassWithContext()
#
# with c as _:
#     print("чёто")

with open("text.txt", "w") as fh:
    fh.writelines(['hhh', 'hhh', 'kkk'])
    fh.seek(fh.tell()//2)
    fh.write('ggg')
