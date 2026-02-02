def isStrongPassword(password):
    
    if (len(password) < 8) or (not any(char.isdigit() for char in password)) or (not any(char.islower() for char in password)):
        return False
    