# Data Export to Redis App

This simple application is designed to export data from an XML file into Redis using Docker and Docker Compose. It includes a Python script for parsing the XML data and a Docker environment for easy deployment.

## Reflection and Acknowledgements

Over the years, I have continuously expanded my knowledge and kept myself open to new technologies and methodologies. While I acknowledge that I currently have no exposure to Docker, I am eager to further develop my skills and remain open to learning.

I was able to create a simple app which meets all the requirements mentioned in the task.

*Notes:*

Considering the time allocated for this task, I have done my best to create a Dockerfile, utilize Docker Compose, and develop a Python script for the data export process. I am pleased with the progress made.

Though I have not added tests for this app, I am familiar with several testing frameworks in both JavaScript and Python. Given more time, I could add tests for this app and elaborate more on the solution.

Please feel free to provide any feedback or suggestions for improvement.

## Usage

### Prerequisites

- Docker
- Python 3.8 or higher

### Setting Up and Running the App

1. Clone the repository to your local machine:

   ```
   git clone git@github.com:coderhimanshu1/Emaww_task.git
   ```

2. Navigate to the project directory:

```
cd emaww_task
```

3. Create a virtual environment (optional but recommended):

```python3 -m venv myenv

```

4. Activate the virtual environment:

```
source myenv/bin/activate
```

5. Install the required Python packages:

```pip install -r requirements.txt

```

6. Run the application using the terminal:

```./export.sh ./config.xml

```

This command will build the Docker images, start the containers, and export data from config.xml to Redis.