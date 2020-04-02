monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    12: "December",
}

print(monthConversion["Nov"])
print(monthConversion.get(12, "Not a valid key"))