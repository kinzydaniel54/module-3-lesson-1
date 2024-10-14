service_tickets = {
    "Ticket-1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket-2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

ticket_counter = 2

def open_ticket():
    '''Creates New Ticket, Assigns Ticket ID, Sets Status to open and returns confirmation.'''
    print("-" * 50)
    global ticket_counter
    ticket_counter += 1
    ticket_id_format = "Ticket-" + str(ticket_counter)
    customer = input("Enter your first name: ")
    print("-" * 50)
    issue = input("Enter the issue your having: ")
    print("-" * 50)
    status = "open"
    service_tickets[ticket_id_format] = {"Customer": customer, "Issue": issue, "Status": status}
    new_ticket = f"Ticket ID: {ticket_id_format} - {service_tickets[ticket_id_format]} has been created."
    print(new_ticket)
    print("-" * 50)

def update_status():
    '''Changes the status to (open/closed) of the given Ticket ID, and returns confirmation.'''
    print("-" * 50)
    try:
        print("Changing the status on the following Ticket")
        ticket_num = input("Enter Ticket Number: ")
        ticket_id = "Ticket-" + ticket_num
        # print("Example: Ticket-(Number Here)")
        # ticket_id = input("Enter Ticket ID: ")
        print("-" * 50)
        if ticket_id in service_tickets:
            old_status = service_tickets[ticket_id]["Status"]
            if old_status == "open":
                service_tickets[ticket_id].update({"Status": "closed"})
            else:
                service_tickets[ticket_id].update({"Status": "open"})
            print(f"Ticket ID: {ticket_id} Status has been updated.")
            print("-" * 50)
        else:
            print(f"Ticket ID: {ticket_id} does not exist.")
            print("-" * 50)
    except ValueError:
        print(f"Ticket ID: {ticket_id} does not exist.")
        print("-" * 50)

def display_tickets():
    '''Displays all Tickets'''
    print("-" * 50)
    for key, value in service_tickets.items():
        print(f"Ticket ID: {key}")
        print(f"Customer: {value['Customer']}")
        print(f"Issue: {value['Issue']}")
        print(f"Status: {value['Status']}")
        print("-" * 50)

keep_running = True
while keep_running:
    print("-" * 50)
    print("Menu:")
    print("1. Open a new service ticket")
    print("2. Update the status of an existing ticket")
    print("3. Display all tickets")
    print("4. Quit")
    option = int(input("Enter Option: "))

    if option == 1:
        open_ticket()
    elif option == 2:
        update_status()
    elif option == 3:
        display_tickets()
    elif option == 4:
        print("-" * 50)
        print("Goodbye")
        keep_running = False
        print("-" * 50)
    else:
        print("-" * 50)
        print("That is not an option")
        print("-" * 50)