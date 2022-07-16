# 7.	Изготвяне на проекти
# Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
# Вход
# От конзолата се четат 2 реда:
# 1.	Името на архитекта - текст
# 2.	Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]
# Изход
# На конзолата се отпечатва:
# •	"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."
# Примерен вход и изход
# вход	изход		вход	изход
# George
# 4	The architect George will need 12 hours to complete 4 project/s.		Sanya
# 9
# 	The architect Sanya will need 27 hours to complete 9 project/s.

name_of_architect = input()
numbers_of_projects = int(input())

time_for_projects = numbers_of_projects * 3
print(f"The architect {name_of_architect} will need {time_for_projects} hours to complete {numbers_of_projects} "
      f"project/s.")


