class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_lovers = students.count(1)
        burger_lovers = students.count(0)
        for i in range(len(sandwiches)):
            food = sandwiches[i]
            # sandwich
            if food == 1:
                # no sandwich lovers left
                if not sandwich_lovers:
                    return burger_lovers
                sandwich_lovers -= 1
            # burger
            else:
                # no burger lovers left
                if not burger_lovers:
                    return sandwich_lovers
                burger_lovers -= 1
        return 0
 
        