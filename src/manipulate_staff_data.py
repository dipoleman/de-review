def format_staff(staff_data, dept_data):
    
    staff = [[staff['first_name'],staff['last_name'],staff['department']] 
             for staff in staff_data]
    staff_dept = []
    for person in staff:
        for i in range(len(dept_data)):
            if person[2] == dept_data[i]['department_name']:
                staff_dept.append([person[0],person[1],dept_data[i]['department_id']])

    return staff_dept




