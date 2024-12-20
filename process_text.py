import math
from read_text import parsed_station_ids, parsed_charger_details

class ChargerUptimeCalculator:
    def __init__(self, station_ids, charger_details):
        # Initialize with parsed station IDs and charger details
        self.station_ids = station_ids
        self.charger_details = sorted(charger_details, key=lambda x: x[0])
        self.uptime_report = {}
        self.chargers_times = {}
        self.station_time = {}
        self.final_result = {}

    def calculate_uptime(self):
        # Calculate the total uptime for each station
        for station_id, charger_ids in self.station_ids.items():
            total_uptime = 0

            for charger in charger_ids:
                time_taken = 0

                for c_id_element in self.charger_details:
                    if c_id_element[3] == 'true':  # Check if the charger is up
                        if charger == c_id_element[0]:
                            start, end = c_id_element[1], c_id_element[2]
                            time_taken = end - start
                            total_uptime += time_taken

                        # Track start and end times for each charger
                        key = c_id_element[0]
                        start = c_id_element[1]
                        end = c_id_element[2]

                        if key not in self.chargers_times:
                            self.chargers_times[key] = [start, end]
                        else:
                            self.chargers_times[key][0] = min(self.chargers_times[key][0], start)
                            self.chargers_times[key][1] = max(self.chargers_times[key][1], end)

            self.uptime_report[station_id] = total_uptime

    def calculate_station_time(self):
        # Calculate the total operational time for each station
        for station_id, charger_ids in self.station_ids.items():
            total_time = 0

            for charger_id in charger_ids:
                start, end = self.chargers_times.get(charger_id, (0, 0))
                total_time += (end - start)

            self.station_time[station_id] = total_time

    def calculate_uptime_percentage(self):
            # Calculate the uptime percentage for each station
            for station_id, c_time in self.uptime_report.items():
                total_c_time = self.station_time.get(station_id, 0)
                if total_c_time > 0:  # Avoid division by zero
                    self.final_result[station_id] = math.floor((c_time / total_c_time) * 100)
                else:
                    self.final_result[station_id] = 0  # Include stations with 0 uptime

    def generate_report(self):
        # Generate the final report
        self.calculate_uptime()
        self.calculate_station_time()
        self.calculate_uptime_percentage()
        return {
            "Uptime Report": self.uptime_report,
            "Chargers Time": self.chargers_times,
            "Station Time": self.station_time,
            "Final Report": self.final_result
        }


# Instantiate the class with parsed data
calculator = ChargerUptimeCalculator(parsed_station_ids, parsed_charger_details)

# Generate the report
report = calculator.generate_report()

# Print the results (Optional)
# print("Final Report:", report["Final Report"])
