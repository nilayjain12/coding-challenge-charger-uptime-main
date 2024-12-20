from read_text import parsed_station_ids, parsed_charger_details

print("Station IDs:\n", parsed_station_ids, '\n', "Charger Details:\n", parsed_charger_details)

# Sort the parsed charger details based on the charger ids
parsed_charger_details = sorted(parsed_charger_details, key=lambda x: x[0])
print("Sorted Charger Detsils:\n", parsed_charger_details)