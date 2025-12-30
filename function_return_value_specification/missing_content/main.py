def bus_announcements(stops):
    while True:
        for stop in stops:
            yield f"Next stop: {stop}"#formats the identifier, it's an f-string that inserts the 
                            # current value of count into the string

stops_list = ["Central Station", "Main Street", "Park Avenue", "Airport"]
announcer = bus_announcements(stops_list)

# Testing the result
for _ in range(6):
    print(next(announcer))