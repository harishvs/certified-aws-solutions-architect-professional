import os
import subprocess
from pathlib import Path

def md_to_pdf(input_dir, output_filename):
  """
  Reads all .md files from a directory and its subdirectories, 
  and combines them into a single PDF file. Logs errors and continues 
  if conversion fails for a specific file.

  Args:
    input_dir: The directory containing the .md files.
    output_filename: The name of the output PDF file.
  """

  md_files = []
  for root, _, files in os.walk(input_dir):
    for file in files:
      if file.endswith(".md"):
        md_files.append(os.path.join(root, file))

  # Use pandoc to convert markdown to PDF
  try:
    subprocess.run(["pandoc"] + md_files + ["-o", output_filename], check=True)
    print(f"Successfully created PDF: {output_filename}")
  except FileNotFoundError:
    print("Error: pandoc is not installed. Please install pandoc.")
  except subprocess.CalledProcessError as e:
    print(f"Error converting to PDF: {e}")
    for file in md_files:
      try:
        subprocess.run(["pandoc", file, "-o", "temp.pdf"], check=True)
        os.remove("temp.pdf")  # Remove the temporary file
      except subprocess.CalledProcessError:
        print(f"Error processing file: {file}")

if __name__ == "__main__":
  dir_name = '01-accounts'
  input_directory = f"./{dir_name}"  # Replace with your directory
  output_pdf = f"{dir_name}.pdf"
  md_to_pdf(input_directory, output_pdf)