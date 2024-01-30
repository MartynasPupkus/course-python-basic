--school_student_list
SELECT student.id, first_name, last_name, classroom_id
    JOIN classroom ON classroom_id = classroom.id