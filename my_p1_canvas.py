from canvasapi import Canvas
import wget

# Canvas API URL
API_URL = "https://learn.insead.edu"
# Canvas API key
API_KEY = ""

canvas = Canvas(API_URL, API_KEY)

# my user id is 3199
myid = 3199

me = canvas.get_user(myid)

course_map = {
    1043: "Financial Accounting",
    1050: "Financial Markets and Valuation",
    960: "Introduction to Strategy",
    947: "Mandatory P1P2 Calendar",
    1055: "Organizational Behavior",
    1053: "Prices and Markets",
    982: "UDJ"
}

# for k in course_map:
#     print(canvas.get_course(k))

course = canvas.get_course(1050)
