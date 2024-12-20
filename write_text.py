from process_text import report
from read_text import filename

class ReportWriter:
    def __init__(self, report, filename):
        self.report = report
        self.filename = filename

    def write_report(self):
        """Write the content of dictionary to the appropriate output file."""
        output_file = self.get_output_filename()
        with open(output_file, "w") as file:
            for i, (key, val) in enumerate(self.report["Final Report"].items()):
                if i > 0:
                    file.write("\n")  # Add a newline before writing from the second item onward
                file.write(f"{key} {val}")

    def get_output_filename(self):
        """Determine the output file name based on the input filename."""
        if self.filename == "input_1.txt":
            return "input_1_my_output.txt"
        else:
            return "input_2_my_output.txt"


if __name__ == "__main__":
    # Create an instance of the ReportWriter class
    report_writer = ReportWriter(report, filename)
    # Write the report to the appropriate file
    report_writer.write_report()