#Movie Ticket Booking
email = input("enter your email : ")
movie = input("enter movie name : ")
date = input("enter date : ")
shows_available = ["9:00AM","12:00PM","3:00PM","6:00PM"]
print(shows_available)
time = int(input("enter show time : "))
no_of_tickets = int(input("enter no.of tickets : "))
tickets_cost = 200*no_of_tickets

print("\n")
print("---SJ cinemas📽️ Nagari---")
print(f"BookMyShow - {movie} movie")
print(f"email : {email} ")
print(f"Date : {date}  | show_Time : {shows_available[time-1]}")
print(f"Tickets : {no_of_tickets} | cost💸 : {tickets_cost}")
print("Thank you🙏🙏🙏")
print("\n")