# Job Application AI Agent

Author: **Divyanshu** ([@Divyanshu0230](https://github.com/Divyanshu0230))

An intelligent AI-powered tool that automates the job application process by:
1. Scraping job listings from platforms like LinkedIn
2. Analyzing job descriptions to extract key requirements
3. Automatically tailoring your CV to match job requirements
4. Generating customized cover letters

## Features

- **Job Scraping**: Automatically search and collect job listings from LinkedIn
- **Intelligent Analysis**: Extract key skills and requirements from job descriptions
- **CV Customization**: Tailor your CV to highlight relevant skills for each job
- **Batch Processing**: Generate multiple tailored CVs for different jobs at once
- **User-Friendly Interface**: Simple web interface to control the entire process

## Setup

### Prerequisites

- Python 3.8+
- Chrome browser (for web scraping)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Divyanshu0230/Job-Application-AI-Agent.git
cd Job-Application-AI-Agent
```

2. Run the installation script:
```bash
# On Unix-based systems (macOS, Linux)
./install.sh

# On Windows
install.bat
```

This will:
- Create a virtual environment
- Install all dependencies
- Download the required spaCy language model
- Install the package in development mode

## Usage

### Web Interface

1. Start the web interface:
```bash
# Activate the virtual environment first
source venv/bin/activate  # On Unix-based systems
venv\Scripts\activate.bat  # On Windows

# Start the web app
job-application-ai-agent web
```

2. Open your browser and go to: http://localhost:5000

3. Upload your base CV template

4. Search for jobs by entering a job title and location

5. Generate tailored CVs for all jobs or for specific jobs

### Command Line

The application also provides a command-line interface:

```bash
# Scrape job listings
job-application-ai-agent scrape --keyword "Software Engineer" --location "Berlin" --max-jobs 5

# Generate tailored CVs for all jobs in an Excel file
job-application-ai-agent batch --cv path/to/cv_template.docx --jobs-file path/to/jobs.xlsx

# Generate a tailored CV for a single job description
job-application-ai-agent tailor --cv path/to/cv_template.docx --job path/to/job_description.txt
```

## Project Structure

- `job_application_ai_agent/scraper/`: Job listing scraping modules
- `job_application_ai_agent/cv_modifier/`: CV customization functionality
- `job_application_ai_agent/utils/`: Utility functions and helpers
- `job_application_ai_agent/ui/`: User interface components
- `job_application_ai_agent/outputs/`: Output directories for jobs and CVs
  - `job_application_ai_agent/outputs/jobs/`: Contains Excel files with job listings
  - `job_application_ai_agent/outputs/cvs/`: Contains generated CV files

## Testing

For detailed testing instructions, see [TESTING_GUIDE.md](TESTING_GUIDE.md).

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
