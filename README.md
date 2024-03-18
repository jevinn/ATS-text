# ATS Resume Expert

ATS Resume Expert is a Streamlit application that utilizes Google's Generative AI model, Gemini, to evaluate a candidate's resume against a given job description. The application provides an unbiased and brutally honest assessment of the candidate's strengths, weaknesses, and overall fit for the role.

## Features

- **Job Description Input**: Enter the job description for the position you are recruiting for.
- **Resume Upload**: Upload the candidate's resume in PDF format.
- **Resume Evaluation**: Get a detailed evaluation of the candidate's resume based on the job description.
- **Percentage Match**: Receive a percentage match score indicating how well the candidate's resume aligns with the job description.
- **Keyword Analysis**: Identify missing keywords from the job description in the candidate's resume.
- **Task Analysis**: Understand which tasks from the job description the candidate can perform well and which ones they might struggle with.
- **Hiring Recommendation**: Receive a summary and recommendation on whether the candidate should be hired or rejected for the role.

## Installation

1. Clone the repository:
  git clone https://github.com/jevinn/ats-resume-expert.git
2. Navigate to the project directory:
   cd ats-resume-expert
3. Install the required dependencies:
   pip install -r requirements.txt
4. Set up the Google API key:
   - Create a `.env` file in the project root directory.
   - Add your Google API key to the `.env` file: `GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
3. Open the application in your web browser.
4. Enter the job description in the provided text area.
5. Upload the candidate's resume in PDF format.
6. Click the desired button ("Tell Me About the Resume" or "Percentage match") to get the evaluation results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
