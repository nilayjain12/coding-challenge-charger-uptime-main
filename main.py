#!/usr/bin/env python3
import sys
from read_text import ChargerReportParser
from process_text import ChargerUptimeCalculator
from write_text import ReportWriter

def main(input_file):
    # Step 1: Parse the input file
    parser = ChargerReportParser(input_file)
    parser.read_file()
    parser.parse_station_ids()
    parser.parse_charger_details()
    station_ids, charger_details = parser.get_parsed_data()

    # Step 2: Process the data
    calculator = ChargerUptimeCalculator(station_ids, charger_details)
    report = calculator.generate_report()

    # Step 3: Write the output file
    writer = ReportWriter(report, input_file)
    writer.write_report()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./your_submission <input_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
