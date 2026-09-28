def get_user_role(status_code):
    match status_code:
        case 1:
            return "Admin"
        case 2:
            return "Editor"
        case 3:
            return "Guest"
        case _:  
            return "Unknown User"

print(get_user_role(2))   
print(get_user_role(99)) 