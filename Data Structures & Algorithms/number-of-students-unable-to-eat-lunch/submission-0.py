class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while sandwiches and count != len(sandwiches):
            while students and count < len(students): 
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    count = 0
                elif students[0] != sandwiches[0]:
                    temp = students[0]
                    students.pop(0)
                    students.append(temp)
                    count += 1
                    if count == len(sandwiches):
                        break
        return len(students)

        