import datetime


#title = varchar(50)
def validation_title(title: str) -> bool:
    return (title != "" and len(title) > 0 and len(title) <= 50)

#duration interger
def validation_duration(duration: int) -> bool:
    return (duration > 0 and duration <= 999)

#released date      
def validation_released(released: str) -> bool:
    try:
        datetime.datetime.strptime(released, '%Y-%m-%d')
        return True
    except ValueError:
        return False