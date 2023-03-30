import pandas as pd



#this section takes the list of students from the gradebook and a 
#student list, filters out those that are below 65 and gets their id 
#from the student list
student_list_df = pd.read_csv("students.txt", sep="\t")
gradebook_df = pd.read_excel("gradebook.xlsx")


gradebook_df = gradebook_df[gradebook_df['PERCENTAGE'] < 65]
gradebook_df = gradebook_df[gradebook_df['CLASS'] == gradebook_df['MY CLASS']]

studentNames = gradebook_df['STUDENT'].tolist()

firstNames = []
lastNames = []
for name in studentNames:
    temp = name.split(", ")
    firstNames.append(temp[1])
    lastNames.append(temp[0])

student_list_df = student_list_df.loc[student_list_df['First Name'].isin(firstNames)
                                      & student_list_df['Last Name'].isin(lastNames)]
IDlist = student_list_df['Perm ID'].tolist()
gradeList = gradebook_df['PERCENTAGE'].tolist()

#exporting the ids and grades to excel
exportList = [('ID', 'Grade')]
for i, ID in enumerate(IDlist):
    exportList.append((ID, gradeList[i]))

pd.DataFrame(exportList).to_excel('IDlist.xlsx', header=False, index=False)

