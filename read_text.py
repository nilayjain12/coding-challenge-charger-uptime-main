import sys

class ChargerReportParser:
    def __init__(self, file_path):
        # Initialize with the input file path
        self.file_path = file_path
        self.content = []
        self.station_ids = {}
        self.charger_details = []

    def read_file(self):
        # Read the text from input file using the in-built readlines method
        with open(self.file_path, "r") as input_file:
            self.content = input_file.readlines()
        self._clean_content()

    def _clean_content(self):
        # Remove \n from each element to make it simpler
        self.content = [line.rstrip() for line in self.content]
        # Remove empty strings from content
        self.content = [line for line in self.content if line]

    def parse_station_ids(self):
        # Initialize the station dictionary that will hold the list of charger IDs
        i = 1
        while self.content[i] != "[Charger Availability Reports]":
            element = self.content[i].split()  # element is the list of strings
            temp_list = [int(x) for x in element[1:]]  # Convert charger IDs to integers
            self.station_ids[int(element[0])] = temp_list
            i += 1

    def parse_charger_details(self):
        # Extract charger details starting after the '[Charger Availability Reports]' section
        start_index = self.content.index("[Charger Availability Reports]") + 1
        for line in self.content[start_index:]:
            element = line.split()  # Split line into individual elements
            temp_list = []
            for item in element:
                # Convert digits to integers, leave other elements as strings
                temp_list.append(int(item) if item.isdigit() else item)
            self.charger_details.append(temp_list)

    def get_parsed_data(self):
        # Return parsed station IDs and charger details
        return self.station_ids, self.charger_details

if len(sys.argv) != 2:
    print("Usage: python read_text.py <input_file_path>")
    sys.exit(1)

filename = sys.argv[1]

# Create an instance of the parser class
parser = ChargerReportParser(filename)

# Read and parse the file
parser.read_file()
parser.parse_station_ids()
parser.parse_charger_details()

# Get the parsed data
parsed_station_ids, parsed_charger_details = parser.get_parsed_data()

# Print the parsed data (Optional)
# print("Station IDs:\n", parsed_station_ids)
# print("Charger Details:\n", parsed_charger_details)