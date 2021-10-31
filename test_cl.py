class Test_exapmle:
   def test_check_len(self):
       phrase = input("Set a phrase: ")
       print(len(phrase))
       assert len(phrase)<16, "Lenght of phrase bigger than 15 symbols"
