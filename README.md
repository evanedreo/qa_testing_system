# Project Setup Guide

## Cloning the Repository
To get started, clone this repository to your local machine:
```sh
git clone <repository-url>
cd <repository-name>
```

## Setting Up the Environment

### 1️⃣ Delete the old virtual environment
If you have an existing virtual environment, remove it:
```sh
rm -rf .venv
```

### 2️⃣ Create a new virtual environment using Python 3.11
```sh
python3.11 -m venv .venv
```

### 3️⃣ Activate the new virtual environment
- **MacOS/Linux:**
  ```sh
  source .venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```sh
  .venv\Scripts\Activate
  ```

### 4️⃣ Verify that Python 3.11 is now being used
```sh
python --version
```
✅ Expected output:
```sh
Python 3.11.x
```

### 5️⃣ Install dependencies
```sh
pip install --upgrade pip
pip install fastapi uvicorn browser-use
```

## Running the FastAPI App
Start the FastAPI server by running:
```sh
python -m uvicorn main:app --reload
```

## Testing the API
### Set up your API Key
Create a new .env file, and write your OPENAI_API_KEY=example_key
### Create a Task
Run the following command to create a task:
```sh
curl -X POST "http://127.0.0.1:8000/create_task" \
     -H "Content-Type: application/json" \
     -d '{
           "website": "https://qacrmdemo.netlify.app/dashboard",
           "test_type": "search for bugs in the website"
         }'
```

### Retrieve a Task
After you run the command above, you will get a task id
```sh
Example = 
{"task_id":"1d2479d3-5333-413c-8457-30bfb7618725","status":"pending"}   
```
Replace the command below`<task_id>` with the actual task ID:
```sh
curl -X GET "http://127.0.0.1:8000/task/<task_id>"
```

## Example Output
## Input
```sh
curl -X POST "http://127.0.0.1:8000/create_task" \
     -H "Content-Type: application/json" \
     -d '{
           "website": "https://qacrmdemo.netlify.app/dashboard",
           "test_type": "search for bugs in the website"
         }'
```

### Output
{"task_id":"1d2479d3-5333-413c-8457-30bfb7618725","status":"running","results":[]}

### Input 
```sh
evanedreo@evans-mbp-3 qa_testing_system % curl -X GET "http://127.0.0.1:8000/task/1d2479d3-5333-413c-8457-30bfb7618725"
```

### Output
```sh                       
evanedreo@evans-mbp-3 qa_testing_system % curl -X GET "http://127.0.0.1:8000/task/1d2479d3-5333-413c-8457-30bfb7618725"
{"task_id":"1d2479d3-5333-413c-8457-30bfb7618725","status":"finished","results":[{"test_steps":"Steps:\n1. Open the website in a web browser.\n2. Perform a visual inspection of the homepage layout to check for any immediate visual bugs (e.g., misplaced elements, incorrect fonts, broken images).\n3. Navigate through the main sections of the website (Home, About, Services, Contact, etc.).\n4. Check each section for:\n   - Functionality issues (e.g., links not working, buttons not responding).\n   - Layout consistency (e.g., alignment issues, overlapping content).\n   - Cross-browser compatibility by testing in different browsers (e.g., Chrome, Firefox, Safari).\n5. Test responsiveness by resizing the browser window and checking the layout on various screen sizes (simulating different devices).\n6. Use website tools or browser developer tools to monitor for any console errors or loading issues.\n7. Perform user-specific actions (if applicable), such as logging in, signing up, submitting forms, and checking for any errors or unexpected behavior.\n8. Check for backend issues by submitting forms and inspecting the network tab in developer tools for failed requests or incorrect API responses.\n9. Validate that all forms have proper validation and error messages that guide the user.\n10. Assess the website's performance (e.g., page loading times) to ensure it's within acceptable limits.\n11. Review content for accuracy (e.g., spelling errors, outdated information).\n12. Perform any specific test cases that are relevant to the website’s functionality (e.g., transaction processes, search functionalities).","expected_result":"- The website functions correctly across all tested browsers and devices, with no visual or functional bugs.\n- All user interactions (logins, form submissions, etc.) work as intended, with proper error handling and user feedback.\n- No console errors or disrupted network requests during navigation and user actions.\n- Consistent layout and design elements throughout the website.\n- All content is accurate, up-to-date, and displays correctly.\n- The website performance meets required standards, with acceptable load times and resource usage.","actual_result":"Completed testing on qacrmdemo.netlify.app: \n1. Identified database connection error in 'Recent Customers'.\n2. Found layout formatting issues in 'Customers'.\n3. Verified 'Deals', 'Companies' sections with no issues.\n4. Identified missing functionalities in 'Reports'.\n5. Successfully tested form submissions and report generation.\nOverall, functionality is mostly consistent across sections, with noted issues to address for improvement.","bug_analysis":"1. **Bug Classification:** Major Bug\n\n2. **Explanation of the Issue:**\n   - The actual outcome reveals several deviations from the expected outcomes that result in a failure to meet key success criteria:\n     - **Database Connection Error:** The 'Recent Customers' section experiencing a database connection error directly impacts the functionality and interrupts user interaction, which could lead to user confusion and hinder essential operations.\n     - **Layout Formatting Issues:** The problems observed in the 'Customers' section's layout violate the expectation of consistent layout and design elements.\n     - **Missing Functionalities:** In the 'Reports' section, the absence of certain functionalities constitutes a significant deviation from the requirement for all interactions and sections to work as intended.\n\n3. **Suggested Fixes:**\n   - **Database Connection Error:** Investigate and resolve the database connectivity issue in the 'Recent Customers' section, ensuring stable access to necessary data. Implement robust error handling to provide clear feedback to users when such errors occur.\n   - **Layout Formatting Issues:** Review and adjust the CSS and design templates involved in the 'Customers' section to ensure consistency and proper formatting across different devices and browsers.\n   - **Missing Functionalities:** Conduct a thorough assessment to identify missing functionalities in the 'Reports' section. Implement the necessary features to ensure comprehensive and expected user interactions.\n\n4. **Confidence Score:** 95%\n   - The presence of a database connection error, layout issues, and missing functionalities indicates clear departures from the expected behaviors, suggesting a high likelihood of these being legitimate bugs that need addressing."}]}
```

## About
No description, website, or topics provided.

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## License
This project is licensed under [Your License Here].

